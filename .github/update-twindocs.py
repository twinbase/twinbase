import os, yaml, json, requests, dtweb

curdir = os.getcwd()

repofull = os.environ["GITHUB_REPOSITORY"]
user = repofull.split('/')[0]
repo = repofull.split('/')[1]

# Detect hosting URL
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

# Copy modified jsons to yamls
print('Copy jsons to yamls')
with open("modified-jsons.txt", "r") as a_file:
  for line in a_file:
    file = line.strip()
    print(file)
    try:
        with open(file, 'r') as jsonfiler:
            data = json.load(jsonfiler)
            # print(data)
        # Save DT doc contents in YAML file
        yamlfile = file[:-10] + 'index.yaml'
        with open(yamlfile, 'w') as filew:
            yaml.dump(data, filew, default_flow_style=False, sort_keys=False, allow_unicode=True)
        # Add modified yaml to list
        with open('modified-yamls.txt', 'a') as file_yaml_list:
            file_yaml_list.write(yamlfile + '\n')
    except FileNotFoundError:
        print('Did not find JSON file, moving to next one')

# Process yamls
print('Process yamls')
with open("modified-yamls.txt", "r") as a_file:
  for line in a_file:
    file = line.strip()
    print(file)
    try:
        with open(file, 'r') as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        data['baseurl'] = baseurl

        folder = file.split('/')[1]
        # Autoassign DT-ID if requested in YAML file
        if data['dt-id'].split('|')[0] == 'autoassign':
            data['dt-id'] = os.path.join(data['dt-id'].split('|')[1], folder)

        # Update DT doc hosting IRI if it doesn't match actual hosting IRI 
        if not (data['hosting-iri'] == os.path.join(baseurl, folder)):
            data['hosting-iri'] = os.path.join(baseurl, folder)
            print('::warning file=' + folder + '/index.yaml::Hosting IRI changed for DT-ID: ' \
                + data['dt-id'] + ' . Hosting IRI is now ' + data['hosting-iri'] \
                + ' . Please update the DT-ID registry if needed.')

        # Update editing URLs
        data['edit'] = 'https://github.com/' + repofull + '/edit/main/docs/' + folder + '/index.yaml'
        data['edit-json'] = 'https://github.com/' + repofull + '/edit/main/docs/' + folder + '/index.json'

        # Save DT doc contents in YAML file
        with open(file, 'w') as filew:
            yaml.dump(data, filew, default_flow_style=False, sort_keys=False, allow_unicode=True)
        # copy yaml to json
        with open(file[:-10] + 'index.json', 'w') as jsonfilew:
            json.dump(data, jsonfilew, indent=4)

        # Test if DT-ID redirects to hosting IRI, give actions error if not
        if not (dtweb.client.fetch_host_url(data['dt-id']) == data['hosting-iri'] + '/'):
            print('::error file=' + folder + '/index.yaml::' \
                + 'DT-ID of ' + data['name'] + ' does not redirect to its hosting IRI!' \
                + ' ==> Please update the DT-ID registry.' \
                + ' DT-ID: ' + data['dt-id'] \
                + ' Hosting IRI: ' + data['hosting-iri'])
        else:
            print('Test successful: DT-ID redirects to hosting IRI for ' + data['name'])
            
    except FileNotFoundError:
        print('Did not find YAML file, moving to next one')
