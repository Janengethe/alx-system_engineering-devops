## 0x05. Processes and signals

### Reference Materials
* [Linux PID](http://www.linfo.org/pid.html)
* [Linux Process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux Signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)
* Man/Help - ps, pgrep, pkill, kill, exit, trap
* [All Signals](https://www.computerhope.com/unix/signals.htm)

#### Take Homes
> What is a PID.
> What is a process.
> How to find a process' PID.
> How to kill a process.
> What is a signal.
> What are the 2 signals that cannot be ignored.

### File Description
* 0-what-is-my-pid - a Bash script that displays its own PID
* 1-list_your_processes - a Bash script that displays a list of currently running processes. Requirements: Must show all processes, for all users, including those which might not have a TTY, Display in a user-oriented format, Show process hierarchy.
* 2-show_your_bash_pid - Using your 1-list_your_processes exercise command, it's a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. Requirements:The third line of the script is # shellcheck disable=SC2009 (for more info about ignoring shellcheck error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))
* 3-show_your_bash_pid_made_easy - a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
* 4-to_infinity_and_beyond-  a Bash script that displays To infinity and beyond indefinitely.
* 5-dont_stop_me_now - to stop 4-to_infinity_and_beyond process we use ctrl+c in the previous file, there is actually another way to do this. This is a Bash script that stops 4-to_infinity_and_beyond process, using `kill`.
* 6-stop_me_if_you_can - a Bash script that stops 4-to_infinity_and_beyond process, without using `kill` or `killall`.
* 7-highlander - a Bash script that displays:a).**To infinity and beyond** indefinitely, With a sleep 2 in between each iteration, b).**I am invincible!!!** when receiving a SIGTERM signal.
* 67-stop_me_if_you_can - a copy of 6-stop_me_if_you_can script, that kills the 7-highlander process.
* 8-beheaded_process - a Bash script that kills the process 7-highlander.