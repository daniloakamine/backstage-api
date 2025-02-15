# backstage-api

### Dependencies

- Python 3.x

### Installation

1.  Create a virtual env:

        python3 -m venv venv

2.  Enable virtual env:

        source venv/bin/activate

3.  Install requirements via `pip`:

        pip install -r requirements.txt

4.  Create database tables (sqlite):

        python manage.py migrate

5.  Create superuser for Admin (optional):

        python manage.py createsuperuser

### APIs

1.  Run:

        python manage.py runserver

2.  Open Swagger:

        open http://localhost:8000/swagger/

### Tests

Run tests:

        pytest
