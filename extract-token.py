REGION = 'us-central1'
PROJECT_ID = 'jinzi95-seattle'
RECEIVING_FUNCTION = 'my-cloud-function'
function_url = "https://hello-ve5nrmgj5a-uc.a.run.app"

from google.oauth2.id_token import fetch_id_token
from google.auth.transport import requests
r = requests.Request()
print(fetch_id_token(r,"https://www.googleapis.com/auth/cloud-platform"))

import google.auth
credentials, project_id = google.auth.default(scopes='https://www.googleapis.com/auth/cloud-platform')

credentials.token = "xxxeyJhbGciOiJSUzI1NiIsImtpZCI6Ijg1ODI4YzU5Mjg0YTY5YjU0YjI3NDgzZTQ4N2MzYmQ0NmNkMmEyYjMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJodHRwczovL2hlbGxvLXZlNW5ybWdqNWEtdWMuYS5ydW4uYXBwLyIsImF6cCI6IjExMTExNjAyNDAxODkzMjc5MjMwMiIsImV4cCI6MTYzNTk1ODY4OCwiaWF0IjoxNjM1OTU1MDg4LCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJzdWIiOiIxMTExMTYwMjQwMTg5MzI3OTIzMDIifQ.FGm9BMYFQz79DZ5u0RJAtY5Nw6iHCosgoBnnZlx4AuTUZ_dlIYzUsvl70GawauQmKE0lAjfuzSDPRZb1RtjCpvn-InrPm_nXtH_XXEwAxBa1DJSxnCRr2vf_PAUcmQkzgEZfKquJYBct0sIQAMs1i7ctG82VeYzF_5DC46j4PZA79u2SVKi7sw64aJoYfrxdwLYVRnAWQVoGaoxrjDYNf2NXq27nFMHtvJiUg2BbicxIDEaZ_8USNbmbN5pnmckuW7pwiWdHAjGeMwQW5LtyVtovUaFVyteSIpKtH9_fMbjqu65VAbDzXfiWpm4Hd7Ix0C61K2xy_-__Z7fehBhvyg"
credentials.id_token("")

# To use the Cloud Build service account email
service_account_email = "mcs-service@jinzi95-seattle.iam.gserviceaccount.com"
#service_account_email = "YOUR OWN SERVICE ACCOUNT"

metadata_server_url = f'https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/{service_account_email}:generateIdToken'
token_headers = {'content-type': 'application/json'}

from google.auth.transport.requests import AuthorizedSession
authed_session = AuthorizedSession(credentials)
import json
body = json.dumps({'audience': function_url})

token_response = authed_session.request('POST',metadata_server_url, data=body, headers=token_headers)
jwt = token_response.json()
print("jwt",jwt)
#print(jwt['token'])