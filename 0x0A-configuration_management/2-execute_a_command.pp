# create a manifest that kills a process named killmenow
$paths = ['/usr/bin', '/sbin', '/bin', '/usr/sbin']

exec { 'killmenow':
  path    => $paths,
  command => 'pkill -f killmenow',
}