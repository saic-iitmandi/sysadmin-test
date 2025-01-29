<h1> It was quiet a fun question which felt like hacking</h1>

<h6>Mostly i used llm for coding part , but faced many issues</h6>

I researched and found that their is something like task schedular which can be used.

2 ways to do this manually and by automated task creation.......i used the automated one

I made the python script for finding the lol folder and copying if it exists.....

Also the upload to cloud took too much of my time and at last i did to google drive with google developer api which i was quiet familar to use with.....i removed the creds ofc

<h2>Now about the problems i faced........</h2>

I was first using the way to manually add task to task schdular but then i found a way to make a task if the script is ran once

<h3>So my idea was the user can be made to run the script once through many ways (with admin rights)  after that the script will be a part of on startup task schedular and every time the user startsup the task will run........</h3>

the script can also be put in some system critical files maybe C:\Windows\System32 also for preveliges and stelth...

I was using with run with highest prevliges which was causing issues so i made my python script to remove that from task_schedular

Other issue I faced was that when it was running the console was also opening which could lead the user to know that the program is running.............SO i researched and found that changing python.exe to pythonw.exe runs the code without showing and terminal.........

<h4>Ideally I should have made that file after copying in some hidden folder in some remote directory but for testing purposes and its just a prototype i kept it in the desktop only /h4>

The script also Perfectly checks if the file lol exists or not and does not copy unecessary files

You can find the screen shots and log files in the SystemUpdater file
