import requests 
from bs4 import BeautifulSoup as BS

def parser():
	url = 'https://cars.kg'
	all_links = []
	for i in range(1,5):
		resp = requests.get(url + '/offers' + str(i))
		soup = BS(resp.text, 'lxml')
		all_links.extend(list(map(lambda a: url + a.get('href'), soup.find_all('a', class_="catalog-list-item"))))
		print('Я спарсил страницу №' + str(i))
		

parser()