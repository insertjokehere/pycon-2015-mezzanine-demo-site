# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
  end

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.provision "puppet"

  # If vagrant-cachier is installed, persist the apt and pip caches
  # vagrant plugin install vagrant-cachier
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box

    config.cache.enable :generic, {
                          "pip" => { cache_dir: "/home/vagrant/.cache/pip" },
    }
  end
end
