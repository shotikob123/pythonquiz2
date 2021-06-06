import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

f = open('movies.csv', 'w', newline='\n', encoding="utf-8")

file_obj = csv.writer(f)
file_obj.writerow(['Movie Title','IMDB Rating'])

h = {'Accept-Language': 'en-US'}
ind = 1
while ind < 5:
    url = 'http://www.file.ge/index.php?paged='+str(ind)
    r = requests.get(url, headers=h)

    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    movies_block = soup.find('div', {'id': 'content'})
    all_movies = movies_block.find_all('div', class_='entry')

    for each in all_movies:
        nameTemp = each.find('a', {'rel': 'bookmark'})
        a= nameTemp.text.find('/')
        name = nameTemp.text[:a]
        try:
            imdbRating = each.find('font', {'color': '#2BA94F'}).text
        except:
            pass
        # print(imdbRating)

        # f.write(name+','+imdbRating+'\n')
        file_obj.writerow([name, imdbRating])
    ind += 1
    sleep(randint(3,8))