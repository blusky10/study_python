import requests
import os
os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["PYTHONHTTPSVERIFY"] = "0"

url='https://api.github.com/search/repositories?q=language:python&amp;sort=stars'

headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url, headers=headers, verify=False)
print(f"Status code: {r.status_code}")

response_dict=r.json()

print(response_dict.keys())

print(f"Total repos : {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"repos returned : {len(repo_dicts)}")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")