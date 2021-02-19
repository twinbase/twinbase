import os, yaml, json

curdir = os.getcwd()

with open('CNAME') as f:
    lines = f.readlines()
baseurl = 'https://' + lines[0]

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

        repo = os.environ["GITHUB_REPOSITORY"]
        editurl = 'https://github.com/' + repo + '/edit/main/docs/' + folder + '/index.yaml'
        print(editurl)
        data['edit'] = editurl

        with open(folder + '/index.yaml', 'w') as filew:
            yaml.dump(data, filew, default_flow_style=False, sort_keys=False, allow_unicode=True)
