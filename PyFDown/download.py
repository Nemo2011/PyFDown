import signal
import tqdm
import requests
import multitasking
from retry import retry
signal.signal(signal.SIGINT, multitasking.killall)


def split(end, step):
    parts = [(start, min(start + step, end)) for start in range(0, end, step)]
    return parts

def size(url, headers: dict={'User-Agent': 'Mozilla/5.0'}):
    res = requests.head(url, headers=headers)
    fs = res.headers.get('Content-Length')
    if fs:
        return int(fs)
    else:
        return 0

def download(url, file, retry_times=3, chunks=128, each=16*1024*1024, user_headers: dict={'User-Agent': 'Mozilla/5.0'}):
    fs = size(url, user_headers)
    f = open(file, "wb")
    @retry(tries=retry_times)
    @multitasking.task
    def download_a_part(start, end, achunk):
        part_headers = user_headers.copy()
        part_headers['Range'] = f'bytes={start}-{end}'
        res = sess.get(url, headers=part_headers, stream=True)
        chunks = []
        for chunk in res.iter_content(chunk_size=achunk):
            chunks.append(chunk)
            bar.update(achunk)
        f.seek(start)
        for chunk in chunks:
            f.write(chunk)
        del chunks
    each_final = min(fs, each)
    parts = split(fs, each_final)
    print(f"Parts: {len(parts)}")
    bar = tqdm.tqdm(total=fs, desc=f"{file}")
    sess = requests.Session()
    for apart in parts:
        start, end = apart
        download_a_part(start, end, chunks)
    multitasking.wait_for_tasks()
    bar.close()
    f.close()
