
#storage.py



#from filestorage import FileStorage
#from memorystorage import MamoryStorage
a = [ 1, 2, 3, 4 ]
b = [ "a", "b", "c", "d" ]

class StorageProxy:
    pass
#  def __init__(self,storageType = "memory"):
#    if storageType == "memory":
#      self.realStorage = a
#    elif storageType == "file":
#      self.realStorage = b
      
  
    def __getattr__(self,name):
        if name == "load":
            return f"Hi, Veronica!!! You try to get attr load!"
        if name == "save":
            return f"Hi, Veronica!!! You try to get attr save!"
