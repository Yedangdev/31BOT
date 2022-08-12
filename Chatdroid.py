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




client = discord.Client()
@client.event
async def on_ready():
    print('봇 온라인!')
    print('업데이트에 성공하였습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')
    
    await client.change_presence(status=discord.Status.online) #온라인
    
    while not client.is_closed():
        await client.change_presence(activity=discord.Game(name="!도움말"))
        await asyncio.sleep(5)
        ch = 0
        for g in client.guilds:
            ch += len(g.channels)
        await client.change_presence(activity=discord.Game(name=f"{ch}개의 채널과 함께"))
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
        univdict = {"경기대(서울)" : "{학교장추천}\n학생부100\n(교과90+출결10)\n{교과성적우수자}\n학생부100\n(교과90+출결11)\n<최저>\n국,수,영,탐/직(1) 중 2개 합 7,한 6", "경희대" : "{지역균형}\n학생부70\n(교과56+출결7+봉사7)+서류30\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 5,한 5\n한의예(인문):국,수,영,탐(1) 중 3개 합 4,한 5\n자연:국,수(미/기),영,과(1) 중 2개 합 5,한 5\n의예/한의예(자연)/치의예/약학:국,수(미/기),영,과(1) 중 3개 합 4,한 5", "고려대" : "{학교추천}\n학생부80+서류20\n<최저>\n인문: 국,수,영,탐 중 3개 합 6, 한 3\n자연: 국,수(미/기),영,과 중 3개 합 7, 한 4\n의대: 국,수(미/기),영,과 중 4개 합 5, 한 4\n(과탐 동일과목 1, 2 미인정)","광운대":"{지역균형}\n학생부100\n<최저>\n없음","국민대":"{교과성적우수자}\n학생부100\n<최저>\n인문 : 국,수,영,탐(1) 중 2개 합 5\n자연 : 국,수,영,과(1) 중 2개 합 6","덕성여대":"{고교추천}\n학생부100\n<최저>\n없음\n<전형방법>\n{학생부100%}\n학생부100\n<최저>\n국,수,영,탐(1) 중 2개 합 7(영 포함시 합 6)\n약학 : 국,수(미/기),과 중 2개 합 4","동국대":"{학교장추천인재}\n학생부70+서류30\n<최저>\n없음","명지대(서울)":"{학교장추천}\n학생부100\n<최저>\n없음\n<전형방법>\n{교과면접}\n1단계(5배수):학생부100\n2단계:학생부 70+면접 30\n<최저>\n없음","상명대":"{고교추천}\n학생부100\n<최저>\n국,수,영,탐(1) 중 2개 합 7\n<전형방법>\n{고교추천}\n1단계(3배수):학생부100\n2단계:학생부80+면접10+체력검정10\n<최저>\n없음","서강대":"{고교장추천}\n학생부100\n(교과90+출결5+봉사5)\n<최저>\n국,수,영,탐/직(1) 중 3개 합 6,한 4","서경대":"{교과성적우수자}\n학생부100\n<최저>\n국,수,영,탐/직(1) 중 2개 합 6\n<전형방법>\n{일반학생}\n학생부60+논술40\n<최저>\n없음","서울과기대":"{고교추천}\n학생부100\n<최저>\n인문: 국,수,영,탐/직(1) 중 2개 합 7\n자연: 국,수(미/기),영,과(1) 중 2개 합 7","서울교대":"{학교장추천}\n1단계(2배수):학생부100\n2단계:1단계80+면접20\n<최저>\n국,수,영,탐 4개 합 9, 한 4(수(미/기), 과탑 선택 시 합 11)","서울시립대":"{지역균형선발}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 3개 합 7\n자연:국,수(미/기),영,과(1) 중 3개 합 7","성균관대":"{학교장추천}\n학생부100\n<최저>\n인문, 의상학 : 국,수,영,탐(1) 중 3개 합 6\n글로벌(리더,경제,경영) : 국,수,영,탐(1) 중 3개 합 5\n자연 : 국,수(미/기),영,과(1),과(2) 5개 중 3개 합 6\n소프트웨어 : 국,수(미/기),영,과(1),과(2), 5개 중 3개 합 5\n*인문 제2외/한문 탐구 1개로 대체 가능","세종대":"{지역균형}\n학생부100\n<최저>\n인문 : 국,수,영,탐(1) 중 2개 합 6\n자연 : 국,수(미/기),영,과(1) 중 2개 합 7","숭실대":"{학생부우수자}\n학생부100\n<최저>\n인문 : 국,수,영,탐(1) 중 2개 합 4\n자연 : 국,수(미/기),영,과(1) 중 2개 합 5\n자유전공 : 국,수(미/기),영,탐(1) 중 2개 합 5","연세대":"{추천형}\n1단계(5배수):학생부100\n2단계:1단계60+면접40\n<최저>\n없음","중앙대":"{지역균형선발}\n학생부100\n(교과90+출결10)\n<최저>\n인문 : 국,수,영,탐(1) 중 3개 합 7, 한 4\n자연 : 국,수(미/기),영,과(1) 중 3개 합 7, 한 4\n약학 : 국,수(미/기),영, 과(1) 4개 합 5, 한 4\n(과탐 동일과목 1,2 미인정)","건국대":"{KU지역균형}\n학생부100\n(교과90+출결10)\n<최저>\n없음","한국외대":"{학교장추천}\n학생부100\n<최저>\n국,수,영,탐(1) 중 2개 합 4,한 4","한성대":"{교과1}\n학생부100\n<최저>\n국,수,영,탐(1) 중 2개 합 7(야간: 합8)\n<전형방법>\n{교과2}\n학생부100\n<최저>\n없음","한양대":"{지역균형발전}\n학생부100\n<최저>\n없음","홍익대":"{학교장추천자}\n학생부100\n<최저>\n인문 : 국,수,영,탐(1) 중 3개 합 7, 한 4\n자연 : 국,수(미/기),영,과(1) 중 3개 합 8, 한 4","인하대":"{지역균형}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 5\n자연:국,수(미/기),영,과(1) 중 2개 합 5\n의예과:국,수(미/기),영,과 중 3개 각 1","가천대":"{지역균형}\n[인문,자연]\n1단계(6배수):학생부100\n2단계: 1단계50+면접50\n<최저>\n없음\n<전형방법>\n[의예,약학,한의예]\n1단계(10배수):학생부100\n2단계:1단계50+면접50\n<최저>\n의예:국,수(미/기),영,과 중 3개 각 1\n(탐구 소수점 절사)\n한의예:국,수(미/기),영,과 중 2개 각 1\n(과탐 적용시 2과목 모두 1등급)\n약학:국,수(미/기),영,과 중 3개 각 1\n<전형방법>\n{학생부우수자}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 6\n자연:국,수,영,탐(1) 중 2개 합 6\n(수(미/기) 선택 시 1등급 상향)","경기대":"{학교장추천}\n학생부100(교과90+출결10)\n<최저>\n인문:국,수,영,탐/직(1) 중 2개 합 7,한 6\n자연:국,수,영,과(1) 중 2개 합 7,한 6\n<전형방법>\n{교과성적우수자}\n학생부100(교과90+출결10)\n<최저>\n인문:국,수,영,탐/직(1) 중 2개 합 7,한 6\n자연:국,수,영,과(1) 중 2개 합 7,한 6","단국대":"{지역균형선발}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 6\n자연:국,수(미/기),영,과(1) 중 2개 합 6","수원대":"{지역균형선발}\n학생부60+면접40\n<최저>\n국,수,영,탐/직(1) 중 1개 4\n<전형방법>\n{교과우수}\n학생부100\n<최저>\n국,수,영,탐/직(1) 중 2개 합 7\n간호:국,수,영,탐/직(1) 중 2개 합 6\n<전형방법>\n{면접교과}\n1단계(5배수):학생부100교과80+출결10+봉사10\n<최저>\n없음","아주대":"{고교추천}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 5\n자연:국,수,영,과(1) 중 2개 합 5","한양대(에리카)":"{지역균형선발}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 6\n자연:국,수(미/기),영,과(1) 중 2개 합 6\n약학:국,수(미/기),영,과(1) 중 3개 합 5","경북대":"{교과우수자}\n학생부100\n<최저>\n인문,자연:국,수,영,탐(1) 중 2개 합 5~6\n(계열별 필수 지정영역 있음)\n의예,치의예:국,수(미/기),영,과 중 3개 합 3\n(과탐 필수,소수점 절사)\n수의예,약학:국,수(미/기),영,과 중 3개 합 5\n(과탐 필수,소수점 절사)","부산대":"{학생부교과}\n학생부100\n<최저>\n인문:국,수,영,탐(1) 중 2개 합 4(경영제외), 3개 합 6(경영)\n자연:국,수,영,탐(1) 중 2~3개 합 4~6\n(일부 학과 수,탐 지정 영역 있음)\n한의학:국,수(미/기),영,과(1) 중 3개 합 4(수 포함)"}  #이부분만 수정하면됨
   
    
    
        try:   #존재하는 key값이라면
            univres = univdict[founddict]  #key값에 해당하는 value값을 가져와 출력
            #hexcdu = "0x7289da"
        
        except KeyError:   #key값이 존재하지 않는다면
            univres = "등록리스트에 존재하지 않거나, 존재하지 않는 대학입니다.\n\n\n**오타를 확인해보세요**\n검색요령: ex) '경북대 검색시' ------> ```!수시 경북대```\n\n!수시와 대학이름사이에 공백이 있어야 검색이 가능합니다.\n\n\n\n\n\n\n**오류는 제보해주세요**" #key값이 없음을 알리기
            founddict = "**검색에 실패했습니다**"
            #hexcdu = "0xff0000"
        
        embed = discord.Embed(title=f"🏫{founddict}", description = f"{univres}", color = 0x7289da)
        await message.channel.send(embed=embed)
        

    
    
    if message.content.startswith("!반란"):
        await message.channel.purge(limit=1)
        nme = message.content[4:]
        
        be = randint(1,100)
        if 1 <= be < 30:
            bly = "씨발새끼야"                    
        if 30 <= be < 60:
            bly = "병신새끼야"              
        if 60 <= be < 100:
            bly = "씹련아"
        if message.author.id == 714351331464314932:
            bly = "사용할 수 없습니다."
            nme = f"{message.author.mention}는"
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
        wday = time.localtime().tm_wday
        if wday == 0:
            timetble = '프로\n기하\n미적\n논술\n심독작\n물리2\n생명2'
        elif wday == 1:
            timetble = '기하\n미적\n여지\n심국\n심독작\n생명2\n프로'
        elif wday == 2:
            timetble = '미적\n심독작\n프로\n여지\n생명2\n물리2\n논술'
        elif wday == 3:
            timetble = '미적\n스포\n심국\n진로\n심독작\n물리2\n여지'
        elif wday == 4:
            timetble = '자율3\n심국\n스포\n기하\n자봉\n동아'
        elif wday == 5:
            timetble = '오늘은 토요일입니다!'
        elif wday == 6:
            timetble = '오늘은 일요일입니다!'

        embed = discord.Embed(title="**📃오늘의 시간표!**", description=f"{timetble}\n\n\n"+"[이곳을 눌러 전체시간표 열람](<https://media.discordapp.net/attachments/1007568791116460073/1007568838180741160/IMG_2534.png>)"+"```python\n오전 9시에 시간표가 갱신됩니다```", color = 0x7289da)
        embed.set_thumbnail(url="https://discord.com/channels/983342486812516413/983342486812516416/986418832526684241")
        await message.channel.send(embed=embed)
        #await message.channel.send("https://media.discordapp.net/attachments/1007568791116460073/1007568838180741160/IMG_2534.png")
        


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
            
            #await message.channel.send('베타기능이에요')
            await message.channel.purge(limit=1)
            
            embed = discord.Embed(title=f"{titi}", description=f"{scrip}", color=0xff00)

            await message.channel.send(embed=embed)
        
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
        
        

    if message.content.startswith('!작성언어'):
        await message.channel.send('저는 파이썬으로 만들어졌어요!')
        
        
    if message.content.startswith('!급식'):
        
        await message.channel.send('```python\nneis api 로딩중...\n예상처리시간:3초```')
        await asyncio.sleep(2.5)
        await message.channel.purge(limit=2)
              
        dietdate = message.content[4:]
        
        if len(dietdate) == 0:
            dietdate = datetime.today().strftime("%Y%m%d")
        
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
        
        if dietdate == datetime.today().strftime("%Y%m%d"):
            titledate = "🍴**오늘의**"
        
        else:
            titledate = f"🍴{dietdate[:4]}/{dietdate[4:6]}/{dietdate[6:]}"
        
        
        if dietre == "**검색에 실패하였습니다**\n\n**오타를 확인해보세요!**\n검색요령ex) ```!급식 20220921``` --> 2022년09월21일의 급식정보":
            titledate = "**⚠️존재하지 않는**"
            #hexcde = "0x0xff0000"
        
        embed=discord.Embed(color= 0x7289da, title= f"{titledate} **급식표**", description= f"{dietpr}\n\n\n```python\n오전 9시에 급식표가 갱신됩니다!```", timestamp=message.created_at)
        #embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
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


    if message.content.startswith('!논술'):    #매크로로 쓴거다. 내가 직접 쓰지 않았음.
        index = message.content[4:]
        #hexcdr = "0x7289da"
        
        
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
            setence = "논술전형을 실시하는 대학이 아니거나, 존재하지 않는 대학입니다.\n\n\n**오타를 확인해보세요**\n검색요령: ex) '한양대학교 에리카 검색시' ------> **```!논술 한양대(에리카)```**\n\n!논술과 대학이름사이에 공백이 있어야 검색이 가능합니다.\n\n\n\n\n\n\n**정보가 누락되었거나, 오류는 제보해주세요**"
            index = "**검색에 실패했습니다**"
            #hexcdr= "0xff0000"
        
        embed=discord.Embed(color= 0x7289da, title= f"🏫{index}", description= f"{setence}")
        await message.channel.send(embed=embed) #출력
        
        
    if message.content.startswith('!운세'):
        
        b = message.content[4:]
        if b == ".":
            
            await message.channel.purge(limit=1)
            
            embed=discord.Embed(color=0x7289da, title= "**이스터에그!**", description= "행운이란 준비와 기회를 만났을 때 나타난다", timestamp=message.created_at)
          
            await message.channel.send(embed=embed)
            await asyncio.sleep(1)
            await message.channel.send('{}님, 1%의 확률에 당첨되셨습니다!!!'.format(message.author.mention))
         
        
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
                await message.channel.send('{}님, ANTI_CMD%의 확률로 당첨되셨습니다!!!'.format(message.author.mention))
            
            
            



    if message.content.startswith('!도움말'):
        #await message.channel.purge(limit=1)
        if message.author.dm_channel:

            #channel = await message.author.create_dm()
            noti = "\n\n\n**<Chatdroid 명령어>**\n\n**!급식** or **!급식** + 년/월/일 --> 급식정보를 제공합니다.\n\n**!논술** + 대학이름 --> 23년도 모든 논술실시대학의 논술전형정보를 제공합니다\n\n**!수시** + 대학이름 --> 34개대학의 인서울권 대학의 수시정보를 보여줍니다\n\n**!반란** + 욕하고 싶은 사람 --> 봇이 욕을 대신해줍니다!\n\n**!한일,!한영,!번역** + 번역하고자하는 내용 --> 번역을 해드립니다.\n\n**!ping** --> 봇의 레이턴시정보를 제공합니다\n\n**!전적** + 소환사이름 --> opgg사이트 바로가기를 보여줍니다.\n\n**!롤토** + 소환사이름 --> lolchess.gg사이트 바로가기를 보여줍니다.\n\n**!마법의 소라고둥님** or **!s** + 하고싶은질문 --> 마법의 소라고둥이 질문에 대해 답해줍니다.\n소라고둥의 답은 깊은 뜻을 가지고 있습니다.\n\n**!운세** --> 간단하게 오늘의 운을 시험해보세요!\n\n**!강조** + 문자내용 --> 메세지를 강조해드립니다, 설문조사홍보나 홍보활동을 강조해보세요!\n\n**!청소** + 숫자 --> 입력한 숫자만큼 메시지를 삭제합니다.(관리자만) 효과적으로 방을 관리하세요.\n\n**!d6** --> 주사위를 굴려요\n\n**!시간표** --> 오늘 시간표를 알려드립니다(오전9시에 업데이트됩니다.)\n\n임베드로 공지사항을 강조해 효과적인 공지사항을 제작하세요(관리자 전용)!!\n\n이용방법\n\n**!제목** --> 임베드의 제목을 정해요\n\n**!내용** --> 임베드의 내용을 정해요\n\n**!공지** --> 임베드를 출력해요\n\n\n\n개인서버에서 초대해 쓰고싶으면 지빈#1638으로 갠디코 주세요\n\n\n\n\n```Chatdroid.ver.2.0.0```"
            
            embed=discord.Embed(color=0x7289da, title= "📌도움말", description= f"{noti}", timestamp=message.created_at)
            await message.author.dm_channel.send(embed=embed)
            await message.channel.send("```python\nCheck your DM!```")
            
        if message.author.dm_channel is None:
            channel = await message.author.create_dm()
            noti = "\n\n\n**<Chatdroid 명령어>**\n\n**!급식** or **!급식** + 년/월/일 --> 급식정보를 제공합니다.\n\n**!논술** + 대학이름 --> 23년도 모든 논술실시대학의 논술전형정보를 제공합니다\n\n**!수시** + 대학이름 --> 34개대학의 인서울권 대학의 수시정보를 보여줍니다\n\n**!반란** + 욕하고 싶은 사람 --> 봇이 욕을 대신해줍니다!\n\n**!한일,!한영,!번역** + 번역하고자하는 내용 --> 번역을 해드립니다.\n\n**!ping** --> 봇의 레이턴시정보를 제공합니다\n\n**!전적** + 소환사이름 --> opgg사이트 바로가기를 보여줍니다.\n\n**!롤토** + 소환사이름 --> lolchess.gg사이트 바로가기를 보여줍니다.\n\n**!마법의 소라고둥님** or **!s** + 하고싶은질문 --> 마법의 소라고둥이 질문에 대해 답해줍니다.\n소라고둥의 답은 깊은 뜻을 가지고 있습니다.\n\n**!운세** --> 간단하게 오늘의 운을 시험해보세요!\n\n**!강조** + 문자내용 --> 메세지를 강조해드립니다, 설문조사홍보나 홍보활동을 강조해보세요!\n\n**!청소** + 숫자 --> 입력한 숫자만큼 메시지를 삭제합니다.(관리자만) 효과적으로 방을 관리하세요.\n\n**!d6** --> 주사위를 굴려요\n\n**!시간표** --> 오늘 시간표를 알려드립니다(오전9시에 업데이트됩니다.)\n\n임베드로 공지사항을 강조해 효과적인 공지사항을 제작하세요(관리자 전용)!!\n\n이용방법\n\n**!제목** --> 임베드의 제목을 정해요\n\n**!내용** --> 임베드의 내용을 정해요\n\n**!공지** --> 임베드를 출력해요\n\n\n\n개인서버에서 초대해 쓰고싶으면 지빈#1638으로 갠디코 주세요\n\n\n\n\n```Chatdroid.ver.2.0.0```"
            
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
        
    if message.content.startswith("!dndprtcl"):
        if message.author.id == 833697465319948361:
        
            await message.channel.send("dnd set")
            await client.change_presence(status=discord.Status.dnd)
            await client.change_presence(activity=discord.Game(name="봇 점검"))
        else:
            embed = discord.Embed(title="**unauthenticated user error**", description = "```Invalid user```", color=0xff0000)
            await message.channel.send(embed=embed)
        
        
    if message.content.startswith("!upprtcl"):
        if message.author.id == 833697465319948361:
        
            #await message.channel_presence(status=discord.Status.idle)
            await client.change_presence(activity=discord.Game(name="봇 업데이트"))
            await message.channel.send("update mode")
        else:
            embed = discord.Embed(title="**⚠️unauthenticated user error**", description = "```Invalid user```", color=0xff0000)
            await message.channel.send(embed=embed)
        
    if message.content.startswith("!killprtcl"):        
        #await message.channel.send("```서비스 종료절차 실행```")
        #await message.channel.send("타이머 셋팅")
        #await message.channel.send("```서비스 종료 5분전```")
        #await asyncio.sleep(300)
        #await message.channel.send("**서비스가 종료되었습니다**")
        await client.change_presence(status=discord.Status.offline)
        #await asyncio.sleep(1000000)
           
 
    
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
           embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```", color=0xff0000)
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
          embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```", color=0xff0000)
          await message.channel.send(embed=embed)
    
    
    if message.content.startswith("!pntprtcl"):
        if message.author.id == 833697465319948361:
            ch = 0
            for g in client.guilds:
                ch += len(g.channels)
        
            await message.channel.purge(limit=1)
            ver = "**2.0.0(31ver)**"
            fix = "**<업데이트 내역>**\n\n**2학기 시간표로 업데이트 되었습니다.**\n\n**일부 기능들의 임베드 UI개선\n및 시인성 향상**\n\n\n```python\n이 업데이트는 일부 서버에만 지원됩니다.```"   
            embed = discord.Embed(title=f"{ver}", description = f"{fix}", color = 0xff0000)
            embed.set_footer(text=f"감지된 서버 수:{ch}")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/984777197506162748/985181219329294376/Screenshot_20220610-224533_Samsung_Notes-removebg-preview.jpg")
            await message.channel.send(embed=embed)
        
        else:
            embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```", color=0xff000)
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
            embed = discord.Embed(title="⚠️unauthenticated user error", description = "```Invalid user```", color=0xff000)
            await message.channel.send(embed=embed)
            
        
 
        


access_token = os.environ["BOT_TOKEN"]

client.run(access_token)








