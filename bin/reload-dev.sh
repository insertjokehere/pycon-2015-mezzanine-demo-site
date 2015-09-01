#!/bin/sh

export PYCON_DEMO_CONFIG="/opt/demo-site/pycon-demo.ini"

cd $(dirname $0)/../

. /opt/demo-site/venv/bin/activate

pip install -r requirements/dev.txt

supervisorctl stop all

dropdb vagrant || true
createdb vagrant

pycon_demo syncdb --noinput

pycon_demo loaddata ./fixtures/site_data.json

pycon_demo collectstatic --link --noinput

mkdir -p /opt/demo-site/static/media/uploads

cp ./fixtures/*.jpg /opt/demo-site/static/media/uploads

supervisorctl start all || true
