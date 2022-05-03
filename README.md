# PyFDown: Fast Downloading in Python. 

PyFDown is a python library. This library can downloading file fast. 

# Install

``` powershell
    python -m pip install PyFDown
```

# Usage

``` python
    from PyFDown import download
    URL = """https://upos-sz-mirrorhwo1.bilivideo.com/upgcxcode/37/00/268620037/268620037_nb2-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1651579328&gen=playurlv2&os=hwo1bv&oi=2569207702&trid=33c4007b9be1492589c034d7d70a32a1u&platform=pc&upsig=efc00ddc776658e2a549ebabbbf3e7f8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&bw=166278&logo=80000000"""
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com/"
    }
    download(url, "test.mp4", headers=HEADERS)
```