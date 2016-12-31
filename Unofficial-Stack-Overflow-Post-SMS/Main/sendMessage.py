from twilio.rest import TwilioRestClient

accountSID = '*'
authToken = '*'

twilioCli = TwilioRestClient(accountSID, authToken)

myTwilioNumber = '+*'
myCellPhone = '*'

def sendMessage(sendmessage):
    try:
        str(sendmessage)
        message = twilioCli.messages.create(body=sendmessage, from_=myTwilioNumber, to=myCellPhone)
    except:
        print("Bad message format")
