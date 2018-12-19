import requests
headers = {'API-OPR':'API-KEY-HERE'}
domain = 'google.com'
url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
request = requests.get(url, headers=headers)
result = request.json()
print(result)
