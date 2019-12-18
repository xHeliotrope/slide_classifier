## Slide Classification App


#### Install necessary software

 - Install [Docker](https://docs.docker.com/v17.12/install) -> for running the app in a platform-independant manner
 - Install [Docker Compose](https://docs.docker.com/compose/install) -> manages connecting multiple services (database, http server)

## Getting the app running

Once Docker Compose is installed, get in a unix-like terminal of your choice. If on windows, I suggest [git bash](http://gitbash.org').

Run
```bash
docker-compose up -d
```
to start the database and app containers. When this script is completed, the following can be run:

```bash
docker-compose run --rm web python manage.py migrate
```

If the machine running the app loses power or stops running the application, you can run
```
docker-compose up -d
```
again to get the application up. The IP address of the application may change, so running the


Tested on:
 - [x] - Linux - Ubuntu
 - [x] - MacOS - Majave
 - [ ] - Windows - 10


## Usage

Support requests can be made to rmoore8849@gmail.com
