import requests
import json

def get_jira_authentication_token():
    try:
        body = { "client_id" : "8589A01E21F64F9D96772EF327AF60E2" , "client_secret" : "14a2dcfb46e97cb14e93be613eae25448b02555499d370685ea225ba2d0ff9de"}
        response  =  requests.post("https://xray.cloud.xpand-it.com/api/v2/authenticate", headers={"Content-Type":"application/json"}, data=json.dumps(body))
    except Exception as e:
        raise e

    return response.text.replace('"','')





def import_testcases_to_jira(bearer_token:str):
    f = open("results/cucumber.json", 'r')
    response = requests.post("https://xray.cloud.xpand-it.com/api/v1/import/execution/cucumber",
                             headers={'Content-Type': 'application/json',
                                      'Authorization': 'Bearer ' + bearer_token},
                             data=json.dumps(json.loads(f.read())))
    print(response.reason)


if __name__== "__main__":
    import_testcases_to_jira(get_jira_authentication_token())