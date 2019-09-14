# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:38:10 2019

@author: ionekr
"""
# Tomado de https://linuxhint.com/google_search_api_python/

from __future__ import print_function
import os.path

from googleapiclient.discovery import build
my_api_key = "TU_LLAVE"
my_cse_id = "TU_ID"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

if __name__ == '__main__':
    r = google_search("TU_BUSQUEDA", my_api_key, my_cse_id)
    print(r)
    
