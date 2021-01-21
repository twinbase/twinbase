 for dir in */ ; do
  echo "$dir"
  filepath=./${dir}index.yaml
  echo $filepath
  cd $dir
  python3 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin, Loader=yaml.FullLoader), sys.stdout, indent=4)' < index.yaml > index.json
  cd ..
done