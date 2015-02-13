__author__ = 'crow'

from os import listdir
from os.path import isfile, join
import os.path, time
from datetime import datetime ,timedelta

def main():

    past = int(time.time())

    mypath = '/Users/utmcrow/Dropbox/images/'
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    for file in onlyfiles:
        print "last modified: %s" % time.ctime(os.path.getmtime(mypath+file))
        print "created: %s" % time.ctime(os.path.getctime(mypath+file))
        print "diff: %s" % timedelta(seconds=past-os.path.getmtime(mypath+file))

        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(mypath+file)
        print "last modified: %s" % time.ctime(mtime)
    pass

if __name__ == "__main__":
    main()

