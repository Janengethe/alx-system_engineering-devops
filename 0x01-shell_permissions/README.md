## 0x01. Shell, permissions
> This project entails the shell builtin commands, and the permissions that are
> ussually granted to files and directories.
> These permissions allows access rights for reading, writing and executing by
> the owner, group or others.

### Resources
* [Permissions](http://linuxcommand.org/lc3_lts0090.php)
* [Watching StarWars IV episode](https://www.commandlinefu.com/commands/view/7251/play-star-wars-episode-iv-in-your-terminal-) on the terminal.
* Man/Help:
  * `chmod`
  * `sudo`
  * `su`
  * `chown`
  * `chgrp`
  * `id`
  * `groups`
  * `whoami`
  * `adduser`
  * `useradd`
  * `addgroup`

### Files Descriptions
* `0-iam_betty`- a script that switches the current user to the user `betty`.
* `1-who_am_i`- a script that prints the effective username of the current user.
* `2-groups`- a script that prints all the groups the current user is part of.
* `3-new_owner`- a script that changes the owner of the file `hello` to the user `betty`.
* `4-empty`- a script that creates an empty file called `hello`.
* `5-execute`-  a script that adds execute permission to the owner of the file hello.
* `6-multiple_permissions`- a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`.
* `7-everybody`- a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
* `8-James_Bond`- a script that sets the permission to the file hello as follows: Owner: no permission at all, Group: no permission at all,Other users: all the permissions.
* `9-John_Doe`- a script that sets the mode of the file hello to this:
```
-rwxr-x-wx 1
```
* `10-mirror_permissions`- a script that sets the mode of the file `hello` the same as `olleh`’s mode.
* `11-directories_permissions`- a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
* `12-directory_permissions`- a script that creates a directory called `dir_holberton` with permissions 751 in the working directory.
* `13-change_group`- a script that changes the group owner to `holberton` for the file `hello`
* `14-change_owner_and_group`- a script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.
* `15-symbolic_link_permissions`- a script that changes the owner and the group owner of `_hello` to `betty` and `holberton` respectively.
* `16-if_only`- a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
* `103-Star_Wars`- a script that will play the StarWars IV episode in the terminal.