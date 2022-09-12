>### Kindly read the guidelines in **README.md** before proceeding with the challenges.
## Challenge 1

-----------------------------------------------------
## Challenge 2

-----------------------------------------------------
## Challenge 3

-----------------------------------------------------
## Challenge 4 - Docker & Networking

Hi there!<br>
In this challenge you have to perform/write scripts for the tasks below:<br>
1. Have you heard about **Docker Hub**?<br>
In this challenge, you have to first **automate docker image deployments** using the image id(s) on [**Docker Hub**](https://hub.docker.com/search?q=).<br>
Then add the below functionalities.

2. **Perform load balancing using multiple instances of the same docker image.**<br>
You can take the number of instances to be **3**.Bonus points for generalizing :)<br>
Load balancing must be such that when you locally request a particular domain multiple times, the requests get distributed uniformly across the docker instances.<br>
Test this load balancing by sending multiple requests using curl or some other tool.<br>
You can either demonstrate it using docker-compose output or <br>
docker logs("sudo docker logs <image name/id> -f") or <br>
through access logs("cat <log file path/location> -f") in the below task<br>

3. **Design a custom log file architecture for all running docker instances which you feel is best suited for a single server**<br>
Demonstrate it locally using at least two docker instances.<br>
Why is your design preferable to the default log file architecture? Justify your answer with respect to both access and error logs.<br>
### [ To demonstrate and test your script(s) you can use [this image(lightweight)](https://hub.docker.com/r/metavinayak/matrix) or [this one(customizable)](https://hub.docker.com/r/metavinayak/matrix-custom)]

-----------------------------------------------------
## Challenge 5