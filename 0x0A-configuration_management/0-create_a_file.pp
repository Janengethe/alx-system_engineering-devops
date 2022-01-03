# Create file using Puppet in /tmp

file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  owner   => 'www-data',
  mode    => '0744',
  group   => 'www-data',
  content => 'I love Puppet'
}