## 0x1B. Web stack debugging #4
* In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

* For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 747 requests failed, let’s fix our stack so that we get to 0.

### Illustration
```
root@4961b47846be:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   3.177 seconds
Complete requests:      2000
Failed requests:        747
   (Connect: 0, Receive: 0, Length: 747, Exceptions: 0)
Non-2xx responses:      1253
Total transferred:      1102054 bytes
HTML transferred:       709017 bytes
Requests per second:    629.50 [#/sec] (mean)
Time per request:       158.856 [ms] (mean)
Time per request:       1.589 [ms] (mean, across all concurrent requests)
Transfer rate:          338.74 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   2.2      0      96
Processing:     2  155  50.0    197     298
Waiting:        2  155  50.1    196     298
Total:          6  155  49.9    197     298

Percentage of the requests served within a certain time (ms)
  50%    197
  66%    198
  75%    198
  80%    199
  90%    199
  95%    199
  98%    201
  99%    201
 100%    298 (longest request)
root@4961b47846be:~# 
```
shows `Failed requests:        747`

### Solution
* [Source](https://www.cyberciti.biz/faq/linux-unix-nginx-too-many-open-files/)

* change the operating system limit to a higher number that the one in the system already(ie 15).
* Edit the file `/etc/default/nginx` change the limit value to 10,000
* Restart nginx, then query again to give `Failed requests:        0`

```
root@4961b47846be:~# puppet apply 0-the_sky_is_the_limit_not.pp 
Notice: Compiled catalog for 4961b47846be.ec2.internal in environment production in 0.20 seconds
Notice: /Stage[main]/Main/Exec[nginx requests]/returns: executed successfully
Notice: /Stage[main]/Main/Exec[restart nginx]/returns: executed successfully
Notice: Finished catalog run in 1.80 seconds
root@4961b47846be:~#
```
```
root@4961b47846be:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   2.553 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    783.46 [#/sec] (mean)
Time per request:       127.640 [ms] (mean)
Time per request:       1.276 [ms] (mean, across all concurrent requests)
Transfer rate:          652.62 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   10  27.6      1     100
Processing:     1  115  59.7    100     396
Waiting:        1  110  58.4     99     396
Total:          3  126  61.6    101     397

Percentage of the requests served within a certain time (ms)
  50%    101
  66%    103
  75%    196
  80%    197
  90%    199
  95%    201
  98%    294
  99%    298
 100%    397 (longest request)
root@4961b47846be:~#
```