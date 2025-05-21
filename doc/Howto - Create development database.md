# Create a postgresql user and a database

Creating a development user and a development database.
```
$ sudo -i -u postgres
[sudo] password for hemi:
postgres@adm-134679:~$ psql
psql (14.17 (Ubuntu 14.17-0ubuntu0.22.04.1))
Type "help" for help.

postgres=# CREATE USER multtrainer PASSWORD 'devpassword';
CREATE ROLE
postgres=# CREATE DATABASE "multiplication-trainer" OWNER tekvideo;
CREATE DATABASE
postgres=# \l
                                                       List of databases
               Name               |            Owner             | Encoding |   Collate   |    Ctype    |   Access privileges   
----------------------------------+------------------------------+----------+-------------+-------------+-----------------------
 multiplication-trainer           | tekvideo                     | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
postgres=# \q
```

Create tables in the development database
```
FLASK_APP='app:create_app("config.DevConfig")' flask db upgrade
```

Early in the development the first database snapshot has to be
generated, this is done using these commands.
```
FLASK_APP='app:create_app("config.DevConfig")' flask db init
FLASK_APP='app:create_app("config.DevConfig")' flask db migrate -m "Initialize database"
```


