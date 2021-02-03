# Remember to update commit message in actions script if you change the contents of this script
cd docs/ 
for dir in */ ; do
  echo "Adding editurl to ${dir}index.yaml"
  echo "Current directory: $PWD"
  echo "ls:"
  ls
  python3 ${GITHUB_WORKSPACE}/.github/add-editurl.py "${GITHUB_REPOSITORY}" "${dir}" # (Hint: trailing / is included in ${dir})
done
cd ..
