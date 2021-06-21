## 0x04. Loops, conditions and parsing

### Reference Materials
* [Loop Samples](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
* [Variable assignment and arithmetic](https://tldp.org/LDP/abs/html/ops.html)
* [Comparison Operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
* [File Test Operators](https://tldp.org/LDP/abs/html/fto.html)
* [Make your Script Portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)
* Man/Help -> env, cut, for, while, until, if


### [Shellcheck](https://github.com/koalaman/shellcheck)
* Shellcheck is a tool that help in writing proper Bash scripts. It make recommendations on syntax and semantics and provide advice on edge cases. Shellcheck is friendly! All Bash scripts must pass Shellcheck without any error.
* Shellcheck is available on the school's computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

### File Descriptions
* 0-RSA_public_key.pub - contains my public key. Resources for this task: a). [Linux and Mac OS users](https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys), b). [Windows Users](https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/), c). man:ssh-keygen.
* 1-for_holberton_school - a Bash script that displays Holberton School 10 times using for loop.
* 2-while_holberton_school - a Bash script that displays Holberton School 10 times using while loop.
* 3-until_holberton_school - a Bash script that displays Holberton School 10 times using until loop.
* 4-if_9_say_hi - a Bash script that displays Holberton School 10 times, but for the 9th iteration, displays Holberton School and then Hi on a new line.
* 5-4_bad_luck_8_is_your_chance - a Bash script that loops from 1 to 10 and: displays bad luck for the 4th loop iteration, displays good luck for the 8th loop iteration, displays Holberton School for the other iterations.
* 6-superstitious_numbers - a Bash script that displays numbers from 1 to 20 and: displays 4 and then bad luck from China for the 4th loop iteration, displays 9 and then bad luck from Japan for the 9th loop iteration, displays 17 and then bad luck from Italy for the 17th loop iteration.
* 7-clock -  a Bash script that displays the time for 12 hours and 59 minutes: display hours from 0 to 12, display minutes from 1 to 59.
* 8-for_ls - displays: The content of the current directory, In a list format, Where only the part of the name after the first dash is displayed.
* 9-to_file_or_not_to_file - a Bash script that gives you information about the holbertonschool file.
* 10-fizzbuzz - a Bash script that displays numbers from 1 to 100.
* 100-read_and_cut - a Bash script that displays the content of the file /etc/passwd. The script only display: username, user id, Home directory path for the user.
