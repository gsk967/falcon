# falcon
Python Rest Api - The Falcon Web Framework


## Install pip and virtualenv for Ubuntu
```
$ sudo apt-get install python-pip python-dev build-essential 
$ sudo pip install --upgrade pip 
$ sudo pip install --upgrade virtualenv 
```

## Setup project
```
  $ git clone https://github.com/gsk967/falcon.git falcon_project
  $ cd falcon_project
  $ virtualenv .venv
  $ pip install requirements.txt
```

## How to run this project 
```
$ cd falcon_project
$ source .venv/bin/activate
$ gunicorn --reload falcon_sample.app

# checking running or not
$ curl localhost:8000 
```

## Test scripts for falcon
```
$ pytest tests
```