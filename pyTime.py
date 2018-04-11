#"""
import os
import os.path, time

print("last modified: %s" % time.ctime(os.path.getmtime("test.html")))
print("created: %s" % time.ctime(os.path.getctime("test.html")))

statinfo = int((os.stat('test.html').st_mtime))
print statinfo

fn = 'ttt.txt'

os.utime(fn, (time.time(), statinfo))

print("last modified: %s" % time.ctime(os.path.getmtime(fn)))
print("created: %s" % time.ctime(os.path.getctime(fn)))

mypath = "./"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print onlyfiles



"""
import time
import os
t = time.mktime(time.strptime('09.04.2016 17:00:00', '%d.%m.%Y %H:%M:%S'))
print t
fn = 'ttt.txt'

os.utime(fn, (t,t)) # <---

print("last modified: %s" % time.ctime(os.path.getmtime(fn)))
print("created: %s" % time.ctime(os.path.getctime(fn)))
"""