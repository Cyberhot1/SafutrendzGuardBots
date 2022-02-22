from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("when moon", "moon when", "when lambo"):
        return "start shilling to moon your own bag, type /shill to get shill groups"
    
    if user_message in ("when launch"):
        return "Launch Date TBA, \n wait for announcement in the Group"
    
    if user_message in ("who can i contact for marketing", "marketing proposal", "marketing", "Marketing"):
        return "For marketing proposal, \n Kindly Mail us on marketing@safutrendz.com "
    
    if user_message in ("who can i contact for partnership", "partnerhip proposal", "partnership", "Partnership"):
        return "For partnership proposal, \n Kindly Mail us on partnership@safutrendz.com "

    if user_message in ("who are you", "who are you?"):
        return "I'm the SaFuTrendz Guard Bot"

    if user_message in ("where is admin", "where is admin?", "where is admin", "where is the admin"):
        return "You can find the admin by typing /admin"

    if user_message in ("time", "what is the time?"):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        return str(date_time)

    #return "I dont understand"
