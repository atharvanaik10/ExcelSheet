def parse_message(message):
    """Parses the complete message recieved from the user

    Args:
        message (string): Full string message

    Returns:
        message_type (int): 1 - spending, 2 - fetching, 3 - analytics, 0 - error
        payload (tuple): 
            For type 1 messages - (amount, description, category)
            For type 2 messages - (month, year)
            For type 3 messages - (query)
    """
    if not message:
        return None
    
    message = message.strip()
    type = message[0]
    payload = message[1:].strip()

    if type == '$':
        parts = payload.split()
        if len(parts) < 2:
            return None, None, None

        amount = parts[0]
        desc = parts[1]

        try:
            category = parts[2]
            return 1, (float(amount), desc, int(category))
        except (ValueError or IndexError):
            return 1, (float(amount), desc, None)
        
    # elif type == '?':
    #     print("Fetching")
    # elif type == '!':
    #     print("Analytics")
    else:
        return 0, (None, None, None)
