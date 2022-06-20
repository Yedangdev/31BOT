import requests, re
from bs4 import BeautifulSoup
  
  
    def get_diet(): 

         #await message.channel.send('시간이 약간 걸릴수 있어요..') 

         url = "https://hiyedang.hs.kr/" 

  

         res = requests.get(url,timeout = 40)    #학교 급식게시판 파싱 

         res.raise_for_status() 

         soup = BeautifulSoup(res.text, "lxml")  

  

         diet = soup.find_all("div", attrs={"class":"menu"})  #가져올 요소 

         for diets in diet: 

             result = diets.get_text() #텍스트만 추출 

              

              

              

          

            

         

      
