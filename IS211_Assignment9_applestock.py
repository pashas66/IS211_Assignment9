#IS211 Assignment-9, Part II
#In this assignment we will load the URL, parse it using BeautiulSoup, and output the close price and data for all the dates shown on the page.
#importing the required libraries:

import sys
import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
	headers = { 'User-Agent' : user_agent }
	req = requests.get(url, headers=headers).content
	html = bs(str(req), 'lxml')   #here we are parsing using BeautiulSoup as "bs"
	return html

#here we are parsing through the data in table row and returning the data closing price value and closing date
def get_appl_close(html): 
     # here it is required to get list of all the rows from the table. We have to use the attribute "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"
    rows = html.findAll('tr', attrs={'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
    appl_close=[]
    for row in rows:
        try:
            close_date = row.findAll('span')[0].text.strip()
            close_value = row.findAll('span')[4].text.strip()
            appl_close.append([close_date, close_value])
        except:
            break
    return appl_close

#print statements for closing price and date: 
def print_aapl(appl_close):
    print("\nApple Stock (Ticker AAPL) Closing Values:\n")
    print("{:<20}{:<10}".format('Date', 'Close Value\n'))
    for aapl in appl_close:
        print("{:<20}{:<10}".format(aapl[0], aapl[1]))

def main():
        #here we are loading the url 
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    html = get_html(url)
    appl_close = get_appl_close(html)
    print_aapl(appl_close)
    sys.exit()

if __name__ == '__main__':
    main() #calling the main function 
        #end of the code