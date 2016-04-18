from Vectors import UserVector
from Vectors import ItemVector
import Rec_Math


class Rec_System:
    #cons
    def __init__(self):
        self.users = dict()
        self.items = dict()
        
    def add_user(self,userID):
        current_user = UserVector(userID)
        self.users[userID] = current_user
        
    def add_item(self,ItemID):
        current_item = ItemVector(ItemID)
        self.items[ItemID] = current_item