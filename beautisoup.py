from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:  #opening html as file
    soup=BeautifulSoup(html_file,'lxml')# here we are creating an object of Beautiful

    #print(soup)
    print(soup.prettify()) # it will print a content in sequential way

#onl want to print out the title

    match = soup.title
    print(match)

#only text from thar perticular tag
    match= soup.title.text
    print(match)

    print('only want to print out div')
    #it will print 1st div from class
    match_div=soup.div
    print(match_div)

    print("if we want to print out div of footer then")

    match_div_footer=soup.find('div',class_='footer')# class is an special keyword which used to define a class so here class_ is used
    #it will print div of footer
    print(match_div_footer)


    print('article')
    article=soup.find('div',class_='article')
    headline=article.h2.a.text
    print(headline)

    summary=article.p.text
    print(summary)

    print('for printing all articles')

    for article in soup.find_all('div',class_='article'):
        headline=article.h2.a.text
        print(headline)

        summary=article.p.text
        print(summary)
