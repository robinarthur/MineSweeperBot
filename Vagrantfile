# -*- mode: ruby -*-

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  config.ssh.forward_x11 = true
  config.vm.provision :shell, path: "provisioning/bootstrap.sh", privileged: false
end
