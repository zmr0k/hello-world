# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
HISTSIZE=999999
HISTFILESIZE=99999999

alias ssh='ssh -l vklaniuk -o "ConnectTimeout 3" -o "StrictHostKeyChecking no"'
alias nc='nc -v -w5'
alias python=python2.7
alias findg='find / \( -path /proc -or -path /sys \) -prune -o'

#export DOCKER_HOST=localhost:2375

PS1='\t \[\033[01;32m\]@\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
# PS1='\t @\H: \[\033[01;32m\]@\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

export DOCKER_HOST=tcp://localhost:2375
unset DOCKER_HOST
export WORKON_HOME="/home/zmr0k/.virtualenvs"
