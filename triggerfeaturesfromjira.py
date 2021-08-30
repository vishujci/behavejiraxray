import json
import requests
import zipfile

def get_jira_authentication_token():
    body = { "client_id" : "8589A01E21F64F9D96772EF327AF60E2" , "client_secret" : "14a2dcfb46e97cb14e93be613eae25448b02555499d370685ea225ba2d0ff9de"}
    response  =  requests.post("https://xray.cloud.xpand-it.com/api/v2/authenticate", headers={"Content-Type":"application/json"}, data=json.dumps(body))
    return response.text.replace('"','')



def get_features_files_from_jira(bearer_token: str):
    response = requests.get('https://xray.cloud.xpand-it.com/api/v2/export/cucumber?keys=DEM-1;DEM-2',headers={'Content-Type':'application/json','Authorization': 'Bearer ' + bearer_token})
    print(response)
    with open("chkfeatures.zip","wb") as code:
        code.write(response.content)
    with zipfile.ZipFile("chkfeatures.zip", "r") as zip_ref:
        zip_ref.extractall("features")


if __name__ == "__main__":
    token = get_jira_authentication_token()
    get_features_files_from_jira(token)



