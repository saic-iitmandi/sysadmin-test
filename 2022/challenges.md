>### Kindly read the guidelines in [**README.md**](https://github.com/saic-iitmandi/sysadmin-test/blob/main/2022/README.md) before proceeding with the challenges.
-----------------------------------------------------
## Challenge 1 - Gain Access to a Remote Server

Since you will be in charge of a public facing server you need to know how to protect a server and in order to protect a server you must first learn how attacks generally work. A drive link containing a SaicVM.ova file is provided to you. This file can be imported into a Virtual Box. When run as guest, it will act as a remote server hosting a site on it's own local host which can be seen on your host localhost. You have to get inside this server by exploiting any vulnerability that you find.

Report your findings and method. You will find the flag once you have gained root privileges.

Use of tools like metasploit is discouraged.

Link: https://drive.google.com/file/d/1DCeI7AQmL9irRW6Ad_j3E2WD8FYVte0o/view?usp=sharing

-----------------------------------------------------
## Challenge 2 - Shell Scripting

One problem almost everyone at IIT Mandi faces almost on a daily basis is that of switching proxies when switching from personal hotspot wifi to institute’s wifi connection. Design a way to automate this on your system, using scripts and anything else you might require. This can include various levels like just configuring system wide proxy through a single command entered manually to automatically detecting when the network is changed and changing proxy appropriately depending on the SSID of the newly connected to network.

Try to generalize your script, so it's portable and can run on other's system without any modifications.

-----------------------------------------------------
## Challenge 3 - Docker Monitoring & Scripting

[**Docker**](https://www.docker.com/resources/what-container/) is one of the most widely used services to _containerize_ applications that must run on the same host system but in independent environments. We also use Docker containers on the SNTC server to deploy each of the clubs' websites. However in case the main program running inside a container exits, the container will also abruptly shut down with it.

Your challenge is to monitor all the Docker containers running on a host system, and identify if a container exits or changes state from normal/running/active. Additionally, your program should then automatically alert us by sending an email to saic@students.iitmandi.ac.in with helpful info such as _Which container? / what program was running inside it? When?_ Optionally even _How did it stop - any error code or traceback?_ etc...<br>
**Send the email with the subject "Sysadmin test 2022 - Challenge 3"**
<br><br>
(**If you are going to test the script a few times, please don't spam this email ID (or anyone else). You can use another personal ID for the test recipient.**)

<details>
  <summary>Notes on Docker [expand]</summary>
  If you have never heard anything about how docker works before, here are 3 questions that may help guide you - <ul>
  <li>What is an <i>Image</i> vs. <i>Container</i> ?</li>
  <li>Virtual Environment (e.g. Python's venv or anaconda) <i>vs.</i> Container (Docker etc..) <i>vs.</i> a Virtual Machine (Oracle VBox, etc...)</li>
  <li>What is a <code>Dockerfile</code> ?</li>
  </ul>
  <p>We aren't asking you to deploy any specific service/container in this problem. You can create your own Docker images of any kind, or even just pull some from the <a href="https://hub.docker.com/search?q=">Docker Hub</a> and run those. Maybe you insert a script that automatically exits after some time, or you can stop the container manually during testing to check if your monitoring script works.</p>
</details>

<details>
  <summary>Notes on Emailing [expand]</summary>
  You will likely need credentials of a <i>trusted</i> SMTP server/relay to send email that will actually be accepted and downloaded to any inbox. You may use any service that is publicly available. There are free accounts on some mailing services that are feasible to create, or even Gmail allows you to use its SMTP relay, with some conditions. <b>Please do not allow your credentials to be leaked or appear in the code at any time, as you will need to make your Git repository public later! They can then be misused by anyone on the internet.</b> You can record a short video of the email script working and being received in your inbox so that we can see the script in action, or, instead document how to provide the credentials so that we can use our own and test it.
</details>


#### Deliverables
- Dockerfiles and relevant associated scripts or description for building the images.
- Email automation script(s)
- Main script(s) to detect changes
- Description of the scheduling/monotoring method you used

-----------------------------------------------------
## Challenge 4 - Docker Deployments
You are given the github repositories of three websites, all of them made using different technologies. You need to set up docker containers for the three websites. The three sites should be running on your localhost through Docker instances. You can use any port of your choice for the three websites. Note that running these websites directly on your system is not expected in this task. You have to set up docker containers for the evaluation.

The websites are provided here: [CP Dashboard](https://github.com/KamandPrompt/CP-Dashboard), [An app of STAC IIT Mandi](https://github.com/STAC-IITMandi/xray-burst-detection), [SAIC IIT Mandi](https://github.com/KamandPrompt/SAIC-Website)

The technologies used in the different websites are ReactJS, Flask and Simple HTML-CSS-JS respectively. The way you set up the docker containers is up to you.

-----------------------------------------------------
## Challenge 5 - Docker & Networking

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
docker logs(`sudo docker logs <image name/id> -f`) or <br>
through access logs(`cat <log file path/location> -f`) (see below task)<br>

3. **Design a custom log file architecture/format for all running docker instances which you feel is best suited for a single server**<br>
Demonstrate it locally using at least two docker instances.<br>
Why is your design preferable to the default one? Justify your answer with respect to both access and error logs.<br>
### [ To demonstrate and test your script(s) you can use [this image(lightweight)](https://hub.docker.com/r/metavinayak/matrix) or [this one(customizable)](https://hub.docker.com/r/metavinayak/matrix-custom) if needed]

#### Deliverables
- Dockerfiles or Docker Compose files
- Video/Screenshots of Load Balancing demonstration
- Video/Screenshot of custom logs demonstration and/or any other scripts used
