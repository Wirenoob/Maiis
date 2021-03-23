import re
import os
import ast
import bs4
import wget
import requests
from config import total_screen_shot

def imdb(movie_name):
    try:
        final_name = movie_name.replace(' ', '+')
        page = requests.get(
            f"https://www.imdb.com/find?ref_=nv_sr_fn&q={final_name}&s=all")
        soup = bs4.BeautifulSoup(page.content, 'lxml')
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext('td').findNext('td').text
        mov_link = "http://www.imdb.com/" + odds[0].findNext('td').findNext('td').a['href']
        page1 = requests.get(mov_link)
        soup = bs4.BeautifulSoup(page1.content, 'lxml')
        image = soup.find('link', attrs={"rel": "image_src"}).get('href', None)
        list_of_ss = screen_shot(mov_link)
        screen = list_of_ss
        if soup.find('div', 'title_wrapper'):
            pg = soup.find('div', 'title_wrapper').findNext('div').text
            mov_details = re.sub(r'\s+', ' ', pg)
        else:
            mov_details = ''
        credits_ = soup.findAll('div', 'credit_summary_item')
        if len(credits_) == 1:
            director = credits_[0].a.text
            writer = 'Not available'
            stars = 'Not available'
        elif len(credits_) > 2:
            director = credits_[0].a.text
            writer = credits_[1].a.text
            actors = []
            for x in credits_[2].findAll('a'):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + ',' + actors[1] + ',' + actors[2]
        else:
            director = credits_[0].a.text
            writer = 'Not available'
            actors = []
            for x in credits_[1].findAll('a'):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + ',' + actors[1] + ',' + actors[2]
        if soup.find('div', "inline canwrap"):
            story_line = soup.find('div', "inline canwrap").findAll('p')[0].text
        else:
            story_line = 'Not available'
        if len(story_line) > 450:
            story_line = story_line[:450] + "..."
        info = soup.findAll('div', "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll('a')
                for i in a:
                    if "country_of_origin" in i['href']:
                        mov_country.append(i.text)
                    elif "primary_language" in i['href']:
                        mov_language.append(i.text)
        if soup.findAll('div', "ratingValue"):
            for r in soup.findAll('div', "ratingValue"):
                mov_rating = r.strong['title']
        else:
            mov_rating = 'Not available'
        des_ = f"""
**Title🎬: **`{mov_title}`

**More Info: **`{mov_details}`
**Rating⭐: **`{mov_rating}`
**Country🗺: **`{mov_country[0]}`
**Language: **`{mov_language[0]}`
**Cast Info🎗: **
  **Director📽: **`{director}`
  **Writer📄: **`{writer}`
  **Stars🎭: **`{stars}`

**IMDB URL Link🔗: **{mov_link}

**Story Line : **`{story_line}`

""" # **Photos 👇👇👇**
    except IndexError as e:
        print(f'IndexError imdb : {e}')
        return None, None, None
    return  des_, screen, image

def screen_shot(link):
    try:
        if not 'https' in link:
            link = link.replace('http', 'https')
        link = f'{link}mediaindex?ref_=tt_pv_mi_sm'
        page = requests.get(link).text
        soup = bs4.BeautifulSoup(page, 'lxml')
        pic_data = soup.find('script', attrs={'type' : 'application/ld+json'}).text
        pic_data = ast.literal_eval(pic_data)
        n = 0
        list_of_ss = []
        for screen_link in range(total_screen_shot):
            list_of_ss.append(pic_data['image'][n]['url'])
            n = n + 1
        return list_of_ss
    except Exception as e:
        list_of_ss = []
        print(f'Error while getting screen shots  imdb {e}\n\nWith link {link}')
        return list_of_ss
