## Slide Classification App


#### Install necessary software

Windows or MacOS

- Install [Python 3](https://www.python.org/downloads/) -> to run script to help with loading the application 
- Install [Docker](https://docs.docker.com/v17.12/install/#desktop) -> for running the app in a platform-independant manner
- Install [Docker Compose](https://docs.docker.com/compose/install) -> manages connecting multiple services (database, http server)

 Linux

- Install [Python 3](https://www.python.org/downloads/) -> to run script to help with loading the application 
- Install [Docker](https://docs.docker.com/v17.12/install/#server) -> for running the app in a platform-independant manner
- Install [Docker Compose](https://docs.docker.com/compose/install) -> manages connecting multiple services (database, http server)


## Getting the app running

Once Docker Compose is installed, get in a unix-like terminal of your choice. If on windows, I suggest [git bash](http://gitbash.org'). Run `docker-compose build` to pull in the database image and compile the web app image. This may take awhile. Next, run `docker-compose up -d` to start the database and app containers. When this script is completed, run the utils.py script with the command `python3 utils.py`. This will return the local IP address that the web application and database servers are running on. Put the IP address of the web application in the browser of your choice, and you can use the app. 
Additionally, to intialize the database for the web application, the command `docker-compose run --rm web python manage.py migrate` should be run after the `docker-compose up -d` command has successfully run

If the machine running the app loses power or stops running the application, you can run `docker-compose up -d` again to get the application up. The IP address of the application may change, so running the `python3 utils.py` may be neede to get the new address.

Tested on:
[x] - Linux - Ubuntu 
[ ] - MacOS - Majave 
[ ] - Windows - 10


## Usage

Support requests can be made to rmoore8849@gmail.com
