import asyncio
import discord
import random
import string
import os
import requests

@client.event
async def on_ready():
    print('on')
    stream = discord.Streaming(name="! 꾸앙#123", url='https://www.twitch.tv/twitch')
    await client.change_presence(status=discord.Status.online, activity=stream)

@client.event
async def on_message(message):
    if message.content.startswith('&명령어'):
        TEXTembed = discord.Embed(title='&명령어, &문상, &니트로, &청소, &출근, &퇴근, &임시퇴근, &휴가,     &실시간검색어, &색상, &임베드 (색상) (말), &제작자',color=0x7289da)
        await message.channel.send(embed=TEXTembed)


    if message.content.startswith('&니트로'):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NITROembed = discord.Embed(title='🎨 니트로 생성했어용!', description='https://discord.gift/' + ranNitro, color=0x7289da)
        await message.channel.send(embed=NITROembed)


    if message.content.startswith('&문상') or message.content.startswith('&문화상품권'):
        a = random.randint(2100, 3800)
        b = random.randint(1000, 9999)
        b2 = random.randint(1000, 9999)
        c = random.randint(100000,999999)
        TICKETembed = discord.Embed(title='💵 문화상품권을 생성했어용!', description=str(a) + '-' + str(b) + '-' + str(b2) + '-' + str(c), color=0x7289da)
        await message.channel.send(embed=TICKETembed)


    if message.content.startswith('&청소'):
        try:
            if message.author.guild_permissions.manage_messages:
                amount = message.content[4:]
                await message.delete()
                await message.channel.purge(limit=int(amount))
                message = await message.channel.send(
                    embed=discord.Embed(title='🧹 메시지 ' + str(amount) + '개 삭제됨', color=0x7289da))
                await asyncio.sleep(2)

            else:
                await message.channel.send('``명령어 사용권한이 없어용..ㅜㅜ``')
        except:
            pass


    if message.content.startswith('&제작자'):
        ADMINembed = discord.Embed(title=' 제작자는 ! 꾸앙#1234 에요!                                                                                  '
                                         '[꾸앙님의 서버 바로가기 https://discord.gg/ad3MyWNubG :grinning: ]',color=0x7289da)
        await message.channel.send(embed=ADMINembed)


    if message.content.startswith("&출근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 출근하였습니다.')
                await message.channel.send (embed=embed)
        except:
            pass

    if message.content.startswith("&퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 퇴근하였습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith("&임시퇴근"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 임시로 퇴근 하였습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith("&휴가"):
        try:
            if message.author.guild_permissions.manage_messages:
                embed = discord.Embed(color=0x7289da)
                embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                embed.add_field(name='관리자 출퇴근 알림', value='관리자가 휴가 가셨습니다.')
                await message.channel.send(embed=embed)
        except:
            pass

    if message.content.startswith('&실시간검색어') or message.content.startswith('&실검'):
        json = requests.get('https://www.naver.com/srchrank?frm=main').json()
        ranks = json.get("data")
        data = []
        for r in ranks:
            rank = r.get("rank")
            keyword = r.get("keyword")
            if rank > 10:
                break
            data.append(f'**{rank}**위 {keyword}')

        dat = str(data)
        dat = dat.replace("'", "")
        dat = dat.replace(", ", "\n")
        dat = dat[1:-1]
        print(dat)
        embed = discord.Embed(title='네이버 실시간 검색어 순위입니당!', description=(dat), color=0x7289da)
        await message.channel.send(embed=embed)

    if message.content.startswith("&색상"):
        await message.channel.send('임베드에 적용가능한 색상이에요! `빨강` `주황` `노랑` `초록` `파랑` `보라` `분홍` `검정` `민트` `하늘` `갈색` `회색` `남색`')

    if message.content.startswith("&임베드"):
        if message.content[5:7] == '빨강':
            selcolor = 0xFF0000
        if message.content[5:7] == '주황':
            selcolor = 0xFF8C00
        if message.content[5:7] == '노랑':
            selcolor = 0xFFDC37
        if message.content[5:7] == '초록':
            selcolor = 0x00FC08
        if message.content[5:7] == '파랑':
            selcolor = 0x006AFF
        if message.content[5:7] == '보라':
            selcolor = 0x9932CC
        if message.content[5:7] == '분홍':
            selcolor = 0xFF00FF
        if message.content[5:7] == '검정':
            selcolor = 0x000000
        if message.content[5:7] == '민트':
            selcolor = 0x00FFDD
        if message.content[5:7] == '하늘':
            selcolor = 0x3CFBFF
        if message.content[5:7] == '갈색':
            selcolor = 0x8B4F1D
        if message.content[5:7] == '회색':
            selcolor = 0x828282
        if message.content[5:7] == '남색':
            selcolor = 0x3700FF

        value = message.content[8:]
        embed = discord.Embed(color=selcolor)
        embed.add_field(name="\u200b", value=value, inline=False)
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)

        await message.channel.send(embed=embed)
        await message.delete()

   

client.run(os.environ['token'])
