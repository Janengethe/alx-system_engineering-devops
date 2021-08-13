# creates a manifest that kills 'killmenow'

exec { 'killmenow':
  command => 'pkill -f killmenow'
}