# Remember to update commit message in actions script if you change the contents of this script
cd docs/ 
for dir in */ ; do
  cd $dir
  echo "Adding editurl to ${dir}index.yaml"
  python3 ${GITHUB_WORKSPACE}/.github/add-editurl.py "${GITHUB_REPOSITORY}" "${dir}" # (Hint: trailing / is included in ${dir})
  cd ..
done
cd ..
