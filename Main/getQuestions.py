import requests
import time


def get_questions(max_answers=0, vote_min=-1, vote_max=3, *tags):
    questions = []
    if len(tags) == 0:
        print("You have no tags.")

    else:
        for tags in tags:
            result = requests.get(
                "https://api.stackexchange.com/2.2/search?page=1&order=desc&sort=creation&tagged={0}&site=stackoverflow".format(
                    tags))
            data = result.json()
            for items in data['items']:
                if items['is_answered'] is False and items['answer_count'] <= max_answers:
                    if items['score'] >= vote_min and items['score'] <= vote_max:
                        questions.append([items['link'], items['title']], )
            if len(tags) > 1:
                time.sleep(0.5)
    return questions
