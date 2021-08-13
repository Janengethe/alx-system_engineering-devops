# creates a manifest that kills 'killmenow'

exec { 'pkill killmenow':
  command => 'pkill -f killmenow'
}