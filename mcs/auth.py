import google.auth
import requests
from google.auth.transport.requests import AuthorizedSession
import json
from pprint import pprint


default_service_account_email = "project-service-account@platform-dev-base-bd49.iam.gserviceaccount.com"
sa_credentials_url = 'https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/{}:generateIdToken'

def get_credential():
    creds, project = google.auth.default()
    auth_req = google.auth.transport.requests.Request()
    creds.refresh(auth_req)
    auth_req.session.close()
    return creds

def get_id_token(credential,audience):
    service_account_email = "project-service-account@platform-dev-base-bd49.iam.gserviceaccount.com"
    if  (hasattr(credential, "service_account_email")):
        service_account_email = creds.service_account_email
    url =  sa_credentials_url.format(service_account_email)
    headers = {'content-type': 'application/json', 'Authurization': f'Bearer {credential.token}'}
    authed_session = AuthorizedSession(credential)
    body = json.dumps({'audience': audience})
    token_response = authed_session.request('POST',url, data=body, headers=headers)
    jwt = token_response.json()
    id_token = jwt['token']
    authed_session.close()
    token_response.close()
    return id_token

if __name__ == '__main__':
    audience = "https://mcs-load-4sdci277xa-uw.a.run.app/"
    creds = get_credential()
    id_token = get_id_token(creds, audience)
    print(id_token);
    
  



# audience = '"https://hello-ve5nrmgj5a-uc.a.run.app"'

# credentials, project_id = google.auth.default(
#             scopes='https://www.googleapis.com/auth/cloud-platform')

# service_account_email = "mcs-service@jinzi95-seattle.iam.gserviceaccount.com"


# sa_credentials_url =  f'https://iamcredentials.googleapis.com/' \
#                       f'v1/projects/-/serviceAccounts/'  \
#                       f'{service_account_email}:generateIdToken'

# headers = {'content-type': 'application/json', 'Authurization': f'Bearer {creds.token}'}

# authed_session = AuthorizedSession(credentials)
# body = json.dumps({'audience': audience})

# token_response = authed_session.request('POST',sa_credentials_url,
#                                         data=body, headers=headers)

# jwt = token_response.json()

# from pprint import pprint
# print("jwt", jwt)
# id_token = jwt['token']
# print("id_token", id_token)
