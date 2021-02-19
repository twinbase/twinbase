import os, yaml, json, requests

curdir = os.getcwd()

repofull = os.environ["GITHUB_REPOSITORY"]
user = repofull.split('/')[0]
repo = repofull.split('/')[1]

try:
    with open('CNAME') as f:
        lines = f.readlines()
    baseurl = 'https://' + lines[0]
except FileNotFoundError:
    try: 
        url = 'https://raw.githubusercontent.com/' + user + '/' + user + '.github.io/master/CNAME'
        r = requests.get(url, allow_redirects=True)
        r.raise_for_status()
        baseurl = 'https://' + r.text + '/' + repo
    except:
        baseurl = 'https://' + user + '.github.io/' + repo

for folder in os.listdir(curdir):
    if os.path.isdir(folder) and folder != 'static' and folder != 'new-twin':
        print('Modifying YAML in folder: ' + folder)
        
        with open(folder + '/index.yaml', 'r') as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        data['baseurl'] = baseurl

        if data['dt-id'].split('|')[0] == 'autoassign':
            data['dt-id'] = os.path.join(data['dt-id'].split('|')[1], folder)

        if not (data['hosting-iri'] == os.path.join(baseurl, folder)):
            data['hosting-iri'] = os.path.join(baseurl, folder)
            print('::warning file=' + folder + '/index.yaml::Hosting IRI changed for DT-ID: ' \
            + data['dt-id'] + ' . Hosting IRI is now ' + data['hosting-iri'] \
            + ' . Please update the DT-ID registry if needed.')

        editurl = 'https://github.com/' + repofull + '/edit/main/docs/' + folder + '/index.yaml'
        data['edit'] = editurl

        with open(folder + '/index.yaml', 'w') as filew:
            yaml.dump(data, filew, default_flow_style=False, sort_keys=False, allow_unicode=True)
