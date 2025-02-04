<h2>Bus Booking Automation</h2>
<h1> 2 videos attached</h1>

*This was a very much fun question.
*I knew beatufiulSoup earlier and had made many apps in it but it was tough to do such a job with it.
\*But for this task selenium was good and so i used LLM for most of the boilerplate code and i builded over it.

\*Step by step I observed the id's of the button and the form part I have to fill and clicked I navigated through the question

<h4>For selecting the date I had 2 options -<h4>

1.Scrolling through the date form of ajax container which was quiet slow process and very much computation.
I faced some issue in this............as when i picked 30 jan 2025 it picked 30 Dec 2024 as the ajax calender had some entires with id 30 jan....
So,I then used both the id and title for varification that the date is correctly selected

<h6>But later i switched to method 2 for date </h6>

2.Directly using DOM variables to put the date in the place like this -
driver.execute_script(f"document.getElementById('txtFromDate').value = '{formatted_date}';")

I faced many issues in choosing the seat..............I used the logic of iterating through the seats and books the first available first seat

<h5>If the bus is full my code will iterate to the next bus on that time</h5>

After choosing the seat I found the id of submit button and clicked it...

<h5>For security</h5>
*I used .env for security reasons to hide the senstive data.....

<h5>For email</h5>
Used smtplib for email sending and used my own gmail api password for sending it........

<h5>Asking users for the crendentials: </h5>

<img src="Screenshot 2025-01-28 204933.png" alt="Example Image" width="600">

<h5> About scheduling ....... </h5>

<h6> I used the logic if the time difference between the current and the booking date with also consedering the time is more than 15 then program sleeps for that much time and runs then..........cron could have also been used i thought but i sticked with sleep.....</h6>

PS- One other option was schedule library but for this task I felt sleep is a better option as -

1.You are only booking a seat once, at a specific time , not many times for which scheudle is good

2.The sleep function will pause the script until the specified time arrives. During this time, the script isn't consuming any CPU or memory, which makes it efficient, especially if the booking window is far in the future.
but schedule, which requires a continuous loop to check for pending tasks, sleep eliminates unnecessary checks or resource consumption.

Mailing was an easy part for me as I have worked on the mailing thing in one of my earlier projects with nodemailer and it was easy with smtplib even in python.....

The finding of correct elements of id and other tags was the toughest job

<h2> ISSUES IN SCHEDULING </h2>
While I was scheduling , my program was not booking the seats properly...
I issue was maybe I was coming late or early on the booking page....
To counter that I took the alert message from the page..........
If the alert message was "Travel date and time is not as per rule." the program will loop in every 30 seconds and click the submit button and it worked...
(video attached) 
I kept a max limit of 30 loops like 900 seconds 15 mins which can be adjusted easily

<h2>cron job or task schedular could have also been for this task but I simply used time.sleep bcz I am lazy</h2>
