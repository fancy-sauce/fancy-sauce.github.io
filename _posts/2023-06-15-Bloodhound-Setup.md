---
layout: post
title: Setting up Bloodhound on Ubuntu 22.04
subtitle: Tools
gh-repo: fancy-sauce/fancy-sauce.github.io
gh-badge: [star, follow]
tags: [bloodhound, tools, linux, ubuntu]
comments: true
---
# Intro

Since most tutorials were mixed up with the process to get Bloodhound installed, which led to breaking apt and gpg keys, I decided to make a note of the process and keep it for reference for anyone else.

I've taken a lot of the steps from:
https://bloodhound.readthedocs.io/en/latest/installation/linux.html#install-neo4j

# Adding keys
---
Run these commands first.

    curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key |sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg

    echo "deb [signed-by=/usr/share/keyrings/neo4j.gpg] https://debian.neo4j.com stable 4.1" | sudo tee -a /etc/apt/sources.list.d/neo4j.list

    sudo add-apt-repository universe

    sudo apt update

Then, you need to stop the service.

    sudo systemctl stop neo4j
Start the neo4j console:

    cd /usr/bin
    sudo ./neo4j console

Check that port 7474 is open:

    netstat -an | grep 7474

navigate to http://127.0.01:7474

![anger](https://github.githubassets.com/images/icons/emoji/unicode/1f4a2.png)If the page isnt loading correctly, make sure your browser didn't rewrite the url to https. If so, change it to http.

Both username and password are **neo4j**

Download the latest ubuntu zip from:
https://github.com/BloodHoundAD/BloodHound/releaseshttps://github.com/BloodHoundAD/BloodHound/releases

Unzip the archive!

---