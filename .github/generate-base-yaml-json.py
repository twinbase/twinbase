import os
import yaml
import json

curdir = os.getcwd()

d = {}

repo = os.environ["GITHUB_REPOSITORY"] # for local dev, set in bash: export GITHUB_REPOSITORY=dev-user/twinbase-dev

owner = repo.split('/')[0]
print('Owner: ' + owner)

repo_plain = repo.split('/')[1]
print('Repo_plain: ' + repo_plain)

try:
    with open('CNAME') as f:
        lines = f.readlines()
    baseurl = 'https://' + lines[0]
    d['baseurl'] = baseurl
except:
    d['baseurl'] = 'https://' + owner + '.github.io/' + repo_plain

d['repo_url'] = 'https://github.com/' + repo

d['new_twin_url'] = "https://github.com/" + repo + "/new/main?filename=docs/edit_this_with_backspace/index.yaml&value=Paste%20a%20DT%20document%20template%20here"

print('Adding twins from folders:')
d['twins'] = []
i = 0
for folder in os.listdir(curdir):
    if os.path.isdir(folder) and folder != 'static' and folder != 'new-twin':
        print('- ' + folder)
        
        with open(folder + '/index.json', 'r') as docfile:
            dtdoc = json.load(docfile)
        d['twins'].append({})
        d['twins'][i]['url'] = baseurl + '/' + folder
        d['twins'][i]['name'] = dtdoc['name']
        i += 1

with open ('index.yaml', 'w') as yamlfile:
    yaml.dump(d, yamlfile)

with open ('index.json', 'w') as jsonfile:
    json.dump(d, jsonfile)
