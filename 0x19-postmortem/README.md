Postmortem
the following is a postmortem document in which will be given a summary about a bug found in an Apache 2 server

on Tuesday 09/29/2020 Holberton School released the project

 0x17. Web stack debugging #3

around 00:00 (PST), at that time occurred a problem with the server.

This server was an apache2 webserver running on a container with ubuntu 1404 and was returning an internal error server error 500 causing a great impact having in account 90% of users were affected



the context
this was a WordPress which should display an HTML file but instead was showing out a website disabled because of a typo mistake in a PHP file so all GET requests returned with 500 status code

debugging timeline

* 9/29/2020, 00:00 (PST) started the project

* 9/29/2020, 10:00 (PST) the bu was noticed, started looking for the causes

* 9/29/2020, 15:00 (PST) with the help of some tools (tmux, strace) could find the error

(no such a file or directory) was seen because of a typo error in a configuration file

* 9/29/2020, 15:30 (PST) the typo was corrected (a mistake on extension .phpp - .php )

* 9/29/2020, 16:15 (PST) a puppet code was written to solve this issue in the future if it occurs again or if this happens in another server

the root of the bug
after trying to start the service was noticed an error in /var/log/apache2 so was decided to test the process with PS (Linux command) and strace (Linux command) to see what processes in Apache2 execution were the cause of the bug-finding this line: require_once( ABSPATH . WPINC . ‘/class-wp-locale.phpp’ )

was decided to look for that file and correct the typo then tested again obtaining the correct answer with a 200 status code

what was the solution:
was written a puppet script that was able to solve this and provided the posibility to automate the task in case it occurs again or in multiple servers

this is the command used :

command => ‘sed -i “s/.phpp/.php/g”

how to prevent
there are many things that can be applied to avoid this kind of mistakes, lets list some

* it can be implemented a kind of test that verify for certain standard files that should be present in a setting process

* a document describing the previous status, changes, current status, changes and who made it

* monitoring tools that alert since the first moment about possible issues

* version review after any change