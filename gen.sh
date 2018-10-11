set -e
pip3 install -r requirements.txt
rm -rf gensql/migrations/000* gensql/migrations/__pycache__ db.sqlite3
python manage.py makemigrations
python manage.py sqlmigrate gensql 0001 > result.sql
echo "Success!\nCheck the result.sql."
