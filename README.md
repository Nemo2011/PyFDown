# PyFDown: Fast Downloading in Python. 

PyFDown is a python library. This library can downloading file fast. 

# Install

``` powershell
    python -m pip install PyFDown
```

# Usage

``` python
    from PyFDown import downloader
    URL = "Link to your file"
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
    }
    download(URL, "test", user_headers=HEADERS)
```

# Info

Max parts: 128
Default one part: 1MB
