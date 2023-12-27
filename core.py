import re
import csv
from datetime import datetime
from message_parser import parse_message
from dotenv import load_dotenv
import app
import os
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request

categories = {
    1: "Rent",
    2: "Utilities",
    3: "Telephone",
    4: "Household",
    5: "Food",
    6: "Travel",
    7: "Tax",
    8: "Subscriptions",
    9: "Insurance",
    10: "Medical",
    11: "Other"
}

filename = "spending_data.csv"

load_dotenv()
CREDENTIALS_JSON = os.getenv("CREDENTIALS_JSON")
SHEET_ID = os.getenv("SHEET_ID")

def get_category(place):
    return None

def process_spending(sender_id, payload):
    (amount, desc, category_int) = payload

    if category_int == None:
        # If category is missing, reprompt the user for full message
        # TODO handle stateful messaging where user can just add category
        send_message(sender_id, 1)
    else:
        print("Writing to sheet")
        write_to_sheet(datetime.now(), amount, categories[category_int])
        print("Writing to csv")
        write_to_csv(datetime.now(), amount, desc, category_int, categories[category_int])
    return None

def process_fetching(payload):
    return NotImplementedError

def process_analytics(payload):
    return NotImplementedError

def write_to_sheet(date, amount, category):
    # Create sheets client
    try:
        # scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        # creds = Credentials.from_service_account_file(CREDENTIALS_JSON, scopes=scope)
        # creds.refresh(Request())
        client = gspread.service_account(filename=CREDENTIALS_JSON)
        print("here")
    except Exception as e:
        print(e)

    # Open the current year sheet
    sheet = client.open_by_key(SHEET_ID).worksheet(str(date.year))
    print(sheet)
    # Find month col and category row
    col = sheet.find(str(date.strftime("%B"))).col
    row = sheet.find(str(category)).row
    print("Fount row and col: " + str(row) + ", " + str(col))

    # Update value in the cell
    curr_val = sheet.cell(row, col, value_render_option='UNFORMATTED_VALUE').value
    new_val = float(curr_val) + float(amount) if curr_val else float(amount)

    sheet.update_cell(row, col, new_val)

    return None

def write_to_csv(date, amount, desc, category_int, category):
    with open(filename,'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, desc, category_int, category])
    return None

def send_message(sender_id, code):
    """Sends back a message using the flask app.py.

    Args:
        code (int): 
            0 - Invalid message/help
            1 - No category provided in spending message

    Returns:
        _type_: _description_
    """
    message = ""
    if code == 0:
        message = "Invalid message. Please send a spending message as $<amt> <description> <category>. The categories are as follows:" + "\n".join([f"{key}. {value}" for key, value in categories.items()])
    elif code == 1:
        message = "No category found. Please send a spending message as $<amt> <description> <category>"
    
    response = app.call_send_api(sender_id, message)
    return None

def process_message(sender_id, message):
    """Recieves message from Flask API and processes it. If the message cannot 
    be parsed into one of the 3 message types, sends back a help message.

    Args:
        message (string): Messenger message
    """
    type, payload = parse_message(message)
    if type == 1:
        process_spending(sender_id, payload)
    else:
        print("Invalid message")
        send_message(sender_id, 0)
