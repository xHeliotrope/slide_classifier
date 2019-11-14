## Slide Classification App


#### Install necessary software

Windows

MacOS

 - Install [Python 3](https://www.python.org/downloads/) -> to run script to help with loading the application
 - Install [Docker](https://docs.docker.com/v17.12/install/#desktop) -> for running the app in a platform-independant manner
 - Install [Docker Compose](https://docs.docker.com/compose/install) -> manages connecting multiple services (database, http server)

Caveats
 * Due to how MacOs [internal networking works with Docker](https://docs.docker.com/docker-for-mac/networking/), the app will run on localhost, and using the `utils.py` script to find the http server address is unneeded. However, it is recommended to run `sudo apachectl stop`, in case the default Apache Server that serves apps in the **Sites** Directory is running.

 Linux

 - Install [Python 3](https://www.python.org/downloads/) -> to run script to help with loading the application
 - Install [Docker](https://docs.docker.com/v17.12/install/#server) -> for running the app in a platform-independant manner
 - Install [Docker Compose](https://docs.docker.com/compose/install) -> manages connecting multiple services (database, http server)

## Getting the app running

Once Docker Compose is installed, get in a unix-like terminal of your choice. If on windows, I suggest [git bash](http://gitbash.org').

Run

```bash
docker-compose build
```
to pull in the database image and compile the web app image. This may take awhile. Next, run
```bash
docker-compose up -d
```
to start the database and app containers. When this script is completed, run the utils.py script with the command
```bash
python3 utils.py
```
This will return the local IP address that the web application and database servers are running on. Put the IP address of the web application in the browser of your choice, and you can use the app. Additionally, to intialize the database for the web application, the command
```bash
docker-compose run --rm web python manage.py migrate
```
should be run after
```sh
docker-compose up -d
```
command has successfully run

If the machine running the app loses power or stops running the application, you can run
```
docker-compose up -d
```
again to get the application up. The IP address of the application may change, so running the
```
python3 utils.py
```
may be neede to get the new address.

Tested on:
 - [x] - Linux - Ubuntu
 - [x] - MacOS - Majave
 - [ ] - Windows - 10


## Usage

Support requests can be made to rmoore8849@gmail.com
