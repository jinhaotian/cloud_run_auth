REGION = 'us-central1'
PROJECT_ID = 'jinzi95-seattle'
RECEIVING_FUNCTION = 'my-cloud-function'
function_url = "https://hello-ve5nrmgj5a-uc.a.run.app"

#Not working, metaserver report 404
# from google.oauth2.id_token import fetch_id_token
# from google.auth.transport import requests
# r = requests.Request()
# print(fetch_id_token(r,"https://www.googleapis.com/auth/cloud-platform"))

import google.auth
from google.auth.transport.requests import AuthorizedSession
import json
audience = '"https://hello-ve5nrmgj5a-uc.a.run.app"'

credentials, project_id = google.auth.default(
            scopes='https://www.googleapis.com/auth/cloud-platform')

# #2 To use the current service account email
#service_account_email = credentials.service_account_email
#not working  with use account
service_account_email = "mcs-service@jinzi95-seattle.iam.gserviceaccount.com"

from pprint import pprint
pprint(vars(credentials))

sa_credentials_url =  f'https://iamcredentials.googleapis.com/' \
                      f'v1/projects/-/serviceAccounts/'  \
                      f'{service_account_email}:generateIdToken'

headers = {'content-type': 'application/json'}

authed_session = AuthorizedSession(credentials)
body = json.dumps({'audience': audience})
body = json.dumps({'audience': audience})
token_response = authed_session.request('POST',sa_credentials_url,
                                        data=body, headers=headers)

jwt = token_response.json()
id_token = jwt['token']
print(id_token)
# from google.auth.transport.requests import AuthorizedSession
# authed_session = AuthorizedSession(credentials)
# import json
# body = json.dumps({'audience': function_url})

# token_response = authed_session.request('POST',metadata_server_url, data=body, headers=token_headers)
# jwt = token_response.json()
# print("jwt",jwt)
# #print(jwt['token'])