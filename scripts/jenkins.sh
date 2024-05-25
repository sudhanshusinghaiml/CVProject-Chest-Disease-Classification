#!bin/bash

# Update Ubuntu Server with latest package
sudo apt update

# Prerequisite for Jenkisn Installation

## Commands to install Jaava.
sudo apt install openjdk-8-jdk -y

## https://pkg.jenkins.io/
## https://pkg.jenkins.io/debian-stable/

## This is the Debian package repository of Jenkins to automate installation and upgrade.
## To use this repository, first add the key to your system (for the Weekly Release Line):
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key

## Then add a Jenkins apt repository entry:
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null


## Update your local package index, then finally install Jenkins:
sudo apt-get update
sudo apt-get install fontconfig openjdk-17-jre
sudo apt-get install jenkins


## Start the jenkins server
sudo systemctl start jenkins

## Enable the jenkins server
sudo systemctl enable jenkins

## Check the status of the jenkins server
sudo systemctl status jenkins


# Commands to install Docker

## Installing Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker $USER
sudo usermod -aG docker jenkins
newgrp docker


## Installing AWSCLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install zip -y
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update

sudo usermod -a -G docker jenkins


## AWS configuration & restarts jenkins
aws configure


## Now setup elastic IP on AWS


## Command for getting the admin password for jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
