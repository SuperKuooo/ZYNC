# ZYNC
ZYNC is A local network syncing software that zips and transfers folders using TCP connections.

ZYNC is a file transfer system designed to ease Unity develop cycle. Waiting for Unity to build could be sometimes grusome. Normally developers would have to wait for Unity to build, distribute it to other computers (if working on multiplayer), then test it. This process could take from 15 - 30 minutes. ZYNC tries to automate that process and let developers spend time on things they actually like.

Contributions are welcome and I would love to keep updating this software. If you have any suggestions or issues, please let me know.

Jerry Kuo: jerrykuo820@gmail.com

## Installing ZYNC
ZYNC is a file transfer/syncing system that uses TCP connections. This section includes knowledge requirements, installation guide, and some basic troubleshooting.

### What You Need for ZYNC
***HARDWARE***

ZYNC doesn't require a whole lot hardware. You will need a dedciated computer to act as server, if you want to auto Unity build with Jenkins (More on that one day lol), then you need a dedicated computer for server since you can only open one Unity instance at a time. 

The server/client connection relies on local network. Both server computer and client computer need to be able to connect to internet.

***SOFTWARE***

You MUST install Python. ZYNC was developed in Python 3.7 and you can find the link <a href="https://www.python.org/" target="_blank">here</a>.

### Dependencies
ZYNC depends on the following Python extra libraries:

*   Watchdog
*   PyQt5

For more advanced library installation guide, visit <a href="https://pythonhosted.org/watchdog/" target="_blank">Watchdog's</a>
and <a href="https://www.riverbankcomputing.com/static/Docs/PyQt5/" target="_blank">PyQt5's</a> webites

pip install should do the trick for normal users
```shell
pip install --user pyqt5
pip install --user watchdog
```

Then you will need to download the source code folder from the release page. You can uncompressed the folder anywhere you like. Do this on both Server and Client computers. Then, open your terminal, change directory to ZYNC/src/

- For Server computer
```shell
# Run server software
python File\ Transfer\ Server.py
```
- For Client computer
```shell
# Run client software
python File\ Transfer\ Client.py
```
Then everything should be setup! The GUI should be self explanatory! Let me know if there is any problem! Thanks.

## Special Thanks
Special shout out to Juan Aller. He was my supervisor for this position. He taught me a lot on software structure, networking, and Unity. One of the chillest guys I have known! Juan is definetely a genious in Unity and game design.

## Release Information
List of patches and update notes for each release version

### July 26th, 2019
First formal release, Version 1.0.0.
* Stablizes connections between servers and clients.
  * Added size-prefix to each messages send
  * Zips folders and transfer folders at a faster rate
  * Change confirm alive messages to single direction
* New Features
  * Auto unpacks the zip folder
* Bug fixes
* Code optimization
  * Removed unnecessary classes
  * Separated classes into modules
* Documentations

### July 16th, 2019
Intial release with basic functionality.


