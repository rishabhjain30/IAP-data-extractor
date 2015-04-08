import requests
import bs4
import xlsxwriter
from itertools import izip
from time import sleep

statename = ['Andhra Pradesh ','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand', 'Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal',]
def main():
 uls = []
 state=[]
 district=[]
 url='http://dolr.nic.in/hyperlink/distlistnew.htm'
 response = requests.get(url)
 soup = bs4.BeautifulSoup(response.text)
 state_name=soup.select('h2')
 firstH3 = soup.find('h2') # Start here

 for nextSibling in firstH3.findNextSiblings():
    if nextSibling.name == 'ul':
        uls.append(nextSibling)
 for ul in uls:
    for li in ul.findAll('li'):
            district.append(li.text)
 workbook = xlsxwriter.Workbook('new1.xlsx')
 worksheet = workbook.add_worksheet()
 bold = workbook.add_format({'bold': True})
 row = 1
 col = 1
 worksheet.write('A1', 'State', bold)
 worksheet.write('B1', 'District', bold)
 worksheet.write('C1', 'Description', bold)
 worksheet.write('D1', 'Website', bold)
  
 for item in state_name:
    state.append(item.text)
 for i iapindia district:       
   index='http://www.iapindia.org/search/search.php?query='+i+'&start=1&search=1&results=100&type=and&domain='
   sleep(1)
   try:

    url= index 
    descript=[]      
    website=[]
    response = requests.get(url)
    BeautifulSoupp = bs4.BeautifulSoup(response.content)
    g_data=soup.find_all("div", {"class": "description"})
    url_data=soup.find_all("div", {"class": "url"})
    for item,item2 in map(None,g_data,url_data):
     descript.append(item.text)
     print item       
     website.append(item2.text)
     print item2
    worksheet.write(row, col,i)
    print i
    for item2,item3 in map(None,descript,website):
      worksheet.write(row,2,item2)
      print item2
      worksheet.write(row,3,item3)
      print item3
      row+=1 
    row+=1
   except:
     pass 

    
     

main()