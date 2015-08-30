$venv = '/opt/demo-site/venv'

file { [ '/opt/demo-site', '/opt/demo-site/static' ]:
  ensure => directory,
  owner  => vagrant,
  group  => vagrant
}

file { '/home/vagrant/.bashrc':
  ensure => link,
  target => '/vagrant/bin/bashrc',
  owner  => vagrant
}

exec {'apt-get update':
  command => '/usr/bin/apt-get update'
}
->
package {['python3-pip', 'supervisor', 'python3-all', 'python3-setuptools', 'python3-dev', 'build-essential', 'htop']:
  ensure  => installed,
  require => Exec['apt-get update']
}
->
exec { 'make-venv':  # Create a virtual env without install pip. This is required because the Debian packaging of the virtualenv module breaks pip
  command => "/usr/bin/python3 -m venv --without-pip ${venv}",
  user    => vagrant,
  creates => $venv,
  require => File['/opt/demo-site'],
}
->
exec { 'install-pip':  # Install pip for ourselves. get-pip.py contains a cut-down version of pip that can do 'pip install pip'
  command => "${venv}/bin/python3 /vagrant/bin/get-pip.py",
  user    => vagrant,
  creates => "${venv}/bin/pip"
}
->
exec { 'develop':  # Install our code as a module in the venv
  command => "${venv}/bin/python3 /vagrant/setup.py develop",
  user    => vagrant,
  cwd     => '/vagrant',
  creates => "${venv}/lib/python3.4/site-packages/pycon-demo.egg-link"
}
->
exec { 'reload-dev':  # reload-dev.sh runs migrate etc
  command     => '/vagrant/bin/reload-dev.sh',
  user        => root,
  refreshonly => true,
  require     => File['/opt/demo-site/pycon-demo.ini']
}

file {'/opt/demo-site/pycon-demo.ini':
  ensure  => link,
  require => File['/opt/demo-site'],
  target  => '/vagrant/conf/pycon-demo.ini.vagrant',
}

## Postgres

package { ['postgresql-9.3', 'libpq-dev']:
  ensure  => installed,
  notify  => [Service['postgresql'], Exec['create-postgres-user'], Exec['reload-dev']],
  require => Exec['apt-get update']
}

service { 'postgresql': ensure => running }

exec { 'create-postgres-user':
  require     => [Package['postgresql-9.3'], Service['postgresql']],
  refreshonly => true,
  command     => "/bin/su - postgres -c 'createuser vagrant -d'",
}

## Supervisor
group { 'supervisor':
  ensure => present
}
->
user { 'vagrant':
  groups => ['supervisor']
}

file { '/etc/supervisor/supervisord.conf':
  content => '
; supervisor config file
; managed by puppet, changes will be discarded

[unix_http_server]
file=/var/run/supervisor.sock   ; (the path to the socket file)
chmod=0770                       ; socket file mode (default 0700)
chown=root:supervisor

[supervisord]
logfile=/var/log/supervisor/supervisord.log ; (main log file;default $CWD/supervisord.log)
pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
childlogdir=/var/log/supervisor            ; (AUTO child log dir, default $TEMP)

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock ; use a unix:// URL  for a unix socket

; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.

[include]
files = /etc/supervisor/conf.d/*.conf
',
  require => Package['supervisor'],
  notify  => Service['supervisor'],
  owner   => 'root'
}

## Supervisor config

service {'supervisor':
  ensure  => running,
  require => [
              Group['supervisor'],
              Package['supervisor'],
              File['/etc/supervisor/conf.d/pycon-demo.conf'],
              File['/opt/demo-site/pycon-demo.ini'],
              File['/etc/supervisor/supervisord.conf'],
              Exec['reload-dev']
              ],
}

file {'/etc/supervisor/conf.d/pycon-demo.conf':
  content => "
[program:gunicorn]
command=${venv}/bin/gunicorn --log-level=DEBUG pycon_demo.wsgi --bind=unix://opt/demo-site/demo-site.sock --reload --workers 4 --env PYCON_DEMO_CONFIG=\"/opt/demo-site/pycon-demo.ini\"
user=vagrant
numprocs=1
  ",
  owner => root,
  require => [Exec['develop'], Package['supervisor'], File['/opt/demo-site/pycon-demo.ini']],
}
~>
exec {'/usr/bin/supervisorctl update':
  refreshonly => true,
  require     => Service['supervisor']
}


## nginx

package { 'nginx':
  ensure => present
}

file { '/etc/nginx/sites-available/default':
  content => "
server {
        listen 8080 default_server;
        listen [::]:8080 default_server ipv6only=on;

        server_name localhost;

        location /static {
          alias /opt/demo-site/static;
        }

        location / {
          proxy_pass http://unix:/opt/demo-site/demo-site.sock:/;
          proxy_pass_header Server;
          proxy_set_header Host \$http_host;
          proxy_redirect off;
          proxy_set_header X-Real-IP \$remote_addr;
          proxy_set_header X-Forwarded-Proto \$scheme;
        }
}
",
require => Package['nginx'],
notify  => Service['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
