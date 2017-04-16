from twilio.rest import TwilioRestClient

accountSID = '*'
authToken = '*'

twilioCli = TwilioRestClient(accountSID, authToken)

myTwilioNumber = '*'
myCellPhone = '*'


def send_message(send_message):

    try:
        str(send_message)
        message = twilioCli.messages.create(body=send_message, from_=myTwilioNumber, to=myCellPhone)
    except:
        print('Bad message format')
