storage = StorageProxy()   # in memory
storage.save("Test Data")
print(storage.load())

storage = StorageProxy("file")   # in file
storage.save("Test Data")
print(storage.load())
