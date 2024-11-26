import requests
import json

# 替换为你的 GitHub 用户名
username = 'your-github-username'

# 获取用户所有仓库的语言信息
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)
repos = response.json()

languages = {}

for repo in repos:
    repo_name = repo['name']
    repo_url = f'https://api.github.com/repos/{username}/{repo_name}/languages'
    repo_languages = requests.get(repo_url).json()
    for lang, lines in repo_languages.items():
        if lang in languages:
            languages[lang] += lines
        else:
            languages[lang] = lines

# 将语言信息写入文件
with open('languages.json', 'w') as f:
    json.dump(languages, f, indent=4)