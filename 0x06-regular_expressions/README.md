## 0x06. Regular expression
> A regular expression, commonly called a “regexp”, is a sequence of characters
> that define a search pattern.  It is mainly for use in pattern matching with
> strings, or string matching (i.e. it operates like a “find and replace”
> command). While it is a very powerful tool, it is also very dangerous because
> of its complexity.
> Different languages use different regexp engines. That means that a regexp in
> Python, for example, will be interpreted differently in Javascript:

> Regular expressions are everywhere and software engineers, no matter their
> positions, will have to use them during their careers. System administrators
> and DevOps are the ones using them the most because they are very handy for
> log parsing.

### Reference Materials
* [http://www.regular-expressions.info/](http://www.regular-expressions.info/)
* [http://www.w3schools.com/jsref/jsref_obj_regexp.asp](https://www.w3schools.com/jsref/jsref_obj_regexp.asp)
* Ruby: [http://rubular.com/](https://rubular.com/)
* PHP/Javascript/Python: [https://regex101.com/](https://regex101.com/)
* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)
* [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
* [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

### Background Context
For this project, am building regular expression using Oniguruma, a regular
expression library that which is used by Ruby by default. Other regular
expression libraries sometimes have different properties other than the ones used here.

Because the focus of this project is to play with regular expressions (regex),
here is the Ruby code that I used, just replacing the regexp part, meaning the code in between the //:
```
Terminal1$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
Terminal1$
Terminal1$ ./example.rb 127.0.0.2
127.0.0.2
Terminal$ ./example.rb 127.0.0.1
127.0.0.1
Terminal$ ./example.rb 127.0.0.a
```

### Files Descriptions
* `0-simply_match_holberton.rb`-a Ruby script that accepts one argument and pass it to a regular expression matching method. he regular expression matches `Holberton`.
* `1-repetition_token_0.rb`- a Ruby script that accepts one argument and pass it to a regular expression matching method
* `2-repetition_token_1.rb`- a Ruby script that accepts one argument and pass it to a regular expression matching method
* `3-repetition_token_2.rb`- a Ruby script that accepts one argument and pass it to a regular expression matching method
* `4-repetition_token_3.rb0`- a Ruby script that accepts one argument and pass it to a regular expression matching method. Your regex should not contain square brackets
* `5-beginning_and_end.rb`- The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between. Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* `6-phone_number.rb`- The regular expression must match a 10 digit phone number
* `7-OMG_WHY_ARE_YOU_SHOUTING.rb`- The regular expression must be only matching: capital letters
* `100-textme.rb`- our script should output: `[SENDER]`,`[RECEIVER]`,`[FLAGS]`. The sender phone number or name (including country code if present). The receiver phone number or name (including country code if present). The flags that were used. Log file:
```
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
+17272713208,+19172319348,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
18572406905,14022180266,-1:0:-1:-1:-1
$
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
12392190384,19148265919,-1:0:-1:-1:-1
$
```