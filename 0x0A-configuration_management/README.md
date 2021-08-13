## 0x0A. Configuration management

#### Install `puppet-lint`
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

### Resources
* [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Puppet resource type](https://puppet.com/docs/puppet/3.8/types/file.html)
* [Puppet's Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
* [Puppet lint](http://puppet-lint.com/)
* [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

### Files Descriptions
* `0-create_a_file.pp` - Using Puppet, create a file in `/tmp`. [Tips](https://puppet.com/docs/puppet/3.8/types/file.html)
* `1-install_a_package.pp` - Using Puppet, install `puppet-lint`.  [Tips](https://puppet.com/docs/puppet/5.5/types/package.html)
* `2-execute_a_command.pp` - g Puppet, create a manifest that kills a process named `killmenow`. [Tips](https://puppet.com/docs/puppet/7/types/exec.html#exec-attributes)