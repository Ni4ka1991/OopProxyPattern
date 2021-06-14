#!/usr/bin/env python3

from storage import StorageProxy



storage = StorageProxy()   # in memory
print(storage.load)
print(storage.save)
#print(storage.load())

#storage = StorageProxy("file")   # in file
#storage.save("Test Data")
#print(storage.load())
