import sys
import requests
from bs4 import BeautifulSoup


if len(sys.argv) != 3 :
    print("Usage: python scraping_mine.py [TABLE] [PAGE]")
    sys.exit()

tableName = sys.argv[1]
page = sys.argv[2]

url = f'http://localhost:9943/ex2?table={tableName}&page={page}'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


csvWriter = open(f'{tableName}_{page}.csv','w')
csvHeaderCheck = True
tablePasred = soup.find_all('table')
for row in tablePasred[0].children:
    if row != "\n":
        if csvHeaderCheck:
            cols = row.find_all('th')
            csvHeaderCheck = False
        else:
            cols = row.find_all('td')
        attr = [item.get_text()   for item in cols[1:] ]
        line = ','.join(attr)
        csvWriter.write(line+"\n")

print("CSV出力が完了しました！")