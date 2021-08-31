import json
import requests
import zipfile
import configparser
import rootpath
import sys


def getconfig():
    # try:
    print(sys.argv)
    config = configparser.ConfigParser()
    config.read(rootpath.detect() + "\\" + sys.argv[1])
    # except Exception as e:
    # raise e
    return config


def get_jira_authentication_token():
    try:
        body = {"client_id": "8589A01E21F64F9D96772EF327AF60E2",
                "client_secret": "14a2dcfb46e97cb14e93be613eae25448b02555499d370685ea225ba2d0ff9de"}
        response = requests.post("https://xray.cloud.xpand-it.com/api/v2/authenticate",
                                 headers={"Content-Type": "application/json"}, data=json.dumps(body))
    except Exception as e:
        raise e

    return response.text.replace('"', '')


def get_features_files_from_jira(bearer_token: str, ticketkeys: str):
    try:
        response = requests.get('https://xray.cloud.xpand-it.com/api/v2/export/cucumber?keys=' + ticketkeys,
                                headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + bearer_token})
        print(response.text)
        print("printing something")
        with open("chkfeatures.zip", "wb") as code:
            code.write(response.content)
        with zipfile.ZipFile("chkfeatures.zip", "r") as zip_ref:
            zip_ref.extractall("features")
    except Exception as e:
        raise e


if __name__ == "__main__":
    config = getconfig()
    sectionsConfig = config.sections()
    sectionsLength = len(sectionsConfig)
    print("hello yellow")
    for x in range(sectionsLength):
        token = get_jira_authentication_token()
        get_features_files_from_jira(token, config.get(sectionsConfig[x], 'tickets'))
