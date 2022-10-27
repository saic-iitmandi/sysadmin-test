>### Kindly read the guidelines in **README.md** before proceeding with the challenges.
## Challenge 1

-----------------------------------------------------
## Challenge 2

-----------------------------------------------------
## Challenge 3 - Gain Access to a Remote Server

Since you will be in charge of a public facing server you need to know how to protect a server and in order to protect a server you must first learn how attacks generally work. A drive link containing a SaicVM.ova file is provided to you. This file can be imported into a Virtual Box. When run as guest, it will act as a remote server hosting a site on it's own local host which can be seen on your host localhost. You have to get inside this server by exploiting any vulnerability that you find.

Report your findings and method. You will find the flag once you have gained root privileges.

Use of tools like metasploit is discouraged.

Link: https://drive.google.com/file/d/1DCeI7AQmL9irRW6Ad_j3E2WD8FYVte0o/view?usp=sharing

-----------------------------------------------------
## Challenge 4 - Docker & Networking

Hi there!<br>
In this challenge you have to perform/write scripts for the tasks below:<br>
1. Have you heard about **Docker Hub**?<br>
In this challenge, you have to first **automate docker image deployments** using the image id(s) on [**Docker Hub**](https://hub.docker.com/search?q=).<br>
Then add the below functionalities.

2. **Perform load balancing using multiple instances of the same docker image.**<br>
You can take the number of instances to be **3**.Bonus points for generalizing :)<br>
Load balancing must be such that when you locally request a particular domain/URL multiple times, the requests get distributed uniformly across the docker instances.<br>
Test this load balancing by sending multiple requests using curl or some other tool.<br>
You can either demonstrate it using docker-compose output or <br>
docker logs("sudo docker logs <image name/id> -f") or <br>
through access logs("cat <log file path/location> -f") (see below task)<br>

3. **Design a custom log file architecture/format for all running docker instances which you feel is best suited for a single server**<br>
Demonstrate it locally using at least two docker instances.<br>
Why is your design preferable to the default one? Justify your answer with respect to both access and error logs.<br>
### [ To demonstrate and test your script(s) you can use [this image(lightweight)](https://hub.docker.com/r/metavinayak/matrix) or [this one(customizable)](https://hub.docker.com/r/metavinayak/matrix-custom)]

-----------------------------------------------------
## Challenge 5 - Shell Scripting

One problem almost everyone at IIT Mandi faces almost on a daily basis is that of switching proxies when switching from personal hotspot wifi to institute’s wifi connection. Design a way to automate this on your system, using scripts and anything else you might require. This can include various levels like just configuring system wide proxy through a single command entered manually to automatically detecting when the network is changed and changing proxy appropriately depending on the SSID of the newly connected to network.

Try to generalize your script, so it's portable and can run on other's system without any modifications.
