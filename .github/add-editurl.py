import sys, yaml, json

# ARGS: repourl, path

try:
  repo = sys.argv[1]
  path = sys.argv[2]
except:
  print('Enter arguments: repourl, path')
  exit()

with open(r'index.yaml') as file:
  data = yaml.load(file, Loader=yaml.FullLoader)

editurl = 'https://github.com/' + repo + '/edit/main/docs/' + path + 'index.yaml'
data['edit'] = editurl

with open(r'index.yaml', 'w') as filew:
  doc = yaml.dump(data, filew, default_flow_style=False, sort_keys=False)

print('Added editurl: ' + editurl)
