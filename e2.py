# coding: utf-8
import urllib
from  urllib import request
headers_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
for line in open('ELECTION_ID','r'):
    #print(line.strip('\n').split('\t')[1])
    year = line.strip('\n').split('\t')[0]
    filename = year+'.csv'
    api_url = 'http://historical.elections.virginia.gov/elections/download/{0}/precincts_include:0/'.format(line.strip('\n').split('\t')[1])
    print(api_url)
    req = urllib.request.Request(api_url, headers=headers_dict)
    response = urllib.request.urlopen(req)
    with open(filename,'w') as f:
        f.write(str(response.read(),encoding='utf-8'))
        f.close()
print('Finish')