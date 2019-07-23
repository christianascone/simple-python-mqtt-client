# Simple Python Mqtt Client
> A python script able to message with mqtt broker

![Project Version][project-image]
![PYTHON Version][python-image]

## Requirements

 - Virtualenv

## Installation

Create and enable the virtual environment

```sh
virtualenv -p python3 venv
. venv/bin/activate
```

Install dependencies
```sh
pipenv install
```

## Configuration

Project configuration must be done making a copy of `.env.example` to `.env`.

Then edit this last file adding values.

## Usage example

Run it with following command:
```sh
python3 broker_manager.py
```

## Release History

* 0.0.2
    * ADDED: log, powermode and main topic functions
* 0.0.1
    * Work in progress

## Meta

Christian Ascone – ascone.christian@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

<!-- Markdown link & img dfn's -->
[project-image]: https://img.shields.io/badge/simple_python_mqtt_client-0.00.02-green.svg
[python-image]: https://img.shields.io/badge/python-3.7-brightgreen.svg