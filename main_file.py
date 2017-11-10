# coding: utf8
from getID import *
from getFriends import *
from Gist import *

ClientID = input("Введите ID: \n")
user = GetUserID(ClientID)
user_id = user.get_data()

friend = Friends(user_id)
friend_list = friend.make_list()
ages = count_bdate(friend_list)
print(friend_list)
fr_gist = gist(ages)

