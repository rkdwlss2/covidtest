version: '3.3'
services:
    web:
        build:
            context: ./php
            dockerfile: Dockerfile
        container_name: php73
        depends_on:
            - db
        volumes:
            - ./php:/var/www/html/
        ports:
            - 8000:80
    db:
        container_name: mysql8
        image: mysql:8.0
        command: --default-authentication-plugin=mysql_native_password
        restart: always
        environment:
            MYSQL_ROOT_PASSWORD: root
            MYSQL_DATABASE: test_db
            MYSQL_USER: devuser
            MYSQL_PASSWORD: devpass
        ports:
            - 6033:3306

