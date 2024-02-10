# datafun-05-sql

## Clone repo from GitHub website
git clone https://github.com/

## Creat project virtual environment
python3 -m venv .venv

## Activate Environment
source .venv/bin/activate

## Install packages
python3 -m pip install pandas
python3 -m pip install pyarrow

## Run pip freeze and redirect the results (>) into requirements.txt
python3 -m pip freeze > requirements.txt

## Push to GitHub
git add .
git commit -m "commit"
git push -u origin main
