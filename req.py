from bs4 import BeautifulSoup
import requests

source=requests.get('http://coreyms.com').text
#it wil return response objetand to get code fotm that use text() method

soup=BeautifulSoup(source,'lxml')
print(soup.prettify())

csv_file=open('csv_req.csv','w')

csv_writer=csv.writer(csv_file)
csv.writer.writerow(['headline','summary','you-tube_link'])
for article in soup.find('article'):
#print(article.prettify())

   headline=article.h2.a.text
   print(headline)


   summary=soup.find('div',class_='entry-content')
   summ=summary.p.text
   print(summ)

   try:

       vid_src=article.find('iframe',class_='youtube-player')['src']# it will return an src
       vid_id=vid_src.split('/')[4]# because id at location 5
       vid_id=vid_id.split('?')[0]
       yt_link=f'www.youtube.com/watch?v={}'
   except Exception as e:
        yt_link=None

print(yt_link)


   csv.writer.writerow([headline,summ,yt_link])
