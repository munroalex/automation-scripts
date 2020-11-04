#imports
from twilio.rest import Client
from datetime import datetime, timedelta
import pytz

#set twilio account variables
account_sid ='AC04...' # paste in Account SID between single quotes
auth_token ='e1...' # paste Auth Token between single quotes

#create function to send reminder message
def send_message():
    client = Client(account_sid, auth_token)

    # this is the Twilio sandbox testing number
    from_whatsapp_number = 'whatsapp:+14155238886'
    # replace this number with your own WhatsApp Messaging number
    to_whatsapp_number = 'whatsapp:+61485678912'
    # replace Message! with your reminder message
    client.messages.create(body='Message!',
                        from_=from_whatsapp_number,
                        to=to_whatsapp_number)

#replace with your country and city seperated by / with no spaces
tz_local = pytz.timezone('Your Country/Your City') 
start_time = datetime.now(tz_local)
print(start_time)


for i in range(23):
    #sets the time for the start of each round
    round_time = datetime.now(tz_local)
    done = False
    #choose your timer length, I have it set to 30 minutes to remind me to get up and move around every thirty minutes
    thirty_minute_delta = (round_time + timedelta(minutes = 30)).strftime("%H:%M:%S")
    
    while done != True:
        #check current time against delta time
        current_time = datetime.now(tz_local)

        if current_time.strftime("%H:%M:%S") >= thirty_minute_delta:
            done = True
            send_message()
            print(current_time)
