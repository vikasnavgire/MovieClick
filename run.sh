#!/bin/bash
## This is docker application run automated script. - Vikas N, July 2017 

set -x # Debug mode

docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=db -e MYSQL_USER=root -p 3306:3306 -d mysql

docker run -d -p 5000:5000 -v /home/vikas/workspace/MovieClick/:/app/ --name movie-click movieclick
