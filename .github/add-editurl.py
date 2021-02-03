import sys, yaml, json

# ARGS: repourl, path

print('YAML version: ' + yaml.__version__)

try:
  repo = sys.argv[1]
  path = sys.argv[2]
except:
  print('Enter arguments: repourl, path')
  exit()

print('Repourl: ' + repo)
print('Twin path:' + path)

with open(r'index.yaml') as file:
  data = yaml.load(file)

editurl = 'https://github.com/' + repo + '/edit/main/docs/' + path + 'index.yaml'
data['edit'] = editurl

with open(r'index2.yaml', 'w') as filew:
  doc = yaml.dump(data, filew, default_flow_style=False, sort_keys=False)

print('Added editurl: ' + editurl)
