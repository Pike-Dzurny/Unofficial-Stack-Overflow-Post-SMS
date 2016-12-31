import time 
from getQuestions import getQuestions
from sendMessage import sendMessage
import random

maxanswers = 0
votemin = -3
votemax = 1

while 1:
    content = getQuestions(maxanswers, votemin, votemax, 'python')
    content = random.choice(content)
    time.sleep(3)
    sendMessage(content)
    time.sleep(60*60*24)
    