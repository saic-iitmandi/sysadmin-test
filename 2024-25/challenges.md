# SysAmin Test 2024-25 Challenges

## **Challenge 1 - Gain Access to a Remote**

Since you will be in charge of a public-facing server you need to know how to protect a server and to protect a server you must first learn how attacks generally work. A drive link containing a saic.ova file is provided to you. This file can be imported into a Virtual Box. When run as a guest, it will act as a remote server hosting a site on it's own local host which can be seen on your host's localhost. You have to get inside this server by exploiting any vulnerability that you find.

Report your findings and method. You will find the flag once you have gained root privileges.

Use of tools like Metasploit is discouraged.

Drive link for the Virtual Machine: [Here](https://drive.google.com/file/d/10zpkNrp7xP7zOx45rGxxnu9nvz5P-OiH/view?usp=sharing)

### **Deliverables**

In your git repository whose link you will be submitting, state your approach for finding the flag along with screenshots of the process.

**Note**: Accessing the mounted disk from outside the VM environment is strictly prohibited.

## **Challenge 2 - Docker Scripting**

Create a script to automate the backup and restore process for Docker volumes and containerized services.

### **Requirements**

The script should:

1. **Backup Process**:

   - Backup the data from all Docker volumes used by containers, specifically targeting application data stored in Docker mounts.
   - Create a compressed archive named with a timestamp for each volume.
   - Ensure the backup process does not interrupt running containers.

2. **Restore Process**:

   - Include an option to restore data from the latest backup for specific Docker volumes or all volumes.
   - Ensure restored data is properly re-mounted to the relevant containers.

### **Bonus**

Use a cron job to schedule the script to run daily at midnight.

### **Deliverables**

1. The script file.
2. A sample log output for both backup and restore operations.
3. Instructions for:
   - Running the backup and restore script.
   - Testing the functionality with a sample Docker setup.
   - Setting up the scheduled cron job.

## **Challenge 3 - Docker Deployments**

You are provided with GitHub repositories for two different projects. Your task is to deploy both projects using Docker containers on your localhost. Each project uses a different technology stack, so you must configure and deploy them accordingly.

### **Repositories**

1. [Nutrient-Tracker](https://github.com/aaltamirano1/Nutrient-Tracker) - A Ruby on Rails project.
2. [TIP](https://github.com/sntc-tech/TIP) - A Next.js project.

### **Tasks**

1. **Deploy Both Projects Using Docker Compose**
   - Create Docker containers for both projects and configure them using a `docker-compose.yml` file.
   - Map each container to ports of your choice on your localhost.
2. **Network Configuration**
   - Suggest appropriate Docker network types (e.g., `bridge`, `host`, or `overlay`) for each container.
   - Justify your choice of network for each container.

### **Deliverables**

- A brief document explaining the setup process for hosting both projects.
- Dockerfiles for both projects.
- The `docker-compose.yml` script.
- Provide screenshots of:
  - Running containers (`docker ps`).
  - Accessing both websites in the browser.

## Question 4 - Dockerizing a fullstack app (frontend+backend)

You are tasked with setting up a fullstack application consisting of a frontend and backend. The goal is to containerize the entire application using Docker to ensure seamless deployment and scalability.

**Repository Link:** [Fullstack App](https://github.com/Rimurudemon/q4_sysadmin/tree/main/q4)

As part of the hosting process, you are required to implement stringent security measures to protect the application and its database. Specifically, the database must not be accessible from outside the host environment under any circumstances. Additionally, even the host server itself should not have direct access to the database, ensuring it can only be accessed by the backend service.

### Your solution should include

1. Steps for containerizing the frontend and backend applications.
2. Configuration of a secure network for communication between containers.
3. Hosting details, including any necessary changes to the Docker Compose setup or infrastructure to achieve the stated security goals.
4. Any best practices for securing the database and preventing unauthorized access.
5. Document the process thoroughly, ensuring that the solution is both functional and adheres to modern security standards for web applications.

## **Challenge 5 - Bus Booking Automation**

### **Problem Statement:**

The bus booking system for IIT Mandi opens its booking for seats based on a specific time and path. Your task is to write a script that automates the booking process as soon as the booking opens.

The system requires that you input a particular date and time for when bookings open, along with a specific path for the bus service. The goal is to have your script automatically book a seat on the bus once the booking opens.

### **Requirements:**

1. **Automated Booking:**
   - The script should be able to monitor the booking website.
   - Once the booking window opens, it should automatically select the desired path and book a seat for you.
2. **Parameters for Booking:**
   - The script should take the following inputs:
     - Date and time when the booking opens.
     - Bus path (this will be pre-defined for you to choose).
3. **Avoid Polling:**
   - Do not continuously poll the site to check for the booking window. Instead, use an efficient way (like a scheduled task or wait mechanism) to trigger the booking process at the exact time when bookings open.
4. **Security:**
   - You should avoid saving sensitive data such as credentials or passwords in plain text. Make sure to use environment variables or a secure method to handle authentication.
5. **Notifications:**
   - Once the booking is successful, you should send a confirmation email to your email address with details of the bus, time, and booking status.

### **Example Input:**

- **Date:** 2025-01-20
- **Time:** 10:00 AM
- **Path:** from north campus to mandi via south

### **Expected Output:**

- Automated seat booking confirmation for the specified path and time.
- Email notification with booking details.

### **Deliverables:**

1. **Script:** The code that automates the bus booking process.
2. **Approach:** Explain how your solution works, including how you avoid polling and handle the booking task at the precise time.
3. **(Optional but recommended) Demo/Video:** Show a demo of the automation in action, including a successful booking.

**Note:** The provided link to the booking system is:  
[Bus Seat Reservation](https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx)

## **BONUS CHALLENGE:**

**Environment:**

Solutions will be tested on a Windows 10/11 machine (the version is the candidate's choice).

Assume administrative privileges are granted for the script's deployment.

**Task:**

Create a Python script that fulfils the following requirements:

**Persistence:**

1. The script should run as a background service (daemon) and start automatically whenever the system is powered on or rebooted.
2. It must remain entirely hidden from the user to ensure stealth. Any user-noticeable signs, such as visible prompts, error messages, or foreground activity, will be considered a failure. While it may appear in the background (e.g., Task Manager or Services list), candidates should use innovative approaches to minimize suspicion.

**Functionality:**

1. The script should monitor for external drives connected to the system. It should activate only when an external drive is connected.
2. When an external drive is detected:

- Check for the folder named "lol":
  If it exists, copy its contents (size guaranteed to be less than 100MB) to a specific location on the local machine.

  Upload the copied contents to a location on the internet from which the folder can later be accessed by the Red Team. (Note: It is not mandatory to upload to a popular cloud service like Google Drive or OneDrive.)

  - Regardless of whether the "lol" folder exists, create or update a log file containing a prioritized list of the major files and folders on the drive. Use the format:

  - {Drive name}: file1, file2, folder1, folder2, etc.

  - Prioritization: Place folder names first, followed by the names of the largest files in the drive. Ensure that the log file is updated each time an external drive is connected.

Store this log file in the same online location as the copied folder (if applicable).

**Constraints**:

1. You do not know in advance which external drive will have the folder "lol", so the script should check each drive when connected.
2. The entire operation must be stealthy, avoiding any obvious signs of activity that could draw user suspicion.

**Important Note:**

1. The solution to this problem might not exist or may be infeasible due to ethical, technical, or environmental constraints. However, the primary focus of this challenge is on understanding the examinee's thought process, problem-solving approach, and ability to identify and address challenges.
2. Examinees are required to document the challenges ("walls") they encounter while attempting to meet the requirements and explain how they attempted to overcome them. Even theoretical or partial solutions will be accepted if they are accompanied by a clear and well-reasoned thought process.

**Evaluation Criteria:**

1. Feasibility: While the solution may not be fully implementable, candidates must demonstrate their thought process in attempting to meet the requirements.
2. Problem-Solving: The candidate's ability to identify potential limitations, propose solutions, and explain their reasoning will be a significant part of the evaluation.
3. Scoring: Depth of understanding, creativity in addressing constraints, and thoroughness of the provided explanations will determine the score.

**Assumptions:**

1. The folder size is guaranteed to be less than 100MB.
2. Access credentials or configuration for the online location (if required) are pre-configured and do not need to be set up by the candidate.

**Note:**

1. Ensure to document your assumptions and design choices thoroughly.
2. Be prepared to discuss the reasoning behind your solution, the limitations you encountered, and the steps you took to address them.

**Important:**

This is a simulated exercise for assessing problem-solving and scriptwriting skills. The solution will not be deployed for malicious purposes. Please provide explanations alongside your code to demonstrate your understanding of the task and constraints.
