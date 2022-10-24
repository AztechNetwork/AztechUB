import os
os.system("pip3 install tgcrypto pyrogram")
os.system("clear")
from pyrogram import Client



# guide them 

intro = """
@BotzXFactory Corporation
Get the following values by logging to,

https://my.telegram.org

Requirements:
  
  1. API_ID
  2. API_HASH
  3. PHONE NUMBER (WITH COUNTRY CODE, EX: +911034567891)
  
"""


print(intro)


API_ID = input("\nEnter your API_ID: ")

while not (API_ID.isdigit() and len(API_ID) == 7):
  print("\n\nPlease enter a valid 7 digit API_ID.\n\n")
  API_ID = input("Enter your API_ID (1234567): ")



API_HASH = input("\nEnter API HASH: ")



# create a new pyrogram session
with Client("Aztech", api_id=API_ID, api_hash=API_HASH) as app:
  app.send_message("me", f"This Is Your Aztech Userbot • [ `SESSION` ]\n\n```{app.export_session_string()}```\n\n⚠️• Don't share this with anyone !!\n\nCreate session online • [ Press Here]()", disable_web_page_preview=True) 
  print("\n\nYour String Session Is Successfully Saved In Telegram Saved (Cloud) Messages !! Don't Share It With Anyone!! Anyone having your session can use (hack) your telegram account !")
  
