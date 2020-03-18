#!/bin/bash

# create N keys
for i in 0 1 2 3
do
	ssh-keygen -f k$i
done

#append them to authorized
cat ~/.ssh/authorized_keys k0.pub k1.pub k2.pub k3.pub > authorized_keys

#create config

#disseminate to all nodes
for i in 0 1 2 3
do
	cat k$i | sudo ssh n$i "cat > /users/abdffsm/.ssh/key"
	cat k$i.pub | sudo ssh n$i "cat > /users/abdffsm/.ssh/key.pub"
	cat authorized_keys | sudo ssh n$i "cat > /users/abdffsm/.ssh/authorized_keys"
	cat config | sudo ssh n$i "cat > /users/abdffsm/.ssh/config"
done
