#configures to connect server without password

file_line { 'PasswordAuthentication':
  ensure => 'present',
  path   => '~/.ssh/holberton',
  line   => 'PasswordAuthentication no',
}
file_line {'IdentityFile':
  ensure => 'present',
  path   => '~/.ssh/holberton',
  line   => 'IdentityFile ~/.ssh/holberton'
}