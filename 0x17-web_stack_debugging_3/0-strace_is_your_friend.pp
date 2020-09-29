# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.
# uses this command to find out the bug:
# ps h --ppid $(cat /var/run/apache2/apache2.pid) | awk '{print"-p " $1}' | xarg# s sudo strace -o strace.txt

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}