import os, yaml, json, requests

# Get current working directory
curdir = os.getcwd()

# Initialize dictionary
d = {}

# Fetch GitHub repository info
repo = os.environ["GITHUB_REPOSITORY"] # for local dev, set in bash: export GITHUB_REPOSITORY=dev-user/twinbase-dev
github_owner = repo.split('/')[0]
repo_plain = repo.split('/')[1]

# Detect base URL
try:
    with open('CNAME') as f:
        lines = f.readlines()
    baseurl = 'https://' + lines[0]
    d['baseurl'] = baseurl
except FileNotFoundError:
    try: 
        url = 'https://raw.githubusercontent.com/' + github_owner + '/' + github_owner + '.github.io/master/CNAME'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        baseurl = 'https://' + r.text + '/' + repo_plain
        d['baseurl'] = baseurl
    except:
        baseurl = 'https://' + github_owner + '.github.io/' + repo_plain
        d['baseurl'] = baseurl

# Fetch owner info from setup.yaml file in repo root and add to dict
with open('../setup.yaml', 'r') as yamlfile:
    setup = yaml.load(yamlfile, Loader=yaml.FullLoader)
d.update(setup)
# Print owner DTID, this is also a test to make sure it exists
print('Owner DTID: ' + setup['owner']['dt-id'])

# Add repo specific URLs
d['repo_url'] = 'https://github.com/' + repo
d['new_twin_url'] = "https://github.com/" + repo \
    + "/new/main?filename=docs/edit_this_with_backspace/index.yaml&value=Paste%20a%20DT%20document%20template%20here"

# Add twins from twin folders
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

# Write YAML file
with open ('index.yaml', 'w') as yamlfile:
    yaml.dump(d, yamlfile, default_flow_style=False, sort_keys=False, allow_unicode=True)

# Write JSON file
with open ('index.json', 'w') as jsonfile:
    json.dump(d, jsonfile)
