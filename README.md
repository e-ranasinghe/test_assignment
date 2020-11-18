

## Installation

1. Clone project:

```bash
git clone https://github.com/e-ranasinghe/test_assignment.git
```

2. Create and start a virtual environment in project folder:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Django migrations:

```bash
python manage.py makemigrations app
python manage.py migrate
```
5. Start Django Project:

```bash
python manage.py runserver
```

6. Open localhost:8000 on your browser to view the app.

```bash
Use user for testing: 
login: eric 
password: 1234
```