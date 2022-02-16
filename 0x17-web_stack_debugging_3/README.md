## 0x17. Web stack debugging #3

> When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

> Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

> Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

> The web stack you are debugging today is a Wordpress website running on a LAMP stack.

### Install puppet-lint
`$ apt-get install -y ruby`
`$ gem install puppet-lint -v 2.1.1`


* Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet.

Hint:

strace can attach to a current running process
You can use [`tmux`](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) to run strace in one window and `curl` in another one


### Example:

```
root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#
```

### Solution
```
# terminal 1
$ cat /var/log/apache2/error.log #No errors found
$ vi /etc/php5/apache2/php.ini #Change the display_errors form 'off' to 'on'
$ curl -sI 127.0.0.1 #Now returns status of 200

$ strace -p <pid of apache2> #strace will wait for actions in another terminal
```

```
#In onother terminal
$ curl -sI 127.0.0.1 #this raises error in terminal 1
```

```
# terminal 1
# After curling in other terminal, we see 'open("/var/www/html/wp-includes/class-wp-locale.php
", O_RDONLY) = -1 ENOENT (No such file or directory)'
# Opening /var/log/apache2/error.log, we see 'PHP Fatal error: require_once(): Failed opening required '/var/www/html/wp-includes/class-wp-locale.phpp' (include_path='.:/usr/share/php:/usr/share/pear') in /var/www/html/wp-settings.php on line 137'
$ emacs /var/www/html/wp-settings.php # line 137 fix spelling error from '.phpp' to '.php'
```
