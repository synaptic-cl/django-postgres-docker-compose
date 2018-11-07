## Setup

build and up containers

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

## django-admin example

The branch admin_example has an example app in django-admin.

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
