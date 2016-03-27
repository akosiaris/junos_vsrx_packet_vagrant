# -*- mode: ruby -*-
# vi: set ft=ruby :
# shamelessly stolen from Matt Oswalt.
# http://keepingitclassless.net/2015/03/go-go-gadget-networking-lab/

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "juniper/ffp-12.1X47-D15.4-packetmode"
  config.vm.box_check_update = false

  config.vm.define "vsrx01" do |vsrx01|
    vsrx01.vm.host_name = "vsrx01"
    vsrx01.vm.network "private_network", ip: "192.168.12.11", virtualbox__intnet: "01-to-02"
    vsrx01.vm.network "private_network", ip: "192.168.31.11", virtualbox__intnet: "03-to-01"
  end

  config.vm.define "vsrx02" do |vsrx02|
    vsrx02.vm.host_name = "vsrx02"
    vsrx02.vm.network "private_network", ip: "192.168.23.12", virtualbox__intnet: "02-to-03"
    vsrx02.vm.network "private_network", ip: "192.168.12.12", virtualbox__intnet: "01-to-02"
  end

  config.vm.define "vsrx03" do |vsrx03|
    vsrx03.vm.host_name = "vsrx03"
    vsrx03.vm.network "private_network", ip: "192.168.31.13", virtualbox__intnet: "03-to-01"
    vsrx03.vm.network "private_network", ip: "192.168.23.13", virtualbox__intnet: "02-to-03"
  end

  config.vm.provision "ansible" do |ansible|
      ansible.verbose = "v"
      ansible.playbook = "rip.yaml"
  end
end
