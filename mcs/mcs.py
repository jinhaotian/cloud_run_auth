import requests
import auth

class MediaCollectionService:
  
  __favorite_resources = "/mcs/me/v1/{}"
  def __init__(self, server_url):
    self.server_url = server_url
    creds = auth.get_credential()
    id_token = auth.get_id_token(creds, server_url)
    self.token = id_token
  
  def get_favorites(self, guid, content_type):
    headers = {'Authorization': f'Bearer {self.token}', 
                'x-napster-user':guid}
    response = requests.get( self.server_url + 
        MediaCollectionService.__favorite_resources.format(content_type), headers=headers)
    resp = response.json()
    response.close()
    return resp
  
  def add_favorites(self, guid, content_type, content_id):
    headers = {'Authorization': f'Bearer {self.token}', 
                'x-napster-user':guid}
    params = {"id":content_id}
    response = requests.put( self.server_url + 
        MediaCollectionService.__favorite_resources.format(content_type), headers=headers,
        params=params)
    status = response.status_code
    return status
  
  def remove_favorites(self, guid, content_type, content_id):
    headers = {'Authorization': f'Bearer {self.token}', 
                'x-napster-user':guid}
    params = {"id":content_id}
    response = requests.delete( self.server_url + 
        MediaCollectionService.__favorite_resources.format(content_type), headers=headers,
        params=params)
    status = response.status_code
    return status
  
  def contains(self, guid, content_type, content_id):
    headers = {'Authorization': f'Bearer {self.token}', 
                'x-napster-user':guid}
    params = {"ids":content_id}
    response = requests.get( self.server_url + 
        MediaCollectionService.__favorite_resources.format(content_type) +  "/contains", headers=headers,
        params=params)
    resp = response.json()
    response.close()
    return resp
  def count(self, guid, content_type):
    headers = {'Authorization': f'Bearer {self.token}', 
                'x-napster-user':guid}
    response = requests.get( self.server_url + 
        MediaCollectionService.__favorite_resources.format(content_type) +  "/count", headers=headers)
    resp = response.json()
    response.close()
    return resp
if __name__ == '__main__':
    mcs = MediaCollectionService("https://mcs-load-4sdci277xa-uw.a.run.app")
    resp = mcs.get_favorites("8C54EEA3387AD457E050960A5503661F","videos")
    print(resp)
    