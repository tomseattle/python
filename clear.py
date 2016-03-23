#!/usr/bin/python
#
#
from path import path
d=path('/home/tdao/cron')
del_size=1000000
for i in d.walk():
   if i.isfile():
	if i.size > del_size:
	   open(i.name,'w').close()
