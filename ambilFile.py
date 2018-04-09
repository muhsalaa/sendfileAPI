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
r = requests.get('http://127.0.0.1:5000/uploads/asertipm.pdf/12345')
s = r.content
fo = open('gaga.pdf','wb')
fo.write(s)
fo.close()