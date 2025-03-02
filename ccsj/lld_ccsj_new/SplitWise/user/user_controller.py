from typing import List
from user import User

class UserController:
    def __init__(self):
        self.user_list: List[User] = []
    
    def add_user(self, user: User):
        self.user_list.append(user)
    
    def get_user_by_uid(self, uid: str):
        for user in self.user_list:
            if user.get_uid() == uid:
                return user
    
    def get_all_user(self):
        return self.user_list
