#!/usr/bin/python3
"""POST an email"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))   
