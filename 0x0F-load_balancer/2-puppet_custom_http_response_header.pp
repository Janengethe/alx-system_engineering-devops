# Creates a custom HTTP header
#using puppet

file_line { 'add header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}
service { 'nginx':
  ensure => running,
}