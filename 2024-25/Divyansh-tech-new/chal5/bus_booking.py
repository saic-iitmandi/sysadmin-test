import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from datetime import timedelta

import smtplib
from selenium.webdriver.common.alert import Alert
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from datetime import datetime
# import emailjs

load_dotenv()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os


load_dotenv()
BOOKING_DATE=0
BOOKING_TIME=0

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")  
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  
SENDER_PASSWORD =   os.getenv("SENDER_PASSWORD")
  

def send_email_notification(driver,details):
    """
    Send a notification email using SMTP upon successful booking.
    """
    try:
        
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = RECIPIENT_EMAIL
        message["Subject"] = "Bus Booking Confirmation"
        global BOOKING_TIME
        global BOOKING_DATE
       
        body = f"""
        <html>
        <body>
        <h2>Booking Successful!</h2>
        <p><strong>Details:</strong></p>
        <ul>
            <li><strong>Username:</strong> {USERNAME}</li>
            
            <li><strong>Seat:</strong> Your seat is succesfully booked </li>
            <li><strong>Date:</strong> {BOOKING_DATE} </li>
        </ul>
        </body>
        </html>
        """
        message.attach(MIMEText(body, "html"))
        #SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())

        print("Email notification sent successfully.")
        

    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
    # Quit the driver here only after the process is done
        driver.quit()
        print("Driver closed.")

USERNAME = "b24122"
PASSWORD = os.getenv("PASSWORD")
RECIPIENT_EMAIL = USERNAME+"@students.iitmandi.ac.in"

BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"



def get_user_inputs():
    """
    Get user inputs for path, date, and timing.
    """
    print("Select a path for the bus:")
    print("1. North Campus -To- Mandi (via South)")
    print("2. Mandi -To- North Campus (via South)")
    print("3. North Campus -To- Mandi (Direct)")

    path_choice = int(input("Enter the option number (1/2/3): "))
    if path_choice == 1:
        path_value = "1"
    elif path_choice == 2:
        path_value = "2"
    elif path_choice == 3:
        path_value = "7"
    else:
        raise ValueError("Invalid path option selected.")

    booking_date = input("Enter the booking date (YYYY-MM-DD): ")
    timing = input("Enter the timing: ")

    return path_value, booking_date, timing


def set_date_via_script(driver, target_date):
    """
    Set the date directly using JavaScript on the input field with the format: day/month/year
    """
    try:
        # Format the target date in the required format
        target_date_obj = datetime.strptime(target_date, "%Y-%m-%d")
        formatted_date = target_date_obj.strftime("%d/%m/%Y")
        global BOOKING_DATE
        BOOKING_DATE = formatted_date
        # Execute the JavaScript to set the value directly in the input field
        driver.execute_script(f"document.getElementById('txtFromDate').value = '{formatted_date}';")
        print(f"Date set directly to {formatted_date}.")
    except Exception as e:
        print(f"Error setting the date: {e}")


def select_bus_and_check_seats(driver, path_value, timing):
    """
    Automates the process of selecting a bus, checking for available seats, and switching to the next bus if no seat is found.
    """
    try:
        # Wait
        bus_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ddlBus"))
        )
        select_bus = Select(bus_dropdown)
        
        # Get all bus
        buses = select_bus.options
        found_seat = False  # To track whether a seat is found

        for bus_option in buses:
            bus_value = bus_option.get_attribute("value")
            
            if bus_value != "Select":  
                
                bus_dropdown = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ddlBus"))
                )
                select_bus = Select(bus_dropdown) 
                select_bus.select_by_value(bus_value)
                print(f"Bus selected: {bus_option.text}")
                time.sleep(3)  #some sleep to load

               
                seat_available = check_seats(driver)
                if seat_available:
                    found_seat = True  # Mark as seat found
                    print(f"Seat found on {bus_option.text}!")
                    break 
                else:
                    print(f"No seats available on {bus_option.text}. Trying next bus...")
                    time.sleep(2) 
                    continue  
        if not found_seat:
            print("No seats found on any of the buses.")
    except Exception as e:
        print(f"Error during bus seat selection: {e}")

def select_first_available_seat(driver, seats):
    """
    Select the first available seat from the available checkboxes and submit the booking.
    """
    try:
        if seats:
            first_seat = seats[0]
            ActionChains(driver).move_to_element(first_seat).click().perform()
            seat_id = first_seat.text
            print(f"Seat {seat_id} selected.")

            save_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "lnkSave"))
            )
            
            max_attempts = 30
            attempts = 0

            while attempts < max_attempts:
                save_button.click()  # Submit the booking
                
                print("Submit button clicked. Booking is being processed.")
                
                try:
                    # Wait for the alert to appear after the booking is done
                    alert = WebDriverWait(driver, 10).until(
                        EC.alert_is_present()
                    )
                    alert_text = alert.text  # Get the text of the alert
                    print(f"Alert text: {alert_text}")
                    
                    if "Travel date and time is not as per rule" in alert_text:
                        # If the alert indicates the travel date and time is incorrect, wait 30 seconds
                        print("Travel date and time is not as per rule. Sleeping for 30 seconds...")
                        time.sleep(30)
                        attempts += 1  # Increment the attempt counter
                        alert.accept()  # Accept the alert
                        continue  # Continue with the loop for next attempt
                    elif "Selected seat successfully booked" in alert_text:
                        print("Booking successful! Seat successfully booked.")
                        alert.accept()  # Accept the alert and break the loop
                        break  # Exit the loop when booking is successful
                    else:
                        print("Unknown alert. Exiting.")
                        alert.accept()
                        break  # If it's an unexpected alert, break out of the loop
                except Exception as e:
                    print(f"Error during alert handling: {e}")
                    break  # If there's any error, break out of the loop

            if attempts >= max_attempts:
                print("Max attempts reached. Could not book the seat.")
                driver.quit()
                return

            driver.quit()
            print("Booking submitted. Exiting the program...")

            send_email_notification(driver,f"Seat {seat_id} successfully booked!")

        else:
            print("No available seats to select.")
    except Exception as e:
        print(f"Error selecting seat or submitting booking: {e}")


def check_seats(driver):
    """
    Checks if a seat is available on the current bus.
    """
    try:
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@type, 'checkbox') and not(@disabled)]"))
        )

       
        seats = driver.find_elements(By.XPATH, "//input[contains(@type, 'checkbox') and not(@disabled)]")  # Adjust XPath
        if seats:
            print(f"{len(seats)} seats available.")
          
            select_first_available_seat(driver, seats)
            return True
        else:
            print("No seats available.")
            return False
    except Exception as e:
        print(f"Error while checking seats: {e}")
        return False



def book_bus_seat():
    """
    Automates the bus seat booking process.
    """
    
    path_value, booking_date, timing = get_user_inputs()

   
    target_time = datetime.strptime(timing, "%I:%M %p").time()  # Convert timing to a time object
    target_date_obj = datetime.strptime(booking_date, "%Y-%m-%d").replace(
        hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0
    )

  
    current_date_obj = datetime.now()

   
    delta = target_date_obj - current_date_obj

  
    booking_start_time = target_date_obj - timedelta(days=15)

    
    sleep_duration = (booking_start_time - current_date_obj).total_seconds()

    if sleep_duration > 0:
       
        print(f"Booking window not open yet. Sleeping for {sleep_duration / 3600:.2f} hours.")
        time.sleep(sleep_duration)
        print("Waking up to start the booking process.")
        # time.sleep(20)
    else:
        
        print("Booking window is already open. Proceeding with the booking process.")

    # Set up Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the booking URL
        driver.get(BOOKING_URL)
        print("Opened the booking page.")

        # Login to the system
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "txtLoginId"))
        ).send_keys(USERNAME)
        print("Username entered.")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "txtPassword"))
        ).send_keys(PASSWORD)
        print("Password entered.")

        driver.find_element(By.ID, "btnLogin").click()
        print("Login button clicked.")
        time.sleep(2) 

        driver.get(BOOKING_URL)

        set_date_via_script(driver, booking_date)

        
        route_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ddlRoute"))
        )
        select_route = Select(route_dropdown)
        select_route.select_by_value(path_value)
        print(f"Route selected: {path_value}")
        time.sleep(3) 
        
        timing_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ddlTiming"))
        )
        select_timing = Select(timing_dropdown)
        select_timing.select_by_visible_text(timing)
        print(f"Timing selected: {timing}")
        time.sleep(3)  

        
        select_bus_and_check_seats(driver, path_value, timing)

    except Exception as e:
        print("Error during booking:", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    book_bus_seat()
