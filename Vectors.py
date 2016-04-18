import copy

#class for User Vector
class UserVector:
    #constructor
    def __init__(self,userID):
        self.userID = userID
        self.vector = dict()
        
    #add a rating    
    def add_rating(self,itemID,rating):
        self.vector[itemID] = rating
        
    #remove rating    
    def remove_rating(self,itemID):
        del self.vector[itemID]
        
    def getVector(self):
        temp = copy.deepcopy(self.vector)
        return temp
    
#class for Item Vector    
class ItemVector:
    #constructor
    def __init__(self,itemID):
        self.itemID = itemID
        self.vector = dict()
        
    #add a rating    
    def add_rating(self,userID,rating):
        self.vector[userID] = rating
        
    #remove rating    
    def remove_rating(self,userID):
        del self.vector[userID]
        
    def getVector(self):
        temp = copy.deepcopy(self.vector)
        return temp