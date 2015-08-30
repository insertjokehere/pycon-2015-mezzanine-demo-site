#!/bin/sh

export PYCON_DEMO_CONFIG="/opt/demo-site/pycon-demo.ini"

cd $(dirname $0)/../

. /opt/demo-site/venv/bin/activate

supervisorctl stop all

dropdb vagrant || true
createdb vagrant

pycon_demo syncdb --noinput

echo "from django.contrib.auth.models import User; " \
     "User.objects.create_superuser('vagrant', 'vagrant@example.com', 'vagrant')" | pycon_demo shell --plain > /dev/null

pycon_demo collectstatic --link --noinput

supervisorctl start all
