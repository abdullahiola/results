## Follow these commands to run the project on your local machine :

Clone the project 
```
git clone https://github.com/abdullahiola/results.git
```

Enter the project directory 

```
cd api (for the api folder)
cd checker (for the checker folder)
cd register (for the register folder)
```

Create a virtual env in each of the folders

```
python -m venv env
(inside each directory/folder)
```

Activate your env(for windows)

```
./env/Scripts/activate 	 
```
(for Linux or mac)

```
source env/bin/activate 
``` 

Install Project Dependencies

```
pip install -r requirements.txt
```

Make Migrations

```
python manage.py makemigrations
python manage.py migrate
```


Create Superuser

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver 4500 
```

To run Celery locally:
```
celery -A workdistrobe worker -l INFO 
```

View the api documentation at:
`https://localhost:8000/api/docs`
