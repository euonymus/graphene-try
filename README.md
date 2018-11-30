# graphene-try
GraphQL Server using graphene

# Refferences
* [graphql-python Tutorial](https://www.howtographql.com/graphql-python/0-introduction/)

# Requirements

* Python 3.6
* pip
* django
* graphene
* graphene-django
* django-filter
* django-graphql-jwt

```
$ pip install django==2.0.2 graphene==2.0.1 graphene-django==2.0.0 django-filter==1.1.0 django-graphql-jwt==0.1.5
```

# Tools You use

* [Insomnia](https://insomnia.rest/)

## Local Preparation

```
# environment for local development
$ git clone {this repository}
$ cd {reposity path}
$ pip install -r requirements.txt

# 
$ source venv/bin/activate
$ python manage.py makemigrations
$ python manage.py migrate
```

## Run Your Own Prisma Serve

```
$ python manage.py runserver
```

Access to http://localhost:8000/graphql/

## How to import Link datas

```
$ python manage.py shell
>>> from links.models import Link
>>> Link.objects.create(url='https://www.howtographql.com/', description='The Fullstack Tutorial for GraphQL')
>>> Link.objects.create(url='https://twitter.com/jonatasbaldin/', description='The Jonatas Baldin Twitter')

```

