create_app:
	python3 manage.py startapp apps

run:
	python3 manage.py runserver localhost

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

create_user:
	python3 manage.py createsuperuser