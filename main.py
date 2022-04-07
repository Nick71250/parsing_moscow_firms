import requests
from bs4 import BeautifulSoup as bs
import csv

# Function for writing to csv file
def write_csv(data):
	with open('data.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file, delimiter=';') # Need to define the delimeter ";" if data contains a lot of "," in order to divide it correctly into columns
		writer.writerow((data['title'], data['address'])) # define a string format in csv file

def get_page_data(html):
	# recieved html data we use bs4 and "lxml" parser to parse it
	soup = bs(html, "lxml")
	# First we search for all junks of code where the necessary data is located. Firms is the list of code-junks
	firms = soup.find_all("div", class_="row_tbl_search")
	# in each for-loop we take title and address from the junks of code that were collected on previous stage
	# if there is no title or address we use title = '' or address = ''
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
		# on each iteration we put title and address into the data dictionary
		data = {'title' : title, 'address' : address}
		# and write a string to the csv file according the rules that were defined earlier
		write_csv(data)
	


	
def main():
	# in each for-loop iteration we change url link and collect html data according to that link by calling get_page_data(html) function
	for i in range(1, 2495): # the number of pages was gotten experimentally (from the web-browser)
		URL = f"https://i.moscow/innoobjectstable?type=6735&page={i}&text="
		header = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
		r = requests.get(URL, headers=header)
		html = r.content
		get_page_data(html)

if __name__ == '__main__':
	main()


