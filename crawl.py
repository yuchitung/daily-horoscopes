from flask import jsonify
import os
from bs4 import BeautifulSoup
import requests
import json
import time

def crawl():
    url = 'http://astro.click108.com.tw/daily_10.php?iAstro='
    horoscopes = ['牡羊座','金牛座','雙子座','巨蟹座','獅子座','處女座','天秤座','天蠍座','射手座','魔羯座','水瓶座','雙魚座']

    daily_horoscopes = {}
    for key,horoscope in enumerate(horoscopes):
        request = requests.get( url + str(key))
        time.sleep(1)
        if request.status_code == requests.codes.ok:
            soup = BeautifulSoup(request.text, 'html.parser')
            daily_horoscopes.update({
                horoscope : format(soup)
            })

    with open('daily-horoscopes.json', 'w') as outfile:
        json.dump(daily_horoscopes, outfile,ensure_ascii=False)

    return jsonify(daily_horoscopes)

def format(soup):
    today_word = soup.find('div', class_='TODAY_WORD').find('p').get_text(strip=True)
    color = soup.find('div', class_='TODAY_LUCKY').select('h4')[1].get_text(strip=True)
    content = soup.find('div', class_='TODAY_CONTENT')
    p_tags = content.select('p')

    star_entirety = content.find('span', class_='txt_green').get_text(strip=True)
    desc_entirety = p_tags[1].get_text(strip=True)

    star_love= content.find('span', class_='txt_pink').get_text(strip=True)
    desc_love = p_tags[3].get_text(strip=True)

    star_work= content.find('span', class_='txt_blue').get_text(strip=True)
    desc_work = p_tags[5].get_text(strip=True)

    star_money= content.find('span', class_='txt_orange').get_text(strip=True)
    desc_money = p_tags[7].get_text(strip=True)

    return {
        'TODAY_WORD': today_word,
        'LUCKY_COLOR': color,
        'STAR_ENTIRETY': star_entirety,
        'DESC_ENTIRETY': desc_entirety,
        'STAR_LOVE': star_love,
        'DESC_LOVE': desc_love,
        'STAR_WORK': star_work,
        'DESC_WORK': desc_work,
        'STAR_MONEY': star_money,
        'DESC_MONEY': desc_money
    }
    