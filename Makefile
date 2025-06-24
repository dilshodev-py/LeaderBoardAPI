mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

ws:
	daphne -b 0.0.0.0 -p 8001 root.asgi:application