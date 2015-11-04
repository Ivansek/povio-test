## Run locally
#### Download source code from this Git repository

```
$ git clone git@github.com:Ivansek/povio-test.git
```

#### Create superuser and apply migrations

```
$ python manage.py syncdb
```

#### Run development server

```
$ python manage.py runserver
```

## Deploying on Heroku
#### Push to Heroku

```
$ git push heroku master
```

#### Start workers

```
$ heroku ps:scale worker=1
```

#### Examine logs for possible errors

```
$ heroku logs -t -p worker
```
