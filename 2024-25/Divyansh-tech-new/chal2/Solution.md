<h1>Docker Backup and Restore</h1>

I used WSL UBUNTU for this Challenge

<hr>
<p>I MESSED UP A LITTLE BIT DIDN'T MAKE THE .log FILE AND HAD TO DO EVERYTHING FROM START</p>
<hr>

<h2>Steps I Followed:</h2>

<img src="Screenshot (97).png" alt="Example Image" width="600">
<img src="Screenshot 2025-01-26 133345.png" alt="Example Image" width="600">

<p> I first installed docker in ubuntu with wsl. Then I made a work directory where I will complete challenge 2.

Then I created a docker container, volumne . I used Buzybox to make a lightweight container. Then i created a sample file in volume with echo "hello" with sample.txt file. In this step i used Hello, Backup!" > /data/sample.txt where ! was giving some issues where i had to use escape sequence.I faced also many issues where I used chatgpt and asked for further steps.I manual backup using a temporary container. Then i made a backup script and made it a part of the repo and tested the script and it worked quiet well.I then removed the volume but realised that i need to stop the docker container first before removing it after getting a big error.I then deleted the volume and restored it manually. Then I restored it using using a script which became automated.

I tested it on some containers and then added the cron job to schedule the backup at midnight and checked the cron code and also the functionality at midnight.....I realized that i didn't had a log file in my script to store the progress made the necessary changes in the script using llm and did everything again....Everything seems good.On each test the same thing "Hello ,Backup" was echoed......

</p>
