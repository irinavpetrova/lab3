# coding: utf8
class BaseClient:

    BASE_URL = "https://api.vk.com/method/"
    method = None


    def generate_url(self):
        return '{0}{1}'.format(self.BASE_URL, self.method)

    def _get_data(self):
         response = None
         return response
