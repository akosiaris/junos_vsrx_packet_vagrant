Introduction
============

Presentation material on how to setup a vagrant env with 3 junos VMs and provision
them using ansible.

Using
=====

Get a debian stretch system and

        apt-get install python-ncclient python-junos-eznc ansible
        git submodule update --init
        vagrant up
