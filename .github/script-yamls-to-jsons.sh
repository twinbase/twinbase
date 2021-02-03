# Remember to update commit message in actions script if you change the contents of this script
cd docs/ 
for dir in */ ; do
  filepath=./${dir}index.yaml # (Hint: trailing / is included in ${dir})
  echo "Converting to JSON: $filepath"
  cd $dir
  # Convert index.yaml to index.json with python:
  python3 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin, Loader=yaml.FullLoader), sys.stdout, indent=4)' < index.yaml > index.json
  cd ..
done
cd ..
