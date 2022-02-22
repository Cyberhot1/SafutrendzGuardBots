from datetime import datetime



def sample_responses(input_text):
    user_message = str(input_text).lower()
        

    if user_message in ("when moon", "moon when", "when lambo"):
        return "start shilling to moon your own bag, type /shill to get shill groups"

    if user_message in ("who are you", "who are you?"):
        return "I'm the SaFuTrendz Guard Bot"

    if user_message in ("where is admin", "where is admin?"):
        return "You can find the admin by typing /admin"

    if user_message in ("time", "what is the time?"):
        now = datetime.now()
        date_time = now.strftime("⏰ %m/%d/%Y, %H:%M:%S")

        return str(date_time)

    #return "I dont understand"
