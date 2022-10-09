#!/bin/bash
cd $( dirname -- "${BASH_SOURCE[0]}" )
git switch latest_ratings
git pull
python generate_ratings.py
git add -A
git commit -m "`date`"
git push --set-upstream origin latest_ratings
git switch main