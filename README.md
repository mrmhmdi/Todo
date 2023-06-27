1-create venv and install requirements.txt
  python3 -m venv env
  source env/bin/activate # work in linux for windows google it :)
  pip3 install -r requirements.txt

2-python3 manage.py migrate

4-create superuser in django
  python3 manage.py createsuperuser
  
5-python manage.py runserver
  open 127.0.0.1:8000 in browser
