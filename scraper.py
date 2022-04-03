import requests
import json
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/95365253#tab=reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("div.js_product-review")

all_reviews = []

for review in reviews:
    review = reviews.pop(6)

    review_id = review["data-entry-id"]

    author= review.select("span.user-post__author-name").pop(0).text.strip()

    recommenadtion = review.select("span.user-post__author-recomendation").pop(0).text

    recommenadtion = True if recommenadtion == "Polecam" else False if recommenadtion == "Nie Polecam" else None

    stars = review.select("span.user-post__score-count").pop(0).text
    stars = float(stars.split("/").pop(0).replace(",","."))

    content = review.select("div.user-post__text").pop(0).text

    content = content.replace("\n", " ")

    publish_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"]

    purchase_date = review.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"]

    useful = review.select("span[id^=votes-yes]").pop(0).text
    useful=int(useful)

    useless = review.select("span[id^=votes-no]").pop(0).text
    useless=int(useless)

    Positives_list= review.select("div.review-feature__title--positives ~ div.review-feature__item")


    Negatives_list = review.select("div.review-feature__title--negatives ~ div.review-feature__item")

    single_review = {
        "review_id": review_id,
        "author": author,
        "reccomendation": recommenadtion,
        "stars": stars,
        "content": content,
        "publish_date": publish_date,
        "purchase_date": purchase_date,
        "useful": useful,
        "useless": useless,
        "Positives_list": Positives_list,
        "Negatives_list": Negatives_list

    }
    all_reviews.append(single_review)
    print(json.dumps(single_review, indent=4, ensure_ascii=False))

