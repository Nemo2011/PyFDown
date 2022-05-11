# PyFDown: Fast Downloading in Python. 

PyFDown is a python library. This library can downloading file fast. 

# Install

``` powershell
    python -m pip install PyFDown
```

# Why use PyFDown
- The fast speed pure python. 
- Easy to use. 
- No any limit to download. The choice is on the user. 

# Compare

| Name | Language | License |
| ---- | -------- | ------- |
| Aria2 | C/C++ | GPLv2 |
| PyFDown | Python | LGPLv3 |

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

Default Max parts: 128
Default one part: 1MB

# Test speed

One episode of MythBusters: `1m30s`<br>
The ISO Image for Windows7: `21m19s`<br>

Max parts: `128` | One part: `1MB`
