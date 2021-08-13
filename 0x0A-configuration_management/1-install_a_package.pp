# script to install puppet-lint using puppet

package {'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem'
}