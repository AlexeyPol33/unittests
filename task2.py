import requests

TOKEN = ''


class ya_disk():
    URL = 'https://cloud-api.yandex.net'
    def __init__(self,token) -> None:
        self.token = token
        pass

    def get_info(self):
        response = requests.get(self.URL + '/v1/disk', headers={'Authorization': f'OAuth {self.token}'})
        return response

    def create_folder(self,name):
        headers={'Authorization': f'OAuth {self.token}'}
        params = {'path': name}
        response = requests.put(self.URL + '/v1/disk/resources', headers=headers,params=params)
        return response

    def del_folder(self,name):
        headers={'Authorization': f'OAuth {self.token}'}
        params = {'path': name}
        response = requests.delete(self.URL + '/v1/disk/resources', headers=headers,params=params)
        return response
    
if __name__ == '__main__':
    a = ya_disk(TOKEN)
    print(a.get_info().status_code)
    print(a.create_folder('Test333'))
    print(a.del_folder('Test333'))