# creates a manifest that kills 'killmenow'

exec { 'pkill':
  command  => 'pkill -f killmenow',
  provider => 'shell'
}