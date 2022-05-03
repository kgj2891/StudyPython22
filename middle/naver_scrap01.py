# 네이버 웹페이지 긁어오기
from tracemalloc import reset_peak
from urllib import request
from urllib.request import Request, urlopen

req = Request('https://www.naver.com/')
res = urlopen(req)
print(res)