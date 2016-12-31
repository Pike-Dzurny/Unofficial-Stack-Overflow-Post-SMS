import requests
import time
from pprint import pprint
import json

def getQuestions(maxanswers=0, votemin=-1, votemax=3, *tags):
    questions = []
    if len(tags) == 0:
        print("You have no tags.")
        
    else:
        for tags in tags:
            result = requests.get("https://api.stackexchange.com/2.2/search?page=1&order=desc&sort=creation&tagged={0}&site=stackoverflow".format(tags))
            data = result.json()
            for items in data['items']:
                if items['is_answered'] == False and items['answer_count'] <= maxanswers:
                    if items['score'] >= votemin and items['score'] <= votemax:
                        questions.append([items['link'], items['title']],)
            if len(tags) > 1:
                time.sleep(0.5)
    return questions




    

