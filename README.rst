***********************
Introduction & Settings
***********************

Introduction
============

Simple Pastebin clone application

Setup (Docker recommended)
================

No local setup should be needed apart from:
- `docker <https://docs.docker.com/engine/installation/>`__
- `docker-compose <https://docs.docker.com/compose/>`__
- creating a .env file with the following Environment variables.

.. code:: bash
    DEBUG=whatever
    SECRET_KEY=whatever
    PG_USERNAME=whatever
    PG_PASSWORD=whatever
    PG_NAME=whatever
    PG_HOST=whatever
    PG_PORT=whatever

The local dev setup uses **docker-compose** to spin up all necessary services.
Make sure you have it installed and can connect to the **docker daemon**.

Build the app
-------------

Run in project directory after you clone the repository:

.. code:: bash

    docker-compose build

Run the app
===========

Start the dev server
------------------

Run in project directory:

.. code:: bash

    docker-compose up

This will build and download the containers and start them. The ``docker-compose.yml``
file describes the setup of the containers.

The web server should be reachable at ``http://localhost:8000``.

.. note:: if you're not using docker, create a virtualenv.
    create a .env inside the project root directory with the Envs variables above.
    Run migrations with (python manage.py migrate)
    Run tests with (python manage.py test)
    Run dev server (python manage.py runserver)


Run commands on the server
==========================

Each docker container uses the same script as entrypoint. The ``entrypoint.sh``
script offers a range of commands to start services or run commands.
The full list of commands can be seen in the script.
The pattern to run a command is always
``docker-compose run <container-name> <entrypoint-command> <...args>``

The following are some examples:

+-------------------------------------+----------------------------------------------------------+
| Action                              | Command                                                  |
+=====================================+==========================================================+
| Run tests                           | ``docker-compose run pastebin test``                     |
+-------------------------------------+----------------------------------------------------------+
| Run django commands                 | ``docker-compose run pastebin manage help``              |
+-------------------------------------+----------------------------------------------------------+
| Create a django shell               | ``docker-compose run pastebin manage shell``             |
+-------------------------------------+----------------------------------------------------------+
| Show ORM migrations                 | ``docker-compose run pastebin manage showmigrations``    |
+-------------------------------------+----------------------------------------------------------+


Containers and services
=======================

These are the two containers we have.

+-----------+-------------------------------------------------------------------------+
| Container | Description                                                             |
+===========+=========================================================================+
| pastebin  | `Django <https://www.djangoproject.com/>`__                             |
+-----------+-------------------------------------------------------------------------+
| db        | `PostgreSQL <https://www.postgresql.org/>`__ database                   |
+-----------+-------------------------------------------------------------------------+

All of the container definitions for development can be found in the ``docker-compose.yml``.

.. note:: Postgresql uses Django ORM models for table configuration and migrations.
