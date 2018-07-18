# NBA real-time project

## Description

It's a real-time project that emulate a real game.
You can choose one team from the West and the other from East. When the game starts the score will be update in the browser.

## Prerequisites

You have to install in your computer:

* [Git (Optional)](https://git-scm.com/downloads)
* [docker-compose](https://docs.docker.com/v17.09/compose/install/)
* [Python 3.6](https://www.python.org/downloads/release/python-360/)
* [mysql Connector/Python](https://dev.mysql.com/downloads/file/?id=477196)

## Installation

1. Clone the repo with the command or download the project
    * Clone: ```git clone https://github.com/gmaron/tp2_exercise.git```
    * Download and decompress: https://github.com/gmaron/tp2_exercise/archive/master.zip
2. Config the database/.env file
    * If you stay with the old file, you can login in phpmyadmin as example/example
    * Warning: if you change these vars, you must change it in the database.py file
3. Open a terminal in the root directory
    * Start the database server
        * ```cd database```
        * ```docker-compose up -d```
        * That's all to start the database server. You can check it through the command ```docker ps``` and you could see the containers up. Also, you can enter in http://localhost:8080 and you have to see the welcome page of phpmyadmin.
    * Start the webserver
        * ```cd ..```
        * ```pip install -r webserver/requeriments.txt```
        * ```python webserver/app.py```
            * Make sure python refers to python3. You can check it through ```python -V```
    * Check the project in http://localhost:8888
