#!/bin/bash

for i in 1 2 3
do
ssh n$i sudo rm -r ~/tensorflow_setup
done

#git clone https://github.cs.tufts.edu/abdullah/tensorflow_setup.git

for i in 1 2 3
do
ssh n$i scp -r abdffsm@n0:~/tensorflow_setup .
done



