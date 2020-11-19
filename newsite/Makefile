run-async:
	gunicorn newsite.asgi:application -k uvicorn.workers.UvicornWorker

run:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

su:
	python3 manage.py createsuperuser

push:
	git add .
	git commit -m "$m"
	git push origin master

