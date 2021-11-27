import urllib.request
import urllib.parse
import pandas as pd
from bs4 import BeautifulSoup

print('==============================뽐뿌 zbord 크롤링 프로그램=====================================')
print('카테고리[1.질문]/[2.기기]/[3.구입관련]/[4.판매]/[5.번호/회선]/[6.A/S]/[7.답변완료]/[8.요청]')
cateGory = input('카테고리 선택하세요 :')

pageNum = 1 #페이지 초기화
count = 1

i = input('몇페이지까지 크롤링 할까요? : ')

lastPage = int(i) * 30 - 29


while pageNum < lastPage + 1:
    
    url = f'https://www.ppomppu.co.kr/zboard/zboard.php?id=phone2&page={pageNum}&category={cateGory}&divpage=350'

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    data = soup.find_all('tr', {'class': ['list0', 'list1']})


    print(f'-----{count}페이지 결과입니다.-----')

 
    row_list = []

    for j in data:
        listNums = j.find_all('td', class_ = 'eng list_vspace')[0] # 일련번호
        titles = j.find('font', class_ = 'list_title')#제목
        link = j.find("td", class_="list_vspace") #질문내용
        wrName = j.find("span", class_="list_name") #작성자
        Wdate = j.find_all('td', class_ = 'eng list_vspace')[1] #등록일시
        ctNum = j.find_all('td', class_ = 'eng list_vspace')[3] #조회수
    
        row_list.append([(listNums.string)]
        # b_list.append([titles.string])
        # c_list.append(['https://www.ppomppu.co.kr/zboard/view.php?id=phone2&page=1&divpage=350&category=1&no='+link.string])
        # d_list.append([wrName.string])
        # e_list.append([Wdate.attrs['title']])
        # f_list.append([ctNum.string])

        
pageNum += 10
count += 1