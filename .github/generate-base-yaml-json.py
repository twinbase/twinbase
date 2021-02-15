import os
import yaml
import json

curdir = os.getcwd()

d = {}

with open('CNAME') as f:
    lines = f.readlines()
baseurl = 'https://' + lines[0]
d['baseurl'] = baseurl

print('Adding twins from folders:')
d['twins'] = []
i = 0
for folder in os.listdir(curdir):
    if os.path.isdir(folder) and folder != 'static':
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
