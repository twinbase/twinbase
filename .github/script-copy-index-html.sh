# Remember to update commit message in actions script if you change the contents of this script
cd docs/ 
for dir in */ ; do
  echo $dir
  if ! [[ $dir == "static/" || $dir == "new-twin/" ]]; then
    echo "Copying static.index.html to ${dir}index.html"
    cp static/index.html ${dir}index.html # (Hint: trailing / is included in ${dir})
  fi
done
cd ..
