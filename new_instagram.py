from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
from selenium.webdriver.common.keys import Keys
import time
inp=input('enter your username:::  ')

driver=webdriver.Chrome('/home/peter/chromedriver_linux (1)/chromedriver')
a=driver.get('https://www.instagram.com/'+inp+'/')
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

html=driver.execute_script('return document.documentElement.outerHTML;')
soup=BeautifulSoup(html,'html.parser')
div=soup.find_all('div',class_='v9tJq AAaSh')
li=[]
count=1
final_list=[]
for data in div:
	photo=(data.img['src'])
	main_posts=data.find_all('div',class_='Nnq7C weEfm')
	mai_posts=data.find_all('div',class_='KL4Bh')
	

	name=data.find('div',class_='nZSzR')
	post=data.find('ul',class_='k9GMp')
	pr=post.find_all('span')
	
	for j in pr:
		li.append(j.get_text())
	posts=li[0]


		
	followers=li[1]
	following=li[2]
	for l in mai_posts:
		sa=(l.img['src'])
		dic={'name':inp,'photo':photo,'posts':posts,'followers':followers,'following':following,'links':sa,'count':count}
		count+=1
		final_list.append(dic)
		pprint(final_list)
		main3=open('new_instagram.html','w+')
		names1=main3.write('<html><head><title>oppo</title></head>\n')
		names5=main3.write('<body>\n')
		names11=main3.write('<h1 style="font-size:50px;font-style:italic;text-align:center">INSTA</h1>\n')
		names12=main3.write('<div style="height:100px;width:100px" >'+'<img src='+''+photo +' '+  '  style="margin-left:500px;border-radius:100%"''>'+'</div>')
		names13=main3.write('<h2 style="font-size:30px;text-align:center;margin-top:80px;">'+inp+'</h2>'+'<hr>\n')
		names14=main3.write('<span style="font-size:40px;color:green">'+'<u>'+'POSTS::::'+'</u>'+dic['posts']+'</span>\n')
		names15=main3.write('<span style="font-size:40px;color:red;margin-left:200px" >'+'<u>'+'FOLLOWING::::'+'</u>'+dic['followers']+'</span>\n')
		names16=main3.write('<span style="font-size:40px;color:blue;margin-left:80px" >'+'<u>'+'FOLLOWERS::::'+'</u>'+dic['following']+'</span>\n')

		names6=main3.write('<table border=1px style="color:black;border-color:red;border-radius:10px 10px 10px 10px">\n')
		names7=main3.write('<tr style="font-size:30px">\n<td>s no.</td>\n<td>photos</td>\n</tr>\n')
		names8=main3.write('<tr style="font-size:20px">')
		main_count=1
		lem=1
		for main_data in final_list:
			photos=main_data['links']

			names9=main3.write('<td>'+str(main_count)+'</td>'+'<td>'+'<img src= "'+ photos +'"' + 'style="height:100px;width:100px;">' + '</td>'+'<tr style="font-size:20px">')
			lem+=1
			main_count+=1
		names10=main3.write('</tr>\n')

		names8=main3.write('</table>\n')

		names9=main3.write('</body>\n')
		names10=main3.write('</html>')
	driver.close()
	
