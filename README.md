# Django Project Creator
Django template to create new projects.

## Getting Started

### Requirements

- [Docker CE](https://docs.docker.com/engine/installation/) 17.09+
- [Docker Compose](https://docs.docker.com/compose/install/) 1.16+

### Running the project

    $ cd docker
    $ docker-compose up

You'll then be able to access the application on `localhost:8000`

### Running tests

    $ docker-compose run web bash
    $ pytest

To lint the Python code:

    $ flake8
