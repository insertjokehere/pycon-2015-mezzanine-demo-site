import configparser
import logging
import logging.config
import io
import os


DEFAULT_CONFIGURATION = """
[django]
## The secret key must be set or the app will fail to run.
## You should set your own
secret_key = ae46a80a-8376-4e22-8f05-ff53cf2603c9ed0dacab-1382-4c1d-884c-2a3fe9d2a19a
debug = True
allowed_hosts = localhost
static_root =

[database]
engine = django.db.backends.sqlite3
name = dev.db
user =
password =
host =
port =
"""


def read_config():
    config = configparser.RawConfigParser(allow_no_value=True)

    config.readfp(io.StringIO(DEFAULT_CONFIGURATION))

    if 'PYCON_DEMO_CONFIG' in os.environ.keys():
        config.read(os.environ['PYCON_DEMO_CONFIG'])

    return config


CONFIG = read_config()
