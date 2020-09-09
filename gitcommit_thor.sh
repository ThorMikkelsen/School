#!/bin/bash

#cd /linuxopg
git add *
git config --global user.email "thor.mikkelsen@gmail.com"
git config --global user.name "ThorMikkelsen"
echo Navn til commiten?
read commit
git commit -m $commit
git push
