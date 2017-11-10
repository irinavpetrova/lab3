# coding: utf8
from BaseClient import BaseClient
import requests


class Friends(BaseClient):
    def __init__(self, vk_id):
        self.vk_id = vk_id
    method = "friends.get"
    http_method = "?uid="
    fields = "&fields=bdate"



    def generate_url(self):
        return '{0}{1}{2}{3}'.format(BaseClient.generate_url(self), self.http_method, self.vk_id, self.fields)

    def get_data(self):
        try:
            response = requests.get(self.generate_url()).json()
            return response["response"]
        except Exception:
            print ('Такого ID не существует')
            exit()


    def make_list(self):
        t_list = []
        for i in self.get_data():
            try:
                if len(i["bdate"]) >= 8:
                    t_list.append(i["bdate"])
            except Exception:
                continue
        return t_list
