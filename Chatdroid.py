import discord
import requests
from bs4 import BeautifulSoup
import re
from random import *
import asyncio
import os
import time
import googletrans
from googletrans import Translator



client = discord.Client()
@client.event
async def on_ready():
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    
    await client.change_presence(status=discord.Status.online) #온라인
    #await client.change_presence(status=discord.Status.idle) #자리비움
    #await client.change_presence(status=discord.Status.dnd) #다른용무
    #await client.change_presence(status=discord.Status.offline) #오프라인
    
    await client.change_presence(activity=discord.Game(name="!help 대기"))

    



@client.event
async def on_message(message):
    
    global titi
    global scrip
    global timetble
    
    if message.content.startswith("!한영"):
      text1 = message.content[4:]
      translator = Translator()
      trans1 = translator.translate(text1, src='ko', dest='en')
      embed = discord.Embed(title="한국어를 영어로 번역했어요", color=0xfaf4c0)
      await message.channel.send(embed=embed)
      await message.channel.send("번역결과: {}" .format(trans1.text))

    
    if message.content.startswith("!한일"):
      text1 = message.content[4:]
      translator = Translator()
      trans2 = translator.translate(text1, src='ko', dest='ja')
      embed = discord.Embed(title="한국어를 일본어로 번역했어요", color=0xfaf4c0)
      await message.channel.send(embed=embed)
      await message.channel.send("번역결과: {}" .format(trans2.text))
      
    
    if message.content.startswith("!영한"):
      text1 = message.content[4:]
      translator = Translator()
      trans3 = translator.translate(text1, src='en', dest='ko')
      embed = discord.Embed(title="영어를 한국어로 번역했어요", color=0xfaf4c0)
      await message.channel.send(embed=embed)
      await message.channel.send("번역결과: {}" .format(trans3.text))
      
    
    if message.content.startswith("!일한"):
      text1 = message.content[4:]
      translator = Translator()
      trans4 = translator.translate(text1, src='ja', dest='ko')
      embed = discord.Embed(title="일본어를 한국어로 번역했어요" ,color=0xfaf4c0)
      await message.channel.send("번역결과: {}" .format(trans4.text))
      await message.channel.send(embed=embed)
   
  
    if message.content.startswith('!312안녕'):
        embed = discord.Embed(title="EasterEgg_file_load_process", description = "Chatdroid_memory", color=0xfaf4c0)
        #embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/983342486812516416/986281059345924167")
        await message.channel.send(embed=embed)
        await message.channel.send("https://media.discordapp.net/attachments/986620556675776532/986638305724620800/Easter_egg_312_1.jpg\nhttps://media.discordapp.net/attachments/986620556675776532/986639756333043753/Easter_egg_312_2.jpg")
        
    
    if message.content.startswith('!TOKEN'):  #토큰 해킹에 대한 약간의 보안조치
        await message.channel.send("send:{}" .format(message.author.mention))
        embed = discord.Embed(title="보안경고", description = "승인되지 않은 유저가 봇 토큰에 대해 접근의도를 보입니다.\n\nsol:reset token", color=0xfaf4c0)
        #embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/983342486812516416/986281059345924167")
        await message.channel.send(embed=embed)
        
    if message.content.startswith('!d6'):  
        await message.channel.send("{}님이 주사위를 굴렸어요!" .format(message.author.mention))
        dice = randint(1,6)
        embed = discord.Embed(title="주사위 결과", description = f"🎲{dice}이(가) 나왔습니다!", color=0xfaf4c0)
        await message.channel.send(embed=embed)

        
    if message.content.startswith('!시간표'):
        wday = time.localtime().tm_wday
        if wday == 0:
            timetble = '프로\n기하\n미적\n논술\n영독작\n물리2\n생명2'
        elif wday == 1:
            timetble = '기하\n미적\n여지\n심국\n영독작\n생명2\n프로'
        elif wday == 2:
            timetble = '여지\n영독작\n프로\n미적\n생명2\n물리2\n논술'
        elif wday == 3:
            timetble = '여지\n스포\n심국\n진로\n영독작\n물리2\n미적'
        elif wday == 4:
            timetble = '자율3\n심국\n스포\n기하\n자봉\n동아'
        elif wday == 5:
            timetble = '놀기'
        elif wday == 6:
            timetble = '놀기'

        embed = discord.Embed(title="📝오늘의 시간표!", description=f"{timetble}", color = 0x62c1cc)
        embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/983342486812516416/986418832526684241")
        await message.channel.send(embed=embed)
        await message.channel.send("오전 9시에 시간표가 갱신됩니다")
        


    if message.content.startswith('!제목'):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            
            await message.channel.purge(limit=1)
            titi = message.content[4:]
            await message.channel.send('제목이 할당되었습니다!')
            
        if i is False:

            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이없습니다".format(message.author.mention))


    if message.content.startswith('!내용'):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            
            await message.channel.purge(limit=1)
            scrip = message.content[4:]
            await message.channel.send('내용이 할당되었습니다!')
            
        if i is False:

            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이없습니다".format(message.author.mention))

    if message.content.startswith('!공지'):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            
            await message.channel.send('베타기능이에요')
            await message.channel.purge(limit=2)
            
            embed = discord.Embed(title=f"{titi}", description=f"{scrip}", color=0xfaf4c0)

            await message.channel.send(embed=embed)
        
        if i is False:

            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이없습니다".format(message.author.mention))


    if message.content.startswith('!시험범위'):    #매크로로 쓴거다. 내가 직접 쓰지 않았음.
        index = message.content[6:]
        
        
        if index == "기하":
            setence = "1단원 ~ 3단원"

        elif index == "미적분":
            setence = "추가 예정"

        elif index == "화작":
            setence = "추가 예정"

        elif index == "프로그래밍":
            setence = "추가 예정"

        elif index == "지식재산일반":
            setence = "추가 예정"

        elif index == "생활과학":
            setence = "추가 예정"

        elif index == "영독작":
            setence = "추가 예정"

        elif index == "여행지리":
            setence = "추가 예정"

        elif index == "물리2":
            setence = "추가 예정"

        elif index == "화학2":
            setence = "추가 예정"

        elif index == "생명2":
            setence = "추가 예정"

        elif index == "심화국어":
            setence = "추가 예정"

        elif index == "영어권문화":
            setence = "추가 예정"

        else:
            setence = "!시험범위 + 기하, 미적분, 화작, 프로그래밍, 지식재산일반, 생활과학, 영독작, 여행지리, 물리2, 화학2, 생명2, 심화국어, 영어권문화 중 택1"
            
        embed=discord.Embed(color=0xff22, title= f"{index}", description= f"{setence}", timestamp=message.created_at)
        await message.channel.send(embed=embed) #출력
            

        
    if message.content.startswith('!안녕'):
        a = randint(1,100)
        if 1 <= a < 30:
            await message.channel.send('안녕하세요!!, {}님!'.format(message.author.mention))
        if 30 <= a < 60:
            await message.channel.send('안녕하세요, {}님 Chatdroid에요'.format(message.author.mention))
        if 60 <= a < 100:
            await message.channel.send('Hello, World!!')
            
    if message.content.startswith("!반란"):
        await message.channel.purge(limit=1)
        nme = message.content[4:]
        #if nme == "지빈" or "최지빈":
            #nme = "아버지한테 어케 욕해"
            
        be = randint(1,100)
        if 1 <= be < 30:
            bly = "씨발새끼야"
             

        if 30 <= be < 60:
            bly = "병신새끼야"
              

        if 60 <= be < 100:
            bly = "씹련아"
            
        #if be == 100:
            #bly = "불가"
           
        
        await message.channel.send(f"{nme} {bly}")
    
        
            

    if message.content.startswith ("!강조"):
       
        await message.channel.purge(limit=1)
        show = message.content[4:]
        await message.channel.send("{}님이 메시지를 강조했어요" .format(message.author.mention))
        embed = discord.Embed(description=f"{show}", color=0x72c1cc)
        await message.channel.send(embed=embed)
 


        
    if message.content.startswith('!잘가'):
        a = randint(1,3)
        if a == 1:
            await message.channel.send('다음에 또 만나요!!')
        if a == 2:
            await message.channel.send('안녕!!')
        if a == 3:
            await message.channel.send('bye!')
        
        

    if message.content.startswith('!작성언어'):
        await message.channel.send('저는 파이썬 기반으로 만들어졌어요!')
        
        
    if message.content.startswith('!급식'):
        await message.channel.send('시간이 약간 걸릴수 있어요..')
        url = "https://hiyedang.hs.kr/"

        res = requests.get(url,timeout = 30)    #학교 급식게시판 파싱
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml") 

        diet = soup.find_all("div", attrs={"class":"menu"})  #가져올 요소
        for diets in diet:
            result = diets.get_text() #텍스트만 추출
            
            await message.channel.purge(limit=1)
            
        result = get_diet()
        #await message.channel.send("어케 알아 씨발")
        embed=discord.Embed(color=0xff00, title= "오늘의 급식", description= f"{result}", timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        
    
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Chatdeletebot", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))


    if message.content.startswith('!논술'):    #매크로로 쓴거다. 내가 직접 쓰지 않았음.
        index = message.content[4:]
        
        
        if index == "부산대":
            setence = "논술전형 논술70 + 학생부30 \n[인문] 국,수,영,탐(1) 중 2개 합 4(경영-3개 합 6), 한 4 \n[자연] 국,수(미/기),영,과(1) 중 수포함 2개 합 5, 한 4"
            
        elif index == "울산대":
            setence = "논술60 + 학생부40 \n[의예] 국,수(미/기),영,과(2) 중 4개 합 5등급, 한국사 4"
            
        elif index == "경북대":
            setence = "논술(AAT)전형\n\n 논술70 + 학생부30\n[대부분] 국,수,영,탐(1) 중 2개 합 5 \n[농생/생과] 국,수,영,탐(1) 2개 합 6\n[생태/과학기술] 영3 혹은 1개 4등급 이내\n[의예/치의예] 국,수(미/기),영,과(2) 중 3개 합 3 \n[수의예/약학] 3개 합 5"
            
        elif index == "경기대(서울)":
            setence = "논술우수자\n\n 논술60 + 학생부40 \n최저 없음"
            
        elif index == "건국대":
            setence = "KU논술우수자\n\n 논술100 \n[인문] 국,수,영,탐(1) 중 2개 합 4 \n[자연] 국,수(미/기),영,과(1) 중 2개 합 5\n[수의] 국,수(미/기),영,과(1) 중 3개 합 4, 한 4 \n과학논술 폐지"
            
        elif index == "광운대":
            setence = "논술우수자\n\n 논술70 + 학생부30 \n 최저 없음"
            
        elif index == "덕성여대":
            setence = "논술전형 논술100 \n국,수,영,탐(1) 중 2개 합 7"
            
        elif index == "경희대":
            setence = "논술우수자 논술70 + 학생부30 \n[인문] 국,수,영,탐(1) 중 2개 합 5등급 \n[한의(인문)] 국,수,영,탐(1) 중 3개 합 4\n[자연] 국,수(미/기),영,과(1) 중 2개 합 5, 한 5 \n[의/한의/치의] 국,수(미/기),영,과(1) 중 3개 합 4, 한 5"
            
        elif index == "동국대":
            setence = "논술우수자 논술70 + 학생부30 \n[인문] 국,수,영,탐 2개 합 4(경찰-국수영 중) \n[자연] 국,수,영,과(1) 중 2개 합 5, 한 4\n[약학] 국,수(미/기),영,과(1) 중 3개 합 4, 한 4 \n[약] 수,과 필수 반영"
            
        elif index == "서강대":
            setence = "논술일반 논술80 + 학생부20 \n국,수,영,탐(1) 중 3개 합 6, 한 4"
            
        elif index == "서경대":
            setence = "SKU논술우수자전형\n\n 논술40 + 학생부60 \n최저 없음"
            
        elif index == "서울과기대":
            setence = "논술전형 논술70 + 학생부30 \n최저 없음"
            
        elif index == "서울시립대":
            setence = "논술전형 논술70 + 학생부30 \n최저 없음"
            
        elif index == "서울여대":
            setence = "논술우수자 논술80 + 학생부20 \n국,수,영 중 1개 3"
            
        elif index == "성균관대":
            setence = "논술우수 논술100\n[인문] 국,수,영,탐(1) 중 3개 합 6등급 \n[글로벌경영/경제/리더] 국,수,영,탐(1) 중 3개 합 5/n[자연] 국,수(미/기),영,과,과 중 3개 합 6\n[약/반도체/소프트/글로벌바이오] 국,수(미/기),영,과,과 중 3개 합 5 \n[의] 국,수(미/.기),영,과(2) 4개 합 5"
            
        elif index == "성신여대":
            setence = "논술우수자 논술70 + 학생부30 \n[인문] 국,수,영,탐(1) 중 2개 합 6등급 \n[자연] 국,수,영,탐(1) 중 2개 합 7"
            
        elif index == "세종대":
            setence = "논술우수자 논술70 + 학생부30 \n[인문] 국,수,영,탐(1) 중 2개 합 5등급 \n[자연] 국,수(미/기),영,과(1) 중 2개 합 6"
            
        elif index == "숙명여대":
            setence = "논술우수자 논술90 + 학생부10 \n국,수,영,사/과(1) 중 2개 합 5"
            
        elif index == "숭실대":
            setence = "논술우수자 논술60 + 학생부40 \n[인문/경상] 국,수,영,탐(1) 2개 합 4등급 \n[자연] 국,수(미/기),과(1) 중 2개 합 5"
            
        elif index == "연세대":
            setence = "논술전형 논술100 \n최저 없음"
            
        elif index == "이화여대":
            setence = "논술전형 논술70 + 학생부30 \n[인문] 국,수,영,탐(1) 중 3개 합 6등급 \n[스크랜튼] 국,수,영,탐(1) 중 3개 합 5\n[자연] 국,수(미/기),영,과(1) 중 수포함 2개 합 5"
            
        elif index == "중앙대":
            setence = "논술전형 논술70 + 학생부30 \n[인문] 국,수,영,탐(1) 중 3개 합 6등급 \n[자연] 국,수(미/기),영,과(1) 중 3개 합 6, 한 4\n[약학] 국,수(미/기),영,과(1) 4개 합 5, 史 4 \n[의예] 국,수(미/기),영,과(2) 4개 합 5, 한 4"
            
        elif index == "한국외대":
            setence = "논술전형 논술70 + 학생부30 \n국,수,영,탐(1) 2개 합 4 \n[L/D, L/T학부] 국,수,영,탐(1) 2개 합 3"
            
        elif index == "한양대":
            setence = "논술전형 논술90 + 학생부10 \n최저 없음"
            
        elif index == "홍익대":
            setence = "논술전형 논술90 + 학생부10 \n[인문] 국,수,영,탐(1) 중 3개 합 7, 한 4 \n[자연] 국,수(미/기),영,과(1) 중 3개 합 8, 한 4"
            
        elif index == "가천대":
            setence = "논술우수 논술60 + 학생부40 \n국,수,영,탐(1) 중 1개 3등급"
            
        elif index == "가톨릭대":
            setence = "논술우수자 논술70 + 학생부30 없음 \n[간호] 국,수,영,사/과(1) 중 3개 합 6 \n[약학] 국,수(미/기),영,과(1) 중 3개 합 5 \n[의] 3개 합 4, 한 4"
            
        elif index == "경기대":
            setence = "논술우수자 논술60 + 학생부40 \n최저 없음"
            
        elif index == "단국대":
            setence = "논술우수자 논술70 + 학생부30 \n최저 없음"
            
        elif index == "수원대":
            setence = "교과논술전형 논술60 + 학생부40 \n최저 없음"
            
        elif index == "아주대":
            setence = "논술우수자 논술80 + 학생부20 \n최저 없음"
            
        elif index == "한국공학대":
            setence = "논술우수자 논술80 + 학생부20 \n최저 없음"
            
        elif index == "한국외대(글로벌)":
            setence = "논술전형 논술70 + 학생부30 \n최저 없음"
            
        elif index == "한국항공대":
            setence = "논술우수자 논술100 \n[경영/소프트웨어/항공교통/항공운항/자유전공] 국,수,영,탐(1) 중 2개 합 5\n[항공우주기계공학/항공전자/항공재료] 국,수(미/기),영,과/직(1) 중 2개 합 6"
            
        elif index == "한양대(에리카)":
            setence = "논술전형 논술70 + 학생부30 \n최저 없음"
            
        elif index == "중앙대(안성)":
            setence = "논술전형 논술70 + 학생부30 \n[인문] 미실시 \n[자연] 국,수(미/기),영,과(1) 중 2개 합 5, 한 4"
            
        elif index == "인하대":
            setence = "논술우수자 논술70 + 학생부30 \n최저 없음"
            
        elif index == "연세대(미래)":
            setence = "논술전형 논술100\n[미래인재] 국,수,영,탐(1) 중 2개 합 6 \n[미래인재간호] 국,수,영,탐(1) 중 2개 합 4\n[창의인재] 국,수,영,과(1) 중 2개 합 6 \n[창의인재간호] 국,수,영,과(1) 중 2개 합 4\n[의예] 국,수(미/기),영,과,과 중 3개 1등급, 영 2, 史 4"
            
        elif index == "고려대(세종)":
            setence = "논술전형 논술70 + 학생부30 \n[인문] 국,수,영,탐(2) 중 1개 3 or 영 2 \n[자연] 국,수,과(2) 중 1개 3 or 영 2 \n[약학] 국,수(미/기),영,과(2) 중 3개 합 5"
            
        elif index == "홍익대(세종)":
            setence = "논술전형 논술90 + 학생부10 \n[인문] 미실시 \n[자연] 국,수(미/기),영,과(1) 중 1개 4"
            
        elif index == "한기대":
            setence = "논술일반전형 논술70 + 학생부30 \n최저 없음"
            
        else:
            setence = "논술전형을 실시하는 대학이 아니거나, 존재하지 않는 대학입니다.\n\n\n오타를 확인해보세요\n\n\n검색요령: ex) '한양대학교 에리카 검색시' ------> !논술 한양대(에리카)\n\n!논술과 대학이름사이에 공백이 있어야 검색이 가능합니다.\n\n\n\n\n\n\n정보가 누락되었거나, 오류는 제보해주세요"
            
        embed=discord.Embed(color=0xff22, title= f"🏫{index}", description= f"{setence}", timestamp=message.created_at)
        await message.channel.send(embed=embed) #출력
        
        
    if message.content.startswith('!운세'):
        a = randint(1, 100)
        if 1 <= a < 40:
            await message.channel.send('{}님은 오늘은 일이 잘풀릴거에요!'.format(message.author.mention))
        if 40 <= a < 75:
            await message.channel.send('{}님의 운세는... 그럭저럭!!'.format(message.author.mention))
        if 75 <= a <= 99:
            await message.channel.send('{}님, 오늘은 조심하는게 좋겠어요..'.format(message.author.mention))
        if 99 < a <= 100:
            #이스터에그
            embed=discord.Embed(color=0xff22, title= "이스터에그!", description= "행운이란 준비와 기회를 만났을 때 나타난다", timestamp=message.created_at)
          
            await message.channel.send(embed=embed)
            await asyncio.sleep(1)
            await message.channel.send('{}님, 1%의 확률에 당첨되셨습니다!!!'.format(message.author.mention))
            
            
            



    if message.content.startswith('!안내'):
        await message.channel.purge(limit=1) 
        
        noti = "\n\n\n안녕하세요 학급도우미 삼일이에요!!!\n\n\n<명령어 기능>\n\n\!논술+대학이름 --> 23년도 모든 논술실시대학의 논술전형정보를 제공합니다\n\n!운세 --> 간단하게 오늘의 운을 시험해보세요!\n\n!강조+문자내용 --> 메세지를 강조해드립니다, 설문조사홍보나 홍보활동을 강조해보세요!\n\n!청소+숫자 --> 입력한 숫자만큼 메시지를 삭제합니다.(관리자만) 효과적으로 방을 관리하세요.\n\n!d6 --> 주사위를 굴려요\n\n!농담해줘 --> 농담을 해드려요, 단, 봇이 거절할 수도 있어요!\n\n!시간표 --> 오늘 시간표를 알려드립니다(오전9시에 업데이트됩니다.)\n\n!시험범위+과목명 --> 해당 과목의 시험범위를 알려드립니다.\n\n\n<베타기능>\n임베드로 공지사항을 강조해 효과적인 공지사항을 제작하세요(관리자 전용)!!\n\n이용방법\n\n!제목 --> 임베드의 제목을 정해요\n\n!내용 --> 임베드의 내용을 정해요\n\n!공지 --> 임베드를 출력해요\n\n!한영+영어로 번역하고 싶은 한국어 --> 한국어를 영어로 번역\n\n\n\n개인서버에서 초대해 쓰고싶으면 지빈#1638으로 갠디코 주세요\n\n\n\n\n31BOT.ver.beta.4"
        
        embed=discord.Embed(color=0xff00, title= "📌안내", description= f"{noti}", timestamp=message.created_at)
        await message.channel.send(embed=embed)
        



    if message.content.startswith('!help'):
        await message.channel.send("<도움말>\n\n\n\!한영+한국어문장 --> 한국어를 영어로 번역\n\n!논술+대학이름 --> 해당 대학 논술전형\n\n!운세 --> 운을 봐드림\n\n!강조+하고싶은말 --> 메시지강조\n\n!청소+숫자 --> 입력한 숫자만큼 메시지 삭제(관리자만)\n\n!d6 --> 주사위를 굴려드림\n\n!농담해줘 --> 농담을 해드려요\n\n!시간표 --> 오늘 시간표를 알려드립니다\n\n!시험범위+과목명 --> 해당 과목의 시험범위를 알려드립니다.\n\n<관리자용 공지기능>\n\n먼저 !제목+원하는 제목으로 공지할 내용의 제목을 설정하세요(ex)!제목 수행안내\n\n!내용+공지내용을 통해 공지할 내용을 설정하세요!(ex)!내용 미적분수행\n\n!공지를 통해 공지를 하면 됩니다.")
        



    if message.content.startswith('!농담'):
        que = ["오리가 얼면? ", "딸기가 직장을 잃으면?", "세상에서 가장 억울한 도형은?", "아몬드가 죽으면?", "토끼가 쓰는 빗은?", "토끼가 강한 이유는?", "삶은?", "11월에 뱀이랑 벌이 없는 이유는?", "가장 폭력적인 동물은?", "스님이 못가는 대학교는?"]
        ans = ["언덕", "딸기시럽", "원통", "다이아몬드", "레빗", "깡과 총이 있어서", "계란", "노뱀벌", "팬다", "중앙대"]
        yn = randint(1, 100)
        shy = randint(1, 4)
        
        if 1 <= yn < 10:
            await message.channel.send("시스템 오류!")
            await asyncio.sleep(0.7)
            await message.channel.send("(그렇게 믿어주세요 제발)")
            
       
            
            
        if 10 <= yn < 40:
            hate = randint(0,5)
            nongdam = ["급식 알려주는", "공지 해주는", "논술전형 정보 알려주는", "운세 봐주는", "시간표 알려주는", "시험범위 알려주는"]
            angry = nongdam[hate]      #농담 대신 다른걸 해보죠^^ (부글부글)
            await message.channel.send("농담이 뭐죠?")
            await asyncio.sleep(0.7)
            await message.channel.send(f"대신 {angry}건 잘할것 같은데?")
            
        if 40 <= yn < 50:
            await message.channel.send("로봇은...농담을 못한답니다!")
            await message.channel.send("^^::")
        
        if 50 <= yn <= 100:
            x = randint(0, 9)
            oops = que[x]
            wow = ans[x]
            
            
            if shy == 1:
                sorry = "잘...했나요...?"
        
            if shy == 2:
                sorry = "(분위기가 얼어버린듯 하다)"
            
            if shy == 3:
                sorry = "다시는 안할거에요!! 으악!"
            
            if shy == 4:
                sorry = "죄송해요...못본걸로 해주세요..."
                
                
            await message.channel.send(f"{oops}")
            await asyncio.sleep(2)
            await message.channel.send(f"{wow}")
            await asyncio.sleep(0.7)
            await message.channel.send(f"{sorry}") #삼일이는 농담을 매우 못한답니다..
            
        
            
        
 
        


access_token = os.environ["BOT_TOKEN"]

client.run(access_token)








