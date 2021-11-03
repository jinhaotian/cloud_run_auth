REGION = 'us-central1'
PROJECT_ID = 'jinzi95-seattle'
RECEIVING_FUNCTION = 'my-cloud-function'
function_url = "https://hello-ve5nrmgj5a-uc.a.run.app"

import google.auth
credentials, project_id = google.auth.default(scopes='https://www.googleapis.com/auth/cloud-platform')

# To use the Cloud Build service account email
service_account_email = credentials.service_account_email
#service_account_email = "YOUR OWN SERVICE ACCOUNT"

metadata_server_url = f'https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/{service_account_email}:generateIdToken'
token_headers = {'content-type': 'application/json'}

from google.auth.transport.requests import AuthorizedSession
authed_session = AuthorizedSession(credentials)
import json
body = json.dumps({'audience': function_url})

token_response = authed_session.request('POST',metadata_server_url, data=body, headers=token_headers)
jwt = token_response.json()
print(jwt['token'])