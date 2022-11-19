# Django Biosphere

Welcome to our Biosphere! Complete with animals and plants! (More to come soon)

Lists of Animals and Plants include scientific names. Plants include fields of study.

Have fun exploring!

## Routes Table

| Verb | Path | Action |
| --------- | -------- | -------- |
| GET | plants/plants | index |
| GET | plants/plants/:pk | show |
| POST | plants/plants | create |
| PATCH | plants/plants/:pk | update |
| DELETE | plants/plants/:pk | destroy |
| GET | plants/fields | index |
| GET | plant/fields/:pk | show |
| POST | plants/fields/ | create |
| PATCH | plants/fields/:pk | update |
| DELETE | pants/fields/:pk | destroy |


| Verb | Path | Action |
| --------- | -------- | -------- |
| GET | animals | index |
| GET | animals/:pk | show |
| POST | animals | create |
| PATCH | animals/:pk | update |
| DELETE | animals/:pk | destroy |

## Starting Instructions

Install dependencies:

```pip3 install --upgrade pip```

```pip install pipenv```

```pipenv install django==4.1 psycopg2-binary```

```python manage.py runserver```
