# -*- coding: utf-8 -*-
from urllib import request


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"}
response = request.urlopen(request.Request("http://www.sina.com.cn",headers=headers))
print(response.read().decode("utf-8"))
