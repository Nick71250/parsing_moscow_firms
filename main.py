import requests
from bs4 import BeautifulSoup as bs
import csv

def write_csv(data):
	with open('data.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file, delimiter=';')
		writer.writerow((data['title'], data['address']))

def get_page_data(html):
	# with open("sergey.html") as file:
	# 	src = file.read()
	
	soup = bs(html, "lxml")
	firms = soup.find_all("div", class_="row_tbl_search")
	# print(firms)
	
	for firm in firms:
		try:
			title = firm.find("div", class_="div_text").text.strip().replace("\n", "")
			print(title)
		except:
			title = ''
		try:
			address = firm.find("div", class_="dop_content1").text.strip().replace("\n", "")
			print(address)
		except:
			address = ''
		data = {'title' : title, 'address' : address}
		write_csv(data)
	


	
def main():
	for i in range(2115, 2495):
		URL = f"https://i.moscow/innoobjectstable?type=6735&page={i}&text="
		header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
		r = requests.get(URL, headers=header)
		html = r.content
		get_page_data(html)

if __name__ == '__main__':
	main()


