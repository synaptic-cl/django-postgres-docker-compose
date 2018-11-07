## setup

build and up containers:

```
docker-compose up
```

run migrations

```
docker-compose run web python3 manage.py migrate
```

create a user for admin

```
docker-compose run web python manage.py createsuperuser
```

## branch admin_example

The branch admin_example has a example app in djangoadmin.

You can learn how the app was made with the commits.

#### features implemented:
  * filters
  * custom fields in table
  * custom actions buttons in table
  * relations one to many
  * add css for a source
  * add global css
  * modify admin html (dashboard)
  * custom form distribution
