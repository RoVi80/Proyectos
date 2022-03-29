mkdir shared-repo
cd shared-repo
git init --bare

cd ..
git clone shared-repo client1
cd client1

touch a.txt
git add a.txt
git commit -m "Some code that exist in the remote repository."
git push

cd ..
rm client1 -Rf
