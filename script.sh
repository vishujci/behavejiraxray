in loop

token=$(curl -H "Content-Type: application/json" -X POST --data @"jiraauth.json" https://xray.cloud.xpand-it.com/api/v2/authenticate| tr -d '"')

curl --location --request GET "https://xray.cloud.xpand-it.com/api/v2/export/cucumber?keys=DEM-1;DEM-2" --header "Content-Type: application/json" --header "Authorization: Bearer $token" -o features.zip

(unzip features.zip -d features)







# feature file will run in windows
behave --format=cucumber_json:PrettyCucumberJSONFormatter -o results/cucumber.json  --format=json -o results/behave.json \features

export result to cucumber

curl -H "Content-Type: application/json" -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnQiOiI4MThjNzI5Zi0yYzdhLTM1YzMtOTM5MS1hZDhhMzQ3YjE5NGUiLCJhY2NvdW50SWQiOiI1YzY0MGFlOGYzMDcxZDU3MDYyMzhjYTgiLCJpc1hlYSI6ZmFsc2UsImlhdCI6MTYzMDMwNDcwMywiZXhwIjoxNjMwMzkxMTAzLCJhdWQiOiI4NTg5QTAxRTIxRjY0RjlEOTY3NzJFRjMyN0FGNjBFMiIsImlzcyI6ImNvbS54cGFuZGl0LnBsdWdpbnMueHJheSIsInN1YiI6Ijg1ODlBMDFFMjFGNjRGOUQ5Njc3MkVGMzI3QUY2MEUyIn0.nPs5eCt7ILo_lDuRHiU3cJ2yDG4CXIX96jdQ0wQUGsw"  --data @"results/cucumber.json" "https://xray.cloud.xpand-it.com/api/v1/import/execution/cucumber"


