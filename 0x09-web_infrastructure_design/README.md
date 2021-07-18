## 0x09. Web infrastructure design
> Web Infrastructure is the physical hardwarem transmission media, and software used to interconnect computers and users on the internet.
> It includes internet servers, web servers, internet storage, network equipment and infructructure software.
> The design is the architecture on the environment to ensure faster response time to users or clients and also allow for further scale in future.

### Horizontal and vertical scaling.
* Horizontal scaling or scaling out involves adding additional servers.
* Vertical scaling or scaling up involves adding more resources to the existing servers.

### Files Descriptions
0. `0-simple_web_stack` - a one server web infrastructure that hosts the website that is reachable via www.foobar.com.
1. `1-distributed_web_infrastructure` - a three server web infrastructure that hosts the website www.foobar.com.
2. `2-secured_and_monitored_web_infrastructure` - a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
3. `3-scale_up` - Split components (web server, application server, database) with their own server

### Resources
#### DNS
* [Learn everything about DNS in cartoon](https://howdns.works/)
* [A](https://support.dnsimple.com/articles/a-record/)
* [CNAME](https://en.wikipedia.org/wiki/CNAME_record)
* [MX](https://en.wikipedia.org/wiki/MX_record)
* [TXT](https://en.wikipedia.org/wiki/TXT_record)
* [Use DNS to scale with round-robin DNS](https://www.dnsknowledge.com/whatis/round-robin-dns/)
* [What is an NS Record?](https://support.dnsimple.com/articles/ns-record/)
* [What is an SOA Record?](https://support.dnsimple.com/articles/soa-record/)
#### Monitoring
* monitoring tools: newRelic, DataDog, Uptime Robot, Nagios, WaveFront.
#### Web Server
* [Wikipedia page about web server](https://en.wikipedia.org/wiki/Web_server)
* [Web server](https://whatis.techtarget.com/definition/Web-server)
* [What is a Web Server?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)
#### Network Basics
* [What is a protocol](https://searchnetworking.techtarget.com/definition/protocol)
* [What is an IP address](https://computer.howstuffworks.com/internet/basics/what-is-an-ip-address.htm)
* [What is TCP/IP](https://searchnetworking.techtarget.com/definition/TCP-IP)
* [What is an Internet Protocol (IP) port?](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
#### Load Balancer
* [Load-balancing](https://www.thegeekstuff.com/2016/01/load-balancer-intro/)
* [Load-balancing algorithms](https://devcentral.f5.com/s/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms)
#### Server
* [What is a server](https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement)
* [What is a server](https://www.youtube.com/watch?v=B1ANfsDyjeA)
* [Where are servers hosted (data centers)](https://www.youtube.com/watch?v=iuqXFC_qIvA&t=33s)
* [LAMP Stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29)
#### Others
* [What is a database](https://searchdatamanagement.techtarget.com/definition/database)
* [What's the difference between a web server and an app server?](https://www.youtube.com/watch?v=S97eKyv2b9M)
* [DNS record types](https://pressable.com/2019/10/11/what-are-dns-records-types-explained-2/)
* [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
* [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
* [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
* [What is HTTPS](https://www.instantssl.com/http-vs-https)
* [What is a firewall](https://www.webopedia.com/definitions/firewall/)

#### Author
[Jane Ng'ethe](https://github.com/Janengethe)