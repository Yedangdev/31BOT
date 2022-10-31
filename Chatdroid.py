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
from datetime import datetime
from pytz import timezone



client = discord.Client()
@client.event
async def on_ready():
    print('봇 온라인!')
    print('업데이트에 성공하였습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    update = datetime.now(timezone('Asia/Seoul')).strftime("%p%Y%m%d%H%M")
    print(update)
        
    await client.change_presence(status=discord.Status.online) #온라인
    
    while not client.is_closed():
        await client.change_presence(activity=discord.Game(name="!도움말"))        
        await asyncio.sleep(5)
        latancys = client.latency
        lateninfo = round(latancys * 1000)
        if lateninfo < 35:
            botst = "정상"
        if 35 < lateninfo < 60:
            botst = "양호"
        if lateninfo > 60:
            botst = "트래픽 주의"
        
        await client.change_presence(activity=discord.Game(name=f"{lateninfo}ms {botst}"))
        await asyncio.sleep(5)
        

        


@client.event
async def on_message(message):
    
    global titi
    global scrip
    global timetble
    
    

        
    if message.content.startswith("!한강"):
        
        headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}   
        
        url = "https://hangang.ivlis.kr/aapi.php?type=dgr"
        res = requests.get(url,timeout = 25)    #파싱
        res.raise_for_status()
        
        soup = BeautifulSoup(res.text, "lxml")
        temp = soup.get_text()
        curse = ["자신의 하루를 마지막 날이라고 생각하라. -호라티우스", "해가 뜨지 않는 날은 절대 없다. -셀이아 박스터", "벽을 내려치느라 아까운 시간을 낭비하지말라 -할 에로드", "열정이 없다면 성취도 없다. -마이클 조던", "만약 어제 넘어졌다면 오늘은 일어서라 -H. G. Wells"]
        randcr = randrange(0,4)
        curre = curse[randcr]
        
        
        embed = discord.Embed(title="**실시간 한강 수온**", description = f"**🌡{temp}**\n\n*{curre}*", color=0x7289da)     #+"\n[좋은 노래! 🔗](<https://m.youtube.com/watch?v=5kbP23jYsNs&vl=ko>)\n "
        embed.set_footer(text = f"출처: ivlis")
        
        await message.channel.send(embed=embed)
       
    
    if message.content.startswith("!명예개발자"):
      await message.channel.purge(limit=1)
      king = "👑지빈#1638"
      pons = "♟️eden01010#3983\n♟️이서진#5397\n♟️윤달#7075"
      embed = discord.Embed(title="**🌿🏆명예의 전당🏆🌿**", description = f"{king}\n\n{pons}\n\n진심으로 감사드립니다.🙏", color=0xff0000)
      await message.channel.send(embed=embed)
    
    
    if message.content.startswith("!마법의 소라고둥님"):
        
        await message.channel.purge(limit=1)
        words = ["돼!", "안돼!", "포기해!", "다시 한 번 물어봐!", "허락할게!", "당장 시작해!", "나중에 해!", "안.돼.", "하지마!", "그래!", "가만히 있어!.", "그것도 안 돼!", "아니!", "응!", "하고 싶은 대로 해!", "그것도 하지마!", "맘대로 해!","꿈도 꾸지 마!","기다려!","왜?"]
        
        sora = randrange(0,19)
        sorare = words[sora]
        
        say = message.content[1:]
        #await message.channel.send("https://media.discordapp.net/attachments/986620556675776532/994980964855992330/Screenshot_20220708-232742_Samsung_Notes.jpg")
        await message.channel.send(f"{say}?")
        await asyncio.sleep(0.2)
        #await message.channel.send("https://media.discordapp.net/attachments/986620556675776532/994980964855992330/Screenshot_20220708-232742_Samsung_Notes.jpg")
        embed = discord.Embed(title="**🐚마법의 소라고둥은 대답했다!**", description = f"\n\n**{sorare}**\n\n{message.author.mention}은 깨달음을 얻었다!🤔\n\n```!s으로도 질문이 가능합니다!```", color=0x7289da)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/986620556675776532/994980964855992330/Screenshot_20220708-232742_Samsung_Notes.jpg")
        await message.channel.send(embed=embed)
        
        
    
    if message.content.startswith("!s"):
        
        await message.channel.purge(limit=1)
        words = ["돼!", "안돼!", "포기해!", "다시 한 번 물어봐!", "허락할게!", "당장 시작해!", "나중에 해!", "안.돼.", "하지마!", "그래!", "가만히 있어!.", "그것도 안 돼!", "아니!", "응!", "하고 싶은 대로 해!", "그것도 하지마!", "맘대로 해!","꿈도 꾸지 마!","기다려!","왜?"]
        
        sora = randrange(0,19)
        sorare = words[sora]
        
        say = message.content[3:]
        #await message.channel.send("https://media.discordapp.net/attachments/986620556675776532/994980964855992330/Screenshot_20220708-232742_Samsung_Notes.jpg")
        await message.channel.send(f"마법의 소라고둥님 {say}?")
        await asyncio.sleep(0.2)
        #await message.channel.send("https://media.discordapp.net/attachments/986620556675776532/994980964855992330/Screenshot_20220708-232742_Samsung_Notes.jpg")
        embed = discord.Embed(title="**🐚마법의 소라고둥은 대답했다!**", description = f"\n\n**{sorare}**\n\n{message.author.mention}은 깨달음을 얻었다🤔", color=0x7289da)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/986620556675776532/994980964855992330/Screenshot_20220708-232742_Samsung_Notes.jpg")
        await message.channel.send(embed=embed)
        
        
        
    if message.content.startswith("!ping"):
        latancy = client.latency
        
        await message.channel.send(f"```python\npong! {round(latancy * 1000)}ms```") 
    
    
    if message.content.startswith("!new"):
        await message.channel.purge(limit=1)
        
        #newfx = "!수시+대학이름\n34개의 인서울권 대학의 수시정보를 보여줍니다\n(송성훈을 갈아만들었습니다.)\n\n!반란+욕하고 싶은 사람\n봇이 욕을 대신해줍니다!\n\n!한일,!한영,!일한,!영한+번역하고자하는 내용\n번역을 해드립니다.\n\n!ping\n봇의 레이턴시정보를 제공합니다\n\n!전적+소환사이름\nopgg사이트 바로가기를 보여줍니다.\n\n!마법의 소라고둥님+하고싶은질문\n마법의 소라고둥이 질문에 대해 답해줍니다.\n소라고둥의 답은 깊은 뜻을 가지고 있습니다.\n(이서진을 갈아만들었습니다.)"
        
        embed = discord.Embed(title="**새로운 기능!**", description = f"**새로 추가된 기능이 없습니다**\n ```!도움말```로 명령어를 확인하세요!", color=0x7289da)
        await message.channel.send(embed=embed)
        
    
    if message.content.startswith("!수시"):
        founddict = message.content[4:]
               
        embed = discord.Embed(title="검색실패", description = "EFT msg: 해당 서비스는 지원종료되었습니다. 이용해주셔서 감사합니다.", color = 0x7289da)
        await message.channel.send(embed=embed)
        

    
    
    if message.content.startswith("!반란"):
        await message.channel.purge(limit=1)
        nme = message.content[4:]
        
        be = randint(1,100)
        if 1 <= be < 10:
            bly = "씨발새끼야"       
        if 10 <= be <50:
            bly = "윤달은 신이야!!"
        if 50 <= be < 60:
            bly = "병신새끼야"              
        if 60 <= be <= 99:
            bly = "씹련아"
        if be == 100:
            bly = "개씨발새끼야 나가 뒤져라 제발좀"
        
        if message.author.id == 714351331464314932:
            bly = "개새끼야"
            nme = "임건우"
        
        
        if nme == "지빈":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
        
        if nme == "최지빈":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
        
        if nme == "장혁진":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
        
        if nme == "혁진":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
            
        if nme == "윤달":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
            
        if nme == "지환":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
            
        if nme == "":
            bly = f"{nme}에게 욕을 할 수 없습니다."
            nme = message.author.mention
           
        
            
        await message.channel.send(f"**{nme} {bly}**")
    
    if message.content.startswith("!한영"):
      text1 = message.content[4:]
      translator = Translator()
      trans1 = translator.translate(text1, src='ko', dest='en')
      tran1 = trans1.text
      
      embed = discord.Embed(title="**📖한국어를 영어로 번역했어요**", description = f"{tran1}", color=0x7289da)
      embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/986620628687798282/997323776809246900")
      await message.channel.send(embed=embed)
      #await message.channel.send("번역결과: {}" .format(trans1.text))

    
    if message.content.startswith("!한일"):
      text1 = message.content[4:]
      translator = Translator()
      trans2 = translator.translate(text1, src='ko', dest='ja')
      tran2 = trans2.text
      
      embed = discord.Embed(title="**📖한국어를 일본어로 번역했어요**", description = f"{tran2}" ,color=0x7289da)
      embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/986620628687798282/997323776809246900")  
      await message.channel.send(embed=embed)
      #await message.channel.send("번역결과: {}" .format(trans2.text))
      
    
    if message.content.startswith("!번역"):
      text1 = message.content[4:]
      translator = Translator()
      await message.channel.send("언어감지완료!")
      await asyncio.sleep(0.5)
      await message.channel.purge(limit=1)
        
      #await message.channel.send(translator.detect(f"{text1}"))
      
      trans3 = translator.translate(text1, dest='ko')
      tran3 = trans3.text
      embed = discord.Embed(title="**📖번역결과**", description = f"{tran3}" , color=0x7289da)
      embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/986620628687798282/997323776809246900")
      embed.set_footer(text = translator.detect(f"{text1}"), icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
      #await message.channel.send("번역결과: {}" .format(trans3.text))
         
  
    if message.content.startswith('!312안녕'):
        embed = discord.Embed(title="**EasterEgg_file_load_process**", description = "Chatdroid_memory", color=0x7289da)
        #embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/983342486812516416/986281059345924167")
        await message.channel.send(embed=embed)
        await message.channel.send("https://media.discordapp.net/attachments/986620556675776532/986638305724620800/Easter_egg_312_1.jpg\nhttps://media.discordapp.net/attachments/986620556675776532/986639756333043753/Easter_egg_312_2.jpg")
        
        
    if message.content.startswith('!d6'):  
        await message.channel.send("**{}님이 주사위를 굴렸어요!**" .format(message.author.mention))
        dice = randint(1,6)
        embed = discord.Embed(title="주사위 결과", description = f"🎲{dice}이(가) 나왔습니다!", color=0x7289da)
        await message.channel.send(embed=embed)

        
    if message.content.startswith('!시간표'):
        
        timesrch = message.content[5:]
            
            
            
            
        if len(timesrch) == 0:
            
            timetiti = "오늘의"
            
            localset = datetime.now(timezone('Asia/Seoul')).strftime("%H")
            utcset = datetime.now(timezone("utc")).strftime("%H")
        
            wday = time.localtime().tm_wday
            if 0 <= int(localset) <= 8:
                if int(utcset) - int(localset) == 15:
                    if wday == 6:
                        rewday = 0
                    else:
                        rewday = wday + 1    #시간 보정
            else:
                rewday = wday	
        
        
            if rewday == 0:
                timetble = '**월요일**\n\n프로\n기하\n미적\n논술\n심독작\n물리2\n생명2'
            
            elif rewday == 1:
                timetble = '**화요일**\n\n기하\n미적\n여지\n심국\n심독작\n생명2\n프로'
            
            elif rewday == 2:
                timetble = '**수요일**\n\n미적\n심독작\n프로\n여지\n생명2\n물리2\n논술'
            
            elif rewday == 3:
                timetble = '**목요일**\n\n미적\n스포\n심국\n진로\n심독작\n물리2\n여지'
            
            elif rewday == 4:
                timetble = '**금요일**\n\n자율3\n심국\n스포\n기하\n자봉\n동아'
            
            elif rewday == 5:
                timetble = '오늘은 토요일입니다!'
            
            elif rewday == 6:
                timetble = '오늘은 일요일입니다!'
        
        if len(timesrch) > 1:
            timesrch = message.content[5]
        
        
        if len(timesrch) == 1:
            
            timetiti = "검색한"
            
            if timesrch == "월":
                timetble = '**월요일**\n\n프로\n기하\n미적\n논술\n심독작\n물리2\n생명2'
            
            if timesrch == "화":
                timetble = '**화요일**\n\n기하\n미적\n여지\n심국\n심독작\n생명2\n프로'
            
            if timesrch == "수":
                timetble = '**수요일**\n\n미적\n심독작\n프로\n여지\n생명2\n물리2\n논술'
            
            if timesrch == "목":
                timetble = '**목요일**\n\n미적\n스포\n심국\n진로\n심독작\n물리2\n여지'
             
            if timesrch == "금":
                timetble = '**금요일**\n\n자율3\n심국\n스포\n기하\n자봉\n동아'
            
            if timesrch == "토":
                timetble = '오늘은 토요일입니다!'
            
            if timesrch == "일":
                timetble = '오늘은 일요일입니다!'
            
            
            
        embed = discord.Embed(title=f"**📃{timetiti} 시간표**", description=f"{timetble}\n\n\n"+"[이곳을 눌러 전체시간표 열람](<https://media.discordapp.net/attachments/1007568791116460073/1007568838180741160/IMG_2534.png>)"+"```python\nKST(00:00)에 갱신됩니다```", color = 0x7289da)
        embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/983342486812516416/986418832526684241")
        await message.channel.send(embed=embed)
        #await message.channel.send("https://media.discordapp.net/attachments/1007568791116460073/1007568838180741160/IMG_2534.png")
        


    if message.content.startswith('!titi'):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            
            await message.channel.purge(limit=1)
            titi = message.content[4:]
            await message.channel.send('제목이 할당되었습니다!')
            
        if i is False:

            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이없습니다".format(message.author.mention))


    if message.content.startswith('!noti'):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            
            await message.channel.purge(limit=1)
            scrip = message.content[4:]
            await message.channel.send('내용이 할당되었습니다!')
            
        if i is False:

            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이없습니다".format(message.author.mention))

    
        
    if message.content.startswith('!안녕'):
        a = randint(1,100)
        if 1 <= a < 30:
            await message.channel.send('안녕하세요!!, {}님!'.format(message.author.mention))
        if 30 <= a < 60:
            await message.channel.send('안녕하세요, {}님 Chatdroid에요'.format(message.author.mention))
        if 60 <= a < 100:
            await message.channel.send('Hello, World!!')
            
   
        
            

    if message.content.startswith ("!강조"):
       
        await message.channel.purge(limit=1)
        show = message.content[4:]
        await message.channel.send("{}님이 메시지를 강조했어요" .format(message.author.mention))
        embed = discord.Embed(description=f"{show}", color=0xff00)
        await message.channel.send(embed=embed)
 


        
    if message.content.startswith('!잘가'):
        a = randint(1,3)
        if a == 1:
            await message.channel.send('다음에 또 만나요!!')
        if a == 2:
            await message.channel.send('안녕!!')
        if a == 3:
            await message.channel.send('bye!')
        
        

    if message.content.startswith('!정보'):
        
        latancys = client.latency
        lateninfo = round(latancys * 1000)
        
        infobot = f"**개발언어:**  Python3\n\n**모듈정보:** discord.py 1.7.3(구버전)\n\n**Cog수:** 구버전은 지원되지 않음\n\n**레이턴시: **{lateninfo}ms\n\n**서비스기한:** (2023년 3월 1일까지 지원), 서비스종료 이후 리뉴얼예정\n\n\n\n**<뉴비개발자들을 위한 도움>**\n\n**봇개발에 입문하는 개발자는 Chatdroid 소스코드자료를 요청할 수 있습니다**\n\n소스코드 요청은 공식서포트채널에서 요청할 수 있습니다.\n-단 소스코드는 Chatdroid(beta)의 소스코드로 2.0.0에서 지원하는 몇가지 기능이 빠져있는 소스코드입니다.\n-봇 토큰은 제공하지 않습니다.\n-해당 소스코드는 재배포가 가능합니다.(출처 밝힐 필요X, 단, 상업용도 사용은 일절금지)\n-소스코드는 Vscode에서 작성되었습니다."
        
        embed = discord.Embed(title=f"봇 정보", description=f"{infobot}", color=0xff0000)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/984777197506162748/985181219329294376/Screenshot_20220610-224533_Samsung_Notes-removebg-preview.jpg")
        await message.channel.send(embed=embed)
        
        
        
        
    if message.content.startswith('!급식'):
        
        randnum = randint(1, 3)
        
        if randnum == 1:
            what = "그거 아시나요? 급식기능은 PIXIV 크롤러를 변형하여 만들었답니다."
            
        if randnum == 2:
            what = "그거 아시나요? 임건우는 로리콘입니다."
        
        if randnum == 3:
            what = "2023-03-01 서비스는 종료됩니다."
        
        await message.channel.send(f'```python\nneis api 로딩중...\n{what}```')
        await asyncio.sleep(2.5)
        await message.channel.purge(limit=2)
        
        start = time.time()
        dietdate = message.content[4:]
        
        if len(dietdate) == 0:
            dietdate = datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")
        
        headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}          
        url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7530849&MLSV_YMD={dietdate}"
        res = requests.get(url,timeout = 25)    #파싱
        res.raise_for_status()
        
        soup = BeautifulSoup(res.text, "xml")

        diet = soup.find_all("DDISH_NM")

        for diets in diet:
            dietre = diets.get_text()
            
        try:
            dietpr = dietre
            #hexcde = "0x7289da"
        
        except NameError:
            dietre = "**검색에 실패하였습니다**\n\n**오타를 확인해보세요!**\n검색요령ex) ```!급식 20220921``` --> 2022년09월21일의 급식정보"
        
        dietpr = dietre.replace("<br/>", "\n")
        
        if dietdate == datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d"):
            titledate = "🍴**오늘의**"
        
        else:
            titledate = f"🍴{dietdate[:4]}/{dietdate[4:6]}/{dietdate[6:]}"
        
        
        if dietre == "**검색에 실패하였습니다**\n\n**오타를 확인해보세요!**\n검색요령ex) ```!급식 20220921``` --> 2022년09월21일의 급식정보":
            titledate = "**⚠️존재하지 않는**"
            #hexcde = "0x0xff0000"
        end = time.time()
        
        embed=discord.Embed(color= 0x7289da, title= f"{titledate} **급식표**", description= f"{dietpr}\n\n\n```python\nKST(00:00)에 갱신됩니다```", timestamp=message.created_at)
        embed.set_footer(text= f"{end - start:.2f}초 소요")
        await message.channel.send(embed=embed)
    
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="**메시지 삭제 알림**", description="```디스코드 채팅 {}개가\n관리자 {}님의 요청으로 삭제되었습니다```".format(amount, message.author), color=0xff00)
            embed.set_footer(text="관리자에 의한 메시지 삭제")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}님은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))


    if message.content.startswith('!논술'):
        index = message.content[4:]     
        embed=discord.Embed(color= 0x7289da, title= "검색실패", description= "EFT msg: 해당 서비스는 종료되었습니다, 이용해주셔서 감사합니다.")
        await message.channel.send(embed=embed) #출력
        
        
    if message.content.startswith('!운세'):
        
        b = message.content[4:]
        if b == ".":
            
            await message.channel.purge(limit=1)
            
            embed=discord.Embed(color=0x7289da, title= "**이스터에그!**", description= "행운이란 준비와 기회를 만났을 때 나타난다", timestamp=message.created_at)
          
            await message.channel.send(embed=embed)
            await asyncio.sleep(1)
            await message.channel.send('{}님, 1%의 안티치트를 사용하셨습니다!!!'.format(message.author.mention))
         
        
        if b == "":
            a = randint(1, 100)
            if 1 <= a < 40:
                await message.channel.send('{}님은 오늘은 일이 잘풀릴거에요!'.format(message.author.mention))
            if 40 <= a < 75:
                await message.channel.send('{}님의 운세는... 그럭저럭!!'.format(message.author.mention))
            if 75 <= a <= 99:
                await message.channel.send('{}님, 오늘은 조심하는게 좋겠어요..'.format(message.author.mention))
            if 99 < a <= 100:
            #이스터에그
                embed=discord.Embed(color=0xff0000, title= "**이스터에그!**", description= "행운이란 준비와 기회를 만났을 때 나타난다", timestamp=message.created_at)
          
                await message.channel.send(embed=embed)
                await asyncio.sleep(1)
                await message.channel.send('{}님, 1%의 확률로 당첨되셨습니다!!!'.format(message.author.mention))
            
            
            



    if message.content.startswith('!도움말'):
        #await message.channel.purge(limit=1)
        if message.author.dm_channel:

            #channel = await message.author.create_dm()
            noti = "\n\n\n**<Chatdroid 명령어>**\n\n**!급식** or **!급식** + 년/월/일 --> 급식정보를 제공합니다.\n\n**!반란** + 욕하고 싶은 사람 --> 봇이 욕을 대신해줍니다!\n\n**!한일,!한영,!번역** + 번역하고자하는 내용 --> 번역을 해드립니다.\n\n**!ping** --> 봇의 레이턴시정보를 제공합니다\n\n**!전적** + 소환사이름 --> opgg사이트 바로가기를 보여줍니다.\n\n**!롤토** + 소환사이름 --> lolchess.gg사이트 바로가기를 보여줍니다.\n\n**!마법의 소라고둥님** or **!s** + 하고싶은질문 --> 마법의 소라고둥이 질문에 대해 답해줍니다.\n소라고둥의 답은 깊은 뜻을 가지고 있습니다.\n\n**!한강** --> 한강의 수온을 실시간으로 확인해보세요, 유용할겁니다!\n\n**!운세** --> 간단하게 오늘의 운을 시험해보세요!\n\n**!강조** + 문자내용 --> 메세지를 강조해드립니다, 설문조사홍보나 홍보활동을 강조해보세요!\n\n**!청소** + 숫자 --> 입력한 숫자만큼 메시지를 삭제합니다.(관리자만) 효과적으로 방을 관리하세요.\n\n**!d6** --> 주사위를 굴려요\n\n**!시간표** --> 오늘 시간표를 알려드립니다(오전9시에 업데이트됩니다.)\n\n\n\n개인서버에서 초대해 쓰고싶으면 지빈#1638으로 갠디코 주세요\n\n\n\n\n```Chatdroid.ver.2.0.0```"
            
            embed=discord.Embed(color=0x7289da, title= "📌도움말", description= f"{noti}", timestamp=message.created_at)
            await message.author.dm_channel.send(embed=embed)
            await message.channel.send("```python\nCheck your DM!```")
            
        if message.author.dm_channel is None:
            channel = await message.author.create_dm()
            noti = "\n\n\n**<Chatdroid 명령어>**\n\n**!급식** or **!급식** + 년/월/일 --> 급식정보를 제공합니다.\n\n**!반란** + 욕하고 싶은 사람 --> 봇이 욕을 대신해줍니다!\n\n**!한일,!한영,!번역** + 번역하고자하는 내용 --> 번역을 해드립니다.\n\n**!ping** --> 봇의 레이턴시정보를 제공합니다\n\n**!전적** + 소환사이름 --> opgg사이트 바로가기를 보여줍니다.\n\n**!롤토** + 소환사이름 --> lolchess.gg사이트 바로가기를 보여줍니다.\n\n**!마법의 소라고둥님** or **!s** + 하고싶은질문 --> 마법의 소라고둥이 질문에 대해 답해줍니다.\n소라고둥의 답은 깊은 뜻을 가지고 있습니다.\n\n**!한강** --> 한강의 수온을 실시간으로 확인해보세요, 유용할겁니다!\n\n**!운세** --> 간단하게 오늘의 운을 시험해보세요!\n\n**!강조** + 문자내용 --> 메세지를 강조해드립니다, 설문조사홍보나 홍보활동을 강조해보세요!\n\n**!청소** + 숫자 --> 입력한 숫자만큼 메시지를 삭제합니다.(관리자만) 효과적으로 방을 관리하세요.\n\n**!d6** --> 주사위를 굴려요\n\n**!시간표** --> 오늘 시간표를 알려드립니다(오전9시에 업데이트됩니다.)\n\n\n\n개인서버에서 초대해 쓰고싶으면 지빈#1638으로 갠디코 주세요\n\n\n\n\n```Chatdroid.ver.2.0.0```"

            
            embed=discord.Embed(color=0x7289da, title= "**📌도움말**", description= f"{noti}", timestamp=message.created_at)
            await message.author.dm_channel.send(embed=embed)
            await message.channel.send("```python\nCheck your DM!```")
                

    if message.content.startswith("!롤토"):
        chess = message.content[4:]
        
        await message.channel.send("```python\n시간이 조금 걸려요...```")
        await asyncio.sleep(1.5)
        await message.channel.purge(limit=2)
        
        headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}   
        
        url = f"https://lolchess.gg/profile/kr/{chess}?save=true"
        res = requests.get(url,timeout = 25)    #파싱
        res.raise_for_status()
        
        soup = BeautifulSoup(res.text, "lxml")
        
        rank = soup.find("div", {"class":"profile__tier__icon"}).find("img").get("src")
        rank2 = soup.find("div", {"class":"profile__tier__icon"}).find("img").get("alt")
        rank4 = soup.find_all("div", {"class":"tier-ranked-info__content"})        
        
        for rank4s in rank4:
        	rank4re = rank4s.get_text()
        
        rank4re = rank4re.replace(" ", "")
        
        embed = discord.Embed(title=f"**{chess}**님의 전적!🎮", description = f"**<Lolchess.gg 바로가기>**\n**https://lolchess.gg/profile/kr/{chess}?save=true**", color=0x7289da)
        embed.add_field(name="**<Tier info>**", value = f"**{rank2}**", inline=True)
        embed.add_field(name=f"**<Other Tier>**", value = f"```python\n{rank4re}```", inline=True)
        embed.set_thumbnail(url=f"https:{rank}")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        

    if message.content.startswith('!전적'):
      
      await message.channel.send("```python\n시간이 조금 걸려요...```")
      await asyncio.sleep(0.7)
      await message.channel.purge(limit=2)
      
      msg = message.content[4:]
      headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}  
      url = f"https://www.lolog.me/kr/user/{msg}?save=true"  #lolog.me라는 url

      res = requests.get(url,timeout = 25)    
      res.raise_for_status()
      soup = BeautifulSoup(res.text, "lxml") 

#랭크정보
      flexrank = soup.find_all("div", attrs={"class":"profile-rank"})  #자유랭크

      for rank1 in flexrank:
        flexRankResult = rank1.get_text() #텍스트만 추출

      solorank = soup.find_all("div", attrs={"id":"user-ranks"})  #솔로랭크
      
      for rank2 in solorank:
        cnt = rank2.get_text() #텍스트만 추출

      
      soloRankResult = cnt[5:49]

#소환사이미지      
      img = soup.find("div", attrs={"id":"user-profile-bio-img"}).find("img").get('src') #소환사이미지 가져오기
      
      
      embed = discord.Embed(title=f"**{msg}**님의 전적!🎮", description = f"**<OP.GG 바로가기>**\n**https://www.op.gg/summoners/kr/{msg}**", color=0x7289da)
      embed.add_field(name="**<솔로랭크>**", value=f"```python\n{soloRankResult}```\n", inline=True)
      embed.add_field(name="**<자유랭크>**", value=f"```python\n{flexRankResult}```", inline=True)
      #embed.add_field(name="전적사이트 바로가기!", value=f"https://www.op.gg/summoners/kr/{msg}", inline=)
      embed.set_thumbnail(url=f"{img}")
      embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
      await message.channel.send(embed=embed)
      #await message.channel.send("beta")

    #dev func
    #Bot presence set
    if message.content.startswith("!onprtcl"):
        if message.author.id == 833697465319948361:
        
            await message.channel.send("online set")
            await client.change_presence(status=discord.Status.online)
            await client.change_presence(activity=discord.Game(name="!도움말"))
        else:
            embed = discord.Embed(title="**unauthenticated user error**", description = "```Invalid user```", color=0xff0000)
            await message.channel.send(embed=embed)
        
    if message.content.startswith("!byeprtcl"):
        await message.channel.purge(limit=1)
        if message.author.id == 833697465319948361:
                    
            def check(m):      
                return m.author == message.author and m.channel == message.channel

            embed=discord.Embed(color=0xff0000, title= "**종료 프로토콜을 실행하시겠습니까?**", description= "**옵션1**  Chatdroid를 입력해 종료\n**옵션2**  아무 키를 눌러 취소\n\n**⚠️경고⚠️**\n서버와 연결을 종료하면 봇 내부에 저장된 변수들이 모두 초기화됩니다.")
            await message.channel.send(embed=embed)
    	
    	   
            try:
                msg = await client.wait_for("message", check=check, timeout=30)
            
                if msg.content == "Chatdroid":
                    await message.channel.send("```서버와 연결종료를 선택하셨습니다.```")
                    print("서버 종료 절차가 실행되었습니다.")
                    await message.channel.send("```서버와 연결종료 절차를 실행합니다.```")
                    print("종료절차 진입")
               
                    await message.channel.send("```오프라인으로 설정중...```")
                    time.sleep(2)
                
                    await client.change_presence(status=discord.Status.offline) #오프라인    
                    await message.channel.send("```봇이 절전상태에 진입했습니다,.```")
                    print("1번 절차 성공")
                
                    await message.channel.send("```서버와 연결을 종료하는중...```")
                    time.sleep(2)
                    await message.channel.send("```Heroku와의 연결이 종료되었습니다.```")
                    print("최종 단계 성공")
                
                    await message.channel.send("```봇이 정지되었습니다.```")
                    print("봇이 정지되었습니다.")
                    await client.close()
                
                               
            
                else:
                    await message.channel.send("```서버와 연결종료를 취소하셨습니다.```")

        
            except asyncio.exceptions.TimeoutError:
                await message.channel.purge(limit=1)
                await message.channel.send("```시간이 초과되었습니다.\n재시도 해주세요.```")

        else:
            embed = discord.Embed(title="**⚠️Master Caution!⚠️**", description = f"**보안 위협 감지**\n```미인증 유저가 봇 관리 명령어에 접근했습니다.```\n**{message.author.mention}**", color=0xff0000)
            await message.channel.send(embed=embed)
        
        
    if message.content.startswith("!why"):
        if message.author.id == 833697465319948361:
                   
            embed = discord.Embed(title="**서비스종료 전 공지**", description = "**Chatdroid는 5일 뒤 서비스종료 예정임을 공지합니다.**\n\n**<서비스종료를 하는 이유>**\n\n**구버전의 discord.py에서 작성되었기 때문**\ndiscord.py ext가 아니여서 코드가 ㅈㄴ지저분합니다. 따라서 단점이 굉장히 많습니다.\n\n**<단점들>**\n\n1. Cogs 미지원(봇 스크립트를 여러 파일과 연결해 개발할 수 있게 돕는것)\n2. 지원하지 않은 기능이 많음\n3. 1.의 이유로 관리가 매우힘듦\n4. discord.py의 불투명한 지원계획\n\n기존 Chatdroid코드는 github에 오픈소스로 풀 예정입니다.\n코루틴, 비동기를 입문하시는 분들에게는 아주 약간 도움이 될겁니다.\n\n\nThank you!", color=0xff0000)
            await message.channel.send(embed=embed)
            
        else:
            embed = discord.Embed(title="**⚠️unauthenticated user error**", description = "```Invalid user```\nID값이 일치하지 않아 사용이 차단되었습니다.", color=0xff0000)
            await message.channel.send(embed=embed)
               
 
    
    if message.content.startswith("!cls"):
        if message.author.id == 833697465319948361:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))
            embed = discord.Embed(title="**Censored!**", description="```메시지가 비공개유저에 의해 삭제되었습니다.\n이 메시지는 3초후 자동삭제 됩니다```" , color=0x000000)
            embed.set_footer(text="DevAccessAdminPrtcl", icon_url = message.author.avatar_url)
            await message.channel.send(embed=embed)
            await asyncio.sleep(3)
            await message.channel.purge(limit=1)
            
         
        else:
           embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```\nID값이 일치하지 않아 사용이 차단되었습니다.", color=0xff0000)
           await message.channel.send(embed=embed)
       
    
    if message.content.startswith('!devnoti'):
        
       if message.author.id == 833697465319948361:
        
            
           await message.channel.send('```dev id verified```')
           await message.channel.send(message.author)
           await asyncio.sleep(0.2)
           await message.channel.purge(limit=2)
            
           embed = discord.Embed(title=f"{titi}", description=f"{scrip}", color=0xff0000)
           await message.channel.send(embed=embed)
        
        
       else:
          embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```\nID값이 일치하지 않아 사용이 차단되었습니다.", color=0xff0000)
          await message.channel.send(embed=embed)
    
    
    if message.content.startswith("!pntprtcl"):
        if message.author.id == 833697465319948361:
            ch = 0
            for g in client.guilds:
                ch += len(g.channels)
        
            await message.channel.purge(limit=1)
            ver = "**2.0.0(31ver)**"
            fix = "**<2022/10/01 업데이트 내역>**\n\n- 봇 레이턴시 최적화\n- 스택 트레이싱 업데이트\n\n\n**<1차 지원종료 공지>**\n\n!논술, !수시, !제목, !내용, !공지 명령어는 2022-10-01부로 지원종료 되었습니다.**"   
            embed = discord.Embed(title=f"{ver}", description = f"{fix}", color = 0xff0000)
            embed.set_footer(text= "감지된 채널 수: {channel.num}")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/984777197506162748/985181219329294376/Screenshot_20220610-224533_Samsung_Notes-removebg-preview.jpg")
            await message.channel.send(embed=embed)
        
        else:
            embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```\nID값이 일치하지 않아 사용이 차단되었습니다.", color=0xff000)
            await message.channel.send(embed=embed)
        
    if message.content.startswith("!dvcl"):
        if message.author.id == 833697465319948361:
            if message.author.dm_channel:
                await message.channel.purge(limit=1)
                dvti = "DevAccessAdminPrtcl dvcl lst"
                clst = "!onprtcl\n!dndprtcl\n!offprtcl\n!upprtcl\n!pnt\n!cls\n!devnoti"        
                embed = discord.Embed(title=f"{dvti}", description = f"{clst}", color=0xff0000)
                await message.author.dm_channel.send(embed=embed)
                await message.channel.send("dev verified")
        
            
            if message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await message.channel.purge(limit=1)
                dvti = "```DevAccessAdminPrtcl dvcl lst```"
                clst = "!onprtcl\n!dndprtcl\n!offprtcl\n!upprtcl\n!pnt\n!cls\n!devnoti"        
                embed = discord.Embed(title=f"{dvti}", description = f"{clst}", color=0xff0000)
                await message.author.dm_channel.send(embed=embed)
                await message.channel.send("dev verified")
        
            
            
        
        else:
            embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```\n열람이 불가능한 명령어입니다.", color=0xff000)
            await message.channel.send(embed=embed)
            
        
 
        


access_token = os.environ["BOT_TOKEN"]

client.run(access_token)








