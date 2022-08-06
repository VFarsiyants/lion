# Lion - wsgi framework

This repository is created for study reasons.

To start framework it's requiered python 3.9.2

To install all pakages use:

`pip install -r requierements.txt`

### System check

To check you sistem use uwsgi with file simple_wsgi.py

`uwsgi --http :8000 --wsgi-file simple_wsgi.py`

It should possible to view hello message on localhost:8000


### Example application

to start example application execute command fron virtual environment:

`python run.py`

now to pages on localhost:8080 available: / and /about
