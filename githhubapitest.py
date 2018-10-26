#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:31:44 2018

@author: manusv
"""

import requests

r = requests.get('https://api.github.com/user', auth=('manusv', 'jayadev!4'))

print r.status_code
print r.headers['content-type']
r = requests.get('https://developer.github.com/v3/activity/events/')
print r.status_code
