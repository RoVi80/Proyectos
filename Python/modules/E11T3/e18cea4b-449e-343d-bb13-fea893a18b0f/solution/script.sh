
git clone $REPO_URL repo
cd repo

printf "ccc" > c.txt

git add c.txt
git add d.txt
git commit -m "Add new file c.txt with some content"

git push
