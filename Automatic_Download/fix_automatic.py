from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
from datetime import datetime
import pandas as pd

# === Set your download directory ===
download_dir = "/home/diego/Premier-Analysis/Daily_Data"

options = Options()
#options.add_argument("--headless")  # crucial for cron

# === Configure Chrome to auto-download files ===
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})

# === Launch browser ===
driver = webdriver.Chrome(options=options)

# === Open the webpage ===
driver.get("https://biwenger.as.com/players")  # URL of list of players from Biwenger

# === Simulate the clicks that lead to the CSV download ===

time.sleep(5)  # Let the page load
driver.find_element(By.ID, "didomi-notice-agree-button").click() #: Necessary only when headless is off
time.sleep(1)
driver.find_element(By.XPATH, "//a[text()='Already have an account']").click()
time.sleep(1)
driver.find_element(By.NAME, "email").send_keys("degnetor@gmail.com")
driver.find_element(By.NAME, "password").send_keys("pruebas123")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
#driver.find_element(By.CLASS_NAME, "close-button").click()
#time.sleep(1)
driver.find_element(By.CLASS_NAME, "mat-mdc-menu-trigger").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[.//span[text()='Export']]").click()

# === Wait to ensure download starts ===
time.sleep(10)

old_path = os.path.join("/home/diego/Premier-Analysis/Daily_Data", "premier-league.csv")
new_name = datetime.now().strftime("%Y-%m-%d") + ".csv"
new_path = os.path.join("/home/diego/Premier-Analysis/Daily_Data", new_name)
os.rename(old_path, new_path)

# === Quit the browser ===
driver.quit()

# === Add data to master file ===
df_today = pd.read_csv(new_path, sep=';')
df_today.to_csv(new_path, index=False) #Change ; to ,
df_today = pd.read_csv(new_path, sep=',') #Re-read the new file with commas
df_today.insert(0, "Date", datetime.now().strftime("%Y-%m-%d")) #Create Date column

master_file = "/home/diego/Premier-Analysis/all_data.csv"

if os.path.exists(master_file):
    df_master = pd.read_csv(master_file, sep=',')
    df_combined = pd.concat([df_master, df_today], ignore_index=True)
else:
    df_combined = df_today

df_combined.to_csv(master_file, index=False, sep=',')
