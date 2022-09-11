# <img id="top" align="center"  src="./extra/3.png" width=500>  <br><br> SAIC CORE TEAM INDUCTION 2021

>## Task 1 - Gain access to a remote server - 

Since you will be in charge of a public facing server you need to know how to protect a server and in order to protect a server you must first learn how attacks generally work. 
A drive link containing a hackme.ova file is provided to you. This file can be imported into a Virtual Box. When run as guest, it will act as a remote server hosting a site on it's own local host which can be seen on your host localhost. 
You have to get inside this server by exploiting any vulnerability that you find.

Report your findings and method. 

You will find the **key** once you have reached the desired level of privilege( not root ).

Use of tools like metasploit is  **discouraged**.

Drive Link - https://drive.google.com/drive/folders/1BmTg1Cyzq2EIcs2L4Jn0jgrYq4jvBHV4?usp=sharing
### Deliverables - 
* Any kinds of scripts used.
* Information about the tools used. 
* List all the things you learnt from this task.


<br><br>


>## Task 2 - Write a script that takes a target domain/ip as input and performs the following actions

* Scans for all the open ports on the ip address.
* Finds the geographical location of the ip address.
* Finds all the information about the domain pointing to that ip address   (if domain provided). 
* The kind of services hosted by the ip and their status

* Any other important detail that you can extract with an explanation to why it's important.
* This script has to record all these details in a file format(.txt or any other) and send them over mail to the user periodically.

You can use any language you like for the script. But keep in mind that an answer having an excessive use of libraries will always be inferior to a solution using lesser libraries. Also the quality and details of the formated output will be considered.


### Deliverables - 

* The script file.
* Documentation of how the script works.
* A working demo using screenshots or recordings if possible.
* List all the things you learnt from this task.


<br><br>


>## Task 3 - Run multiple sites on the same docker container by mapping different ports on localhost (127.0.0.1) of the host OS.

Your job is to create a docker container on your personal device. Now clone the following site into the container and run them inside that container. Map the ports for the container such that both the sites are up and running on 127.0.0.1(localhost) of your host OS's browser using the mapped ports. 

Then you have to export this docker container in form of an image and upload it as a public image on docker-hub after signing up for a free account. Therefore, **anyone from any part of the world** should be able to download and run your image  with the simple command.
```
docker run <flags> <username>/<image_name>
```
and have the 2 sites running on any 2 available ports.

**Note** - the complete list of commands needs to be submitted along with all the necessary flags and user info.


### Sites to run - 

https://github.com/KamandPrompt/SAIC-Website

https://github.com/KamandPrompt/kamandprompt.github.io


### Deliverables - 
* Commands used.
* List all the things you learnt from this task.


<br><br>


>## Task 4 - Create a script that performs git-auto pull from a remote git repository.
 Your task is to write a script that is able to detect whether a repository has changed on a remote branch. If so, then the script must auto-pull the changes into the local repository's pre-determined branch. 

<b>BONUS MARKS</b> - You need to redeploy/restart the pulled application on the local( for non-static sites this important ). You can do it for any web site involving a backend like django, flask , express etc.

### Deliverables - 

* The script file.
* Documentation of how the script works.
* A working demo using screenshots or recordings if possible.
* List all the things you learnt from this task.

<br><br>
