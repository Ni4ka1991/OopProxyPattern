
#jsonstorage

import json

class JsonStorage:
    
    def __init__( self ):
        self.name = "data.json"
   
    def save( self, data ):
        with open( "data.json", "w" ) as write_file:
            json.dump( data, write_file, ensure_ascii = False, indent = 4 )


    def load( self ):
        file = open( self.name, "r" )
        data = json.loads( file.read() )
        file.close()
        return data
