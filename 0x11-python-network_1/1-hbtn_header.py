#!/usr/bin/python3
"""script that  display id ,fetches url given"""

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id', None)
        print(request_id)
