#!/bin/bash

if [ -f .tunnel.env ]; then
	. .tunnel.env
fi

port="$1"
jump_server="$2"

function usage () {
	echo "Invoke as $0 port [jump_host]"
	echo "A SSH tunnel will be created to jump_host on port."
	echo "jump_host can be replaced by creating .tunnel.env"
	echo "or setting the SSH_JUMP_HOST environment variable."
}

if [ "$jump_server" == "" ]; then
	if [ "$SSH_JUMP_HOST" == "" ]; then
		usage
		exit 2
	else
		jump_server="$SSH_JUMP_HOST"
	fi
fi

if [ "$port" == "" ]; then
	usage
	exit 1
fi

ssh -D "$port" "$jump_server"

exit 0
