import re
import csv
from datetime import date
from message_parser import parse_message
from dotenv import load_dotenv

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

def get_category(place):
    return None

def process_spending(payload):
    (amount, desc, category) = payload

    if category == None:
        # If category is missing, reprompt the user for full message
        # TODO handle stateful messaging where user can just add category
        send_message(1)
    else:
        write_to_sheet(date.today(), amount, category)
        write_to_csv(date.today(), amount, desc, category)
    return None

def process_fetching(payload):
    return NotImplementedError

def process_analytics(payload):
    return NotImplementedError

def write_to_sheet(date, amount, category):
    return None

def write_to_csv(date, amount, desc, category):
    with open(filename,'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, desc, category])
    return None

def send_message(code):
    """Sends back a message using the flask app.py.

    Args:
        code (int): 
            0 - Invalid message/help
            1 - No category provided in spending message

    Returns:
        _type_: _description_
    """
    return None

def process_message(message):
    """Recieves message from Flask API and processes it. If the message cannot 
    be parsed into one of the 3 message types, sends back a help message.

    Args:
        message (string): Messenger message
    """
    type, payload = parse_message(message)
    if type == 1:
        process_spending(payload)
    else:
        send_message(0)
