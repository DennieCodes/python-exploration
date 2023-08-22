import requests

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}  # Headers to mimic a browser visit

res = requests.get("https://www.zillow.com/homes/06704_rb/", headers = headers) # url

html = BeautifulSoup(res.text, 'html.parser')

listing = html.find("ul", class_="List-c11n-8-84-3__sc-1smrmqp-0 StyledSearchListWrapper-srp__sc-1ieen0c-0 doa-doM fgiidE photo-cards photo-cards_extra-attribution")

list_item = listing.contents[0] # print first listing
list_container = list_item.select('article')
# list_details = list_card.div
print(list_container)

# text_file = open("Output.txt", "w")
# text_file.write(str(html))
# text_file.close()

# uls = html.find_all('div', class_="search-page-list-header")

# print(uls)