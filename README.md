# *LOGIK*

LOGIK is an AI-powered advertisement recommender for public digital screens.


## Installation

Create a new environments using the command:

```bash
python3 -m venv /path/to/new/virtual/environment
```

Activate the environment using the command:

```bash
source path/to/env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to run the following commands:

Upgrade PIP
```bash
python3 -m pip -upgrade pip
```

Install the requirements:

```bash
pip install -r requirements.txt
```
This will install the pip packages including: django, psycopg2-binary, django-jquery.

## Usage

In order to run the app you will need to setup a POSTGRES database in your local machine.

All names and passwords **must** be "intern". The name of the database **must** be togik.

```bash
sudo apt install postgresql postgresql-contrib
sudo -i -u postgres
psql

createuser --interactive
Enter name of role to add: intern
Shall the new role be a superuser? (y/n) y

createdb togik
```

Run the following commands in the same environment to setup django admin user:

All usernames and passwords **should** be "intern".

```bash
cd path/to/logik/datamodule

python3 manage.py createsuperuser

Username: intern
Email address: intern@intern.com
Password: intern
Password (again): intern
```

Complete database migrations using the following commands:

```bash
cd path/to/logik/datamodule

python3 manage.py makemigrations
python3 manage.py migrate
```

Admin and database setups are complete. Now, run the server using the following commands:


```bash
cd path/to/logik/datamodule

python3 manage.py runserver
```

Go to the address http://localhost:8000/ to view the app.

NOTE: 127.0.0.1:8000 will not work because it is not in the list of ALLOWED HOSTS. This can be changed from settings.py inside *logik*.
