# Install Flask version 2.1.0
package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/bin'],
  creates     => '/usr/local/lib/python3.5/dist-packages/flask-2.1.0.dist-info',
  timeout     => 600,
  environment => ['HOME' => '/root'],
}
