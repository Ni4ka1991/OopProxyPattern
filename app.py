#!/usr/bin/env python3

from storage import StorageProxy

a = [ "1", "2", "3", "4" ]

storage = StorageProxy( "json" )   # in memory
#storage = StorageProxy("file")       # in file


storage.save( "bu-bu-bu" )
print(storage.load())
