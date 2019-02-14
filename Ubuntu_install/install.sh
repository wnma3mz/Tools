# install first
sudo apt -y upgrade
sudo apt update
sudo apt install -y vim ssh python-pip python3-pip ipython3 tree mycli axel autossh git
pip3 install numpy virtualenv bs4 requests pandas sklearn keras 


# install docker
curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://nruk9663.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

# install docker images
sudo docker pull mysql
sudo docker pull nginx


