# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:54:01 2018

@author: emotment
"""

import requests
'''
## INI UNTUK KIRIM FILE ##
r = requests.post('http://127.0.0.1:5000/todo/lone/', 
                  files={'file': open('gagaso.pdf', 'rb')})
'''
## INI UNTUK AMBIL FILE ##
url='http://127.0.0.1:5000/uploads/gagaso.pdf/12345'
res = requests.get(url)
p = res.content
fo = open('gagas.pdf','wb')
fo.write(p)
fo.close()
