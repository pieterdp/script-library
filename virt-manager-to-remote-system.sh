#!/bin/bash

function usage () {
	echo "Invoke as $0 server to connect virt-manager"
	echo "to a remote system running a KVM server."
	echo "Your user must have SSH keys set and be"
	echo "a member of the libvirt group for this"
	echo "to work."
}

server="$1"

if [ "$server" == "" ]; then
	usage
	exit 1
fi

virt-manager -c "qemu+ssh://${server}/system"

exit 0
