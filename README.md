# Belvo test

## Prerequisites
To run the project you only need to have the docker in your local environment, after that go to Intallation section.

- Docker (https://docs.docker.com/get-docker/)
- Git (https://git-scm.com/downloads)

## Installation
Once you have the git installed in your machine, please open your terminal and in the directory you want, run the command below.

```sh
https://github.com/oOojhonnyoOo/belvo-test.git
```

You just copied the project in your local environment, now please go to the newly created directory.

```sh
cd belvo-test
```

Now you need to create the containers, so run the command below.

```sh
docker-compose up -d
```

It can take a while because the docker are download the images to your local machine. After the command has been executed, we need to run the migrations inside the containers, so again run the following command.

```sh
docker exec -it belvo_service sh
```

Right now, you are inside the container you can be able to run the migrations.

```sh
python manage.py migrate
```

Now everything is ready to be tested.

## Testing

You can check if the database connection is fine with your machine using the following connection:

```sh
jdbc:mysql://127.0.0.1:3307/?user=belvo
```

***P.S.: the password to connect to the database is `belvo`***

When you create the containers both the database and the server are already running on your machine, the server is available on `http://localhost:8000`. To test the API application you can do it using postman if you want, to make your life easier, I've already created a collection that you can just import and start using, to import the collection on your machine, open your postman and click the import button, then paste the url below.

```sh
https://api.postman.com/collections/5439843-d91acd52-5393-40f2-98e5-ebf592f9e791?access_key=PMAT-01H1CZEMW2NK54ZVNQ3J4Z4J6Q
```

## The API

If you had difficulty or didn't want to use postman to test the application, no problem, you can take a look at the documentation and test it in your local environment.

- API Documentation (https://documenter.getpostman.com/view/5439843/2s93m7W265)

