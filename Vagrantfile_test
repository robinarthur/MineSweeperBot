# -*- mode: ruby -*-

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end

  config.ssh.forward_x11 = true
  # config.vm.provision :shell, path: "provisioning/bootstrap.sh", privileged: false
  config.vm.synced_folder "c:/Users/CKr/Documents/GitHub/MineSweeperBot", "/home/vagrant/"
end
