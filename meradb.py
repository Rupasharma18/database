import json
import os
from random import randrange

def load(bool=False, fileName='' ):
    meradb = meraDB(bool, fileName)
    meradb.load_file()
    return meradb

# def Dmerage(self,bool=False, fileName=''  ):    
#     dmerge = meraDB(fileName, bool)
#     dmerge.load_file()
#     return dmerge
class meraDB():
    fileName = ""
    jObject = {}
    bool=False
    
    def __init__(self,fileName,bool):
        self.fileName = fileName
        self.bool = bool

    def load_file(self):
        if os.path.exists(self.fileName):
            print ("Loading Database from ", self.fileName, " !")
            content = open(self.fileName).read()
            self.jObject = json.loads(content)
            print ("DB loaded successfully!")
        else:
            self.dump()  
            print ("done")
        return self.jObject

    def dump(self):
        print ( "Dumping database to ", self.fileName, " !")
        open(self.fileName, 'w').write(json.dumps(self.jObject))
        print ( "DB dumped successfully!")
        return "OK"
        
    def set(self, key, value):
        print ("set the value")
        self.jObject[key] = value
        if bool:
            self.dump()
        # print (self.jObject)
        return True
    def get(self,key):
        print ("get successfully")
        print (self.jObject[key]) 
        if key in self.jObject:
            print ("got it")
            return True
        
        else:
            print ("key is not in db")    
            return False
        return True
    def get_all(self):
        all_key = self.jObject.keys()
        print (all_key)
        if bool:
            self.dump()

        return True
    def rem(self,key):
        print ("key is delete ")
        del self.jObject[key] 
        if bool:
            self.dump()
        return True
    def exist_key(self, key):
        if key in self.jObject :
            print ("got")
            return True
        else:
            print ("error")
            return False
        if bool:
            self.dump()    

    def total_keys(self):
        count = 0
        for self.i in self.jObject.keys():
            count= count +1
        print (count) 
        if bool :
            self.dump()
        return count 
       

    def del_db(self):
        del self.jObject
        # print (self.jObject)
        print ("delete")
        if bool:
            self.dump()
        return True

    def random_insert(self,  value):
        for i in range(0,10):
            self.jObject['key'+str(i)] = randrange(value)
            # print (self.jObject)
        if bool:
            self.dump()   
        return self.jObject

    # def Dmerage(self,bool=False, fileName=''  ):    
    #     dmerge = meraDB(fileName, bool)
    #     dmerge.load_file()
    #     return dmerge



