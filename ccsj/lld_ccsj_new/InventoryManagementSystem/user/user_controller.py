from typing import List

from user import User

class UserController:
    def __init__(self, user_list: List[User]):
        self.user_list: List[User] = user_list
    
    def add_user(self, user: User) -> None:
        self.user_list.append(user)
    
    def remove_user(self, user: User) -> None:
        self.user_list.remove(user)
    
    # get particular user by user id
    def get_user_by_id(self, user_id: int) -> User:
        for user in self.user_list:
            if user.uid == user_id:
                return user
