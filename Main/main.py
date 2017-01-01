import time
import random
from getQuestions import get_questions
from sendMessage import sendMessage

max_answers = 0
vote_min = -3
vote_max = 1

while 1:
    content = get_questions(max_answers, vote_min, vote_max, 'python')
    content = random.choice(content)
    time.sleep(3)
    sendMessage(content)
    time.sleep(60*60*24)
    
