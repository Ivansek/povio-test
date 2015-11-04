## Deploying on Heroku
```
$ git push heroku master
```

```
$ heroku ps:scale worker=1
```

```
$ heroku logs -t -p worker
```
