#/usr/bin/env sh
ssh-agent
if [ ! -d '~/freebsd-ports' ] ; then
  git clone git+ssh://git@github.com/GhostBSD/freebsd-ports.git
fi

cd freebsd-ports
git remote -v | grep -q fbsdports
if [ $? -eq 1 ] ; then
  git remote add fbsdports https://github.com/freebsd/freebsd-ports.git
fi

git fetch fbsdports
git checkout master
git merge fbsdports/master
ssh-agent
git push origin master
