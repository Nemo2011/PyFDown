# PyFDown: Fast Downloading in Python. 

PyFDown is a python library. This library can downloading file fast. 

# Install

``` powershell
    python -m pip install PyFDown
```

# Usage

``` python
    from PyFDown import download
    URL = "Link to your file"
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.bilibili.com/"
    }
    download(URL, "test", user_headers=HEADERS)
```