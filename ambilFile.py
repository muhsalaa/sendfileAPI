# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:54:01 2018

@author: emotment
"""
import requests
'''
## INI UNTUK KIRIM FILE ##
r = requests.post('http://127.0.0.1:5000/todo/lone/', 
                  files={'file': open('aaa.pdf', 'rb')})
'''
## INI UNTUK AMBIL FILE ##
url='https://kirimincoba.herokuapp.com/uploads/aass.pdf/12345'
res = requests.get(url,stream=True)
fo = open('gagaso.pdf','wb')
for chunk in res.iter_content(chunk_size=8*1024):
    if chunk:
        fo.write(chunk)