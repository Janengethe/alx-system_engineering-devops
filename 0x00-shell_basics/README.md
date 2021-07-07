## 0x00. Shell, basics
> A shell is a program that takes command from the keyboard and gives them to
> the operating system to perform.
> A terminal is a program that opens a window and lets you interact with the
> shell.

### Resources
* [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)
* [Navigation](http://linuxcommand.org/lc3_lts0020.php)
* [Looking Around](http://linuxcommand.org/lc3_lts0030.php)
* [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
* [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
* [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
* [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
* [Keyboard shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
* [LTS](https://wiki.ubuntu.com/LTS)
* [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)
* [Creating custom mafic file](https://cweiske.de/tagebuch/custom-magic-db.htm)
* Man or Help:
  * `cd`
  * `ls`
  * `pwd`
  * `less`
  * `file`
  * `ln`
  * `cp`
  * `mv`
  * `rm`
  * `mkdir`
  * `type`
  * `which`
  * `help`
  * `man`

### Files Descriptions
* `0-current_working_directory`- a script that prints the absolute path name of the current working directory.
* `1-listit`- a script that display the contents list of your current directory.
* `2-bring_me_home`- a script that changes the working directory to the user’s home directory.
* `3-listfiles`- a script that display the current directory contents in a long format.
* `4-listmorefiles`- a script that display the current directory contents, including hidden files (starting with .). Use the long format.
* `5-listfilesdigitonly`- a script that display the current directory contents: Long format, with user and group IDs displayed numerically, And hidden files (starting with .)
* `6-firstdirectory`- a script that creates a directory named `holberton` in the `/tmp/` directory.
* `7-movethatfile`- a script that Move the file `betty` from `/tmp/` to `/tmp/holberton`.
* `8-firstdelete`- a script that Delete the file `betty`.
* `9-firstdirdeletion`- a script that Delete the directory `holberton` that is in the `/tmp` directory.
* `10-back`- a script that changes the working directory to the previous one.
* `11-lists`- a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.
* `12-file_type`- a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script.
* `13-symbolic_link`- Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.
* `14-copy_html`- a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
* `15-lets_move`- a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
* `16-clean_emacs`- a script that deletes all files in the current working directory that end with the character `~`.
* `17-tree`- a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/holberton` in the current directory.
* `18-commas`- a command that lists all the files and directories of the current directory, separated by commas (`,`).
* `holberton.mgc`- Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.