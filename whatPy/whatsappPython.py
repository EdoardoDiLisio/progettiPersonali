# pip install pywhatkit
import pywhatkit as kit

# Specify the phone number (with country code) and the message
phone_number = "+4545454545"
message = "Hello World"
# Send the message instantly
kit.sendwhatmsg_instantly(phone_number, message)