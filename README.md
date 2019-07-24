# ZYNC
A local network syncing software that transfers zipped folders using TCP connections.

## Introduction to ZYNC
ZYNC is a file transfer system designed to ease Unity develop cycle. ZYNC Server detects local file changes in the target directories, zips the folder, and transfer to ZYNC clients. 

### Why Was ZYNC Needed
The studio I interned for, Antiloop, is a virtual reality (VR) experience developing company. While I interned there, I noticed that other developers often wait for 10 - 15 minutes for each Unity build and spend another 10 - 15 minutes to distribute the VR experience to individual computers. I wanted to reduce the time thus improve the studio's efficiency, so I developed that auto-syncs the files between computers.

### Who ZYNC is For
ZYNC was first made for Unity developer, yet it is suitable for anyone looking for auto  local file syncing solution, then ZYNC is for you. 

## Getting Started
ZYNC is a file transfer/syncing system that uses TCP connections. This section includes knowledge requirements, installation guide, and some basic troubleshooting.

### What You Need for ZYNC
***HARDWARE***

Not a whole lot to be honest. If you want to auto build with Jenkins (More on that one day lol), then you need a dedicated computer for server since you can only open one Unity instance at a time. You could probably use virtual box for such server, but at the studio I interned for, they had extra laptops sitting around so I just used one of them.

***SOFTWARE***

You MUST install Python. ZYNC was developed in Python 3.7 and you can find the link <a href="https://www.python.org/" target="_blank">`here</a>.

### Installing ZYNC on Your Computers
Once Python is installed, you will then need to install some python modules. The procedures are same for all operating systems.

We need PtQt5 and watchdog modules, so open terminal (command prompt) and type the following commands.
```shell
pip3 install pyqt5
pip3 install watchdog
```
Then you will need to download the source code folder from the release page. You can uncompressed the folder anywhere you like. Do this on both Server and Client computers. Then, open your terminal, change directory to ZYNC/src/

- For Server computer
```shell
cd Server
python File\ Transfer\ Server.py
```
- For Client computer
```shell
cd Client
python File\ Transfer\ Client.py
```
Then everything should be setup! The GUI should be self explanatory! Let me know if there is any problem! Thanks.



