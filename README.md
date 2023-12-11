## Follow these commands to run the project on your local machine :

Clone the project 
```
git clone https://github.com/abdullahiola/results.git
```

Enter the project directory 

```
cd api 
```

Create a virtual env in each of the folders

```
python -m venv env
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

#### Repeat these steps for the checker and register 
#### Make sure you change the port number when trying to run the server
