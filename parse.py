from bs4 import BeautifulSoup
import json

def parse(url):
    reponse = BeautifulSoup(url, 'html.parser')
    reviews = reponse.find_all('div', class_='jftiEf fontBodyMedium')
    data = []
    with open('reviews.json', 'w', encoding='utf-8') as file:
        for review in reviews:
            name = review.find('div', class_='d4r55')
            name_parsed = name.find('span').text
            text = review.find('span', class_='wiI7pd').text
            answer = review.find('div', class_='wiI7pd').text if review.find('div', class_='wiI7pd') else None
            data.append({
                'Imię': name_parsed,
                'Recenzja': text,
                'Odpowiedź właściciela': answer
            })
        json_object = json.dumps(data, indent=2, ensure_ascii=False)
        file.write(json_object)