# coding : utf-8
import urllib
from urllib import request 
from bs4 import BeautifulSoup
import re
api_url = 'http://historical.elections.virginia.gov/elections/jump_list/39050/year_from:1924/year_to:2015/office_id:1/stage:General'
headers_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

request = urllib.request.Request(api_url, headers=headers_dict)
response = urllib.request.urlopen(request)
html = response.read()

soup = BeautifulSoup(html,'html.parser')
items_list = soup.find_all('option')
f = open('ELECTION_ID','w')
f.write('2016\t80871\n')
for item in items_list[1:]:
    f.write('{0}\t{1}\n'.format(re.findall('[0-9]+$',item.string)[0],item['value']))
f.close()
