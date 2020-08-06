"""
This script is designed to take in a local directory of a cloned lesson repo and the lesson number
It will then:
    -iterate through each repo
    -checkout the canvas branch
    -fix the LaTeX rendering in the README.md
    -and create a lesson on canvas with the provided course number
Example: bash latex-to-canvas.sh phase2-repos 343  - this will use the post-grad folder and pass 154 as the course id
Requires github-to-canvas gem
"""


if [ $# -eq 0 ] || [ $# -eq 1 ] || [ $# -eq 2 ]
  then
    echo "Three arguments required - the folder name to iterate through, the canvas course id, and the LaTeX inticator character"
    echo "Example: bash latex-to-canvas.sh phase2-repos 343 "
    exit 1
fi


REPOS=$PWD/$1/*

cd $1

for r in $REPOS
do
  
  cd $r
  git checkout -b canvas

  python ~/latex-to-canvas.py README.md $3

  git add .
  git commit -m 'Corrected LaTeX rendering with latex-to-canvas script'

   
  github-to-canvas -c $2 -slr --type page -b canvas
  
  # Avoid limits with sleep for large amounts of repos
  sleep 5;
done



