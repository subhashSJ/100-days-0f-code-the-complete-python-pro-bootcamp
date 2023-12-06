import requests

AMOUNT_OF_QUESTIONS = 10
QUESTION_TYPE = 'boolean'
CATEGORY = 18

try:
    response = requests.get(url="https://opentdb.com/api.php",
                            params={'amount': AMOUNT_OF_QUESTIONS, 'type': QUESTION_TYPE, 'category': CATEGORY})
    response.raise_for_status()
    question_data = response.json()['results']
except:
    question_data = []
