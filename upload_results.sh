#!/bin/bash
cd $( dirname -- "${BASH_SOURCE[0]}" )
git pull
source ~/miniconda3/bin/activate fussball_rankings
python generate_ratings.py && git add -A && git commit -m "`date`" && git push --set-upstream origin main