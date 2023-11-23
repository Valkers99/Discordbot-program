import json
from random import randint
import discord
from decouple import config
import requests
from bs4 import BeautifulSoup
import io
from PIL import Image
import aiohttp

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.name == "gmcgwn" and not(message.content.startswith('t!')):
        tenpercenter = randint(0,9)
        if tenpercenter == 0:
            page = randint(0,5)
            post = randint(0,24)
            response = requests.get(f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=foot_focus&limit=25&pid={page}")
            unsouped_response = BeautifulSoup(response.content, features='xml')
            image_url = str(unsouped_response.find_all('file_url')[post])[10:-11]
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    if resp.status != 200:
                        return await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(f"Hey {message.author.name}  here is your image!")
                    await message.channel.send(file=discord.File(data, 'cool_image.png'))
    
    if message.author.name == "badgersclan" and not(message.content.startswith('t!')):
        tenpercenter = randint(0,9)
        if tenpercenter == 0:
            fiftyfifty = randint(0,1)
            await message.channel.send(f"Hey {message.author.name}  here is your video!")
            if fiftyfifty == 0:
                
                await message.channel.send("https://cdn.discordapp.com/attachments/921075396416536578/1177350723214786677/Hes_going_to_sacrifice_himself_.mp4")
            else:
                await message.channel.send("https://cdn.discordapp.com/attachments/921075396416536578/1177350722505936916/y2mate.is_-_Not_me_not_Hermione_..._YOU-sinDVeBVjgw-720p-1700771385.mp4")
    
    if message.author.name == "totallynotbob" and not(message.content.startswith('t!')):
        tenpercenter = randint(0,9)
        if tenpercenter == 0:
            page = randint(0,5)
            post = randint(0,24)
            response = requests.get(f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=suit 1girl solo helltaker&limit=25&pid={page}")
            unsouped_response = BeautifulSoup(response.content, features='xml')
            image_url = str(unsouped_response.find_all('file_url')[post])[10:-11]
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    if resp.status != 200:
                        return await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(f"Hey {message.author.name}  here is your image!")
                    await message.channel.send(file=discord.File(data, 'cool_image.png'))


    if message.author.name == "valkers" and not(message.content.startswith('t!')):
        tenpercenter = randint(0,9)
        if tenpercenter == 0:
            page = randint(0,5)
            post = randint(0,24)
            response = requests.get(f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags=futa solo&limit=25&pid={page}")
            unsouped_response = BeautifulSoup(response.content, features='xml')
            image_url = str(unsouped_response.find_all('file_url')[post])[10:-11]
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as resp:
                    if resp.status != 200:
                        return await message.channel.send('Could not download file...')
                    data = io.BytesIO(await resp.read())
                    await message.channel.send(f"Hey {message.author.name}  here is your image!")
                    await message.channel.send(file=discord.File(data, 'SPOILER_cool_image.png'))

    if message.content.startswith('t!'):
        command = message.content[3:]
        # HELLO COMMAND
        if command[:5] == "hello":
            await message.channel.send('Hello!')
    
        # FINDCARD MTG COMMAND
        elif command[:11] == "findcardmtg":
            response = requests.get(f"https://api.magicthegathering.io/v1/cards?name={command[12:]}")
            if response.status_code == 400:
                await message.channel.send("That card doesn't exist, sorry!")
            else:
                print(f"findcard command by {message.author}")
                await message.channel.send('Here is your card!')
                image_url = json.loads(response.content)['cards'][0]['imageUrl']
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as resp:
                        if resp.status != 200:
                            return await message.channel.send('Could not download file...')
                        data = io.BytesIO(await resp.read())
                        await message.channel.send(file=discord.File(data, 'cool_image.png'))
                await message.channel.send(f"Name: {json.loads(response.content)['cards'][0]['name']} \
                                        \nCost: {json.loads(response.content)['cards'][0]['manaCost']} \
                                        \nDescription: ```{json.loads(response.content)['cards'][0]['text']}``` \
                                        \nType: {json.loads(response.content)['cards'][0]['type']}")

        # FINDCARD YUGIOH COMMAND
        elif command[:14] == "findcardyugioh":
            response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={command[15:]}")
            if response.status_code == 400:
                await message.channel.send("That card doesn't exist, sorry!")
            else:
                print(f"findcard command by {message.author}")
                await message.channel.send('Here is your card!')
                await message.channel.send(json.loads(response.content)['data'][0]['card_images'][0]['image_url'])
                # Link cards
                if json.loads(response.content)['data'][0]['type'] == "Link Monster":
                    await message.channel.send(f"Name: {json.loads(response.content)['data'][0]['name']} \
                                           \nType: {json.loads(response.content)['data'][0]['type']} \
                                           \nDescription: ```{json.loads(response.content)['data'][0]['desc']}``` \
                                           \nAttack: {json.loads(response.content)['data'][0]['atk']} \
                                           \nLINK: {json.loads(response.content)['data'][0]['linkval']} \
                                           \nPrices: \n  Cardmarket: ${json.loads(response.content)['data'][0]['card_prices'][0]['cardmarket_price']} \
                                           \n  Amazon: ${json.loads(response.content)['data'][0]['card_prices'][0]['amazon_price']} \
                                           \n  TCGplayer: ${json.loads(response.content)['data'][0]['card_prices'][0]['tcgplayer_price']} \
                                           \n  Ebay: ${json.loads(response.content)['data'][0]['card_prices'][0]['ebay_price']} \
                                           \n  Coolstuffinc: ${json.loads(response.content)['data'][0]['card_prices'][0]['coolstuffinc_price']}")
                # Spell/Trap cards    
                elif json.loads(response.content)['data'][0]['type'] == "Spell Card" or json.loads(response.content)['data'][0]['type'] == "Trap Card":
                    await message.channel.send(f"Name: {json.loads(response.content)['data'][0]['name']} \
                                           \nType: {json.loads(response.content)['data'][0]['type']} \
                                           \nDescription: ```{json.loads(response.content)['data'][0]['desc']}``` \
                                           \nPrices: \n  Cardmarket: ${json.loads(response.content)['data'][0]['card_prices'][0]['cardmarket_price']} \
                                           \n  Amazon: ${json.loads(response.content)['data'][0]['card_prices'][0]['amazon_price']} \
                                           \n  TCGplayer: ${json.loads(response.content)['data'][0]['card_prices'][0]['tcgplayer_price']} \
                                           \n  Ebay: ${json.loads(response.content)['data'][0]['card_prices'][0]['ebay_price']} \
                                           \n  Coolstuffinc: ${json.loads(response.content)['data'][0]['card_prices'][0]['coolstuffinc_price']}")
                # Other monster cards
                else:
                    await message.channel.send(f"Name: {json.loads(response.content)['data'][0]['name']} \
                                            \nType: {json.loads(response.content)['data'][0]['type']} \
                                            \nDescription: ```{json.loads(response.content)['data'][0]['desc']}``` \
                                            \nAttack: {json.loads(response.content)['data'][0]['atk']} \
                                            \nDefense: {json.loads(response.content)['data'][0]['def']} \
                                            \nPrices: \n  Cardmarket: ${json.loads(response.content)['data'][0]['card_prices'][0]['cardmarket_price']} \
                                            \n  Amazon: ${json.loads(response.content)['data'][0]['card_prices'][0]['amazon_price']} \
                                            \n  TCGplayer: ${json.loads(response.content)['data'][0]['card_prices'][0]['tcgplayer_price']} \
                                            \n  Ebay: ${json.loads(response.content)['data'][0]['card_prices'][0]['ebay_price']} \
                                            \n  Coolstuffinc: ${json.loads(response.content)['data'][0]['card_prices'][0]['coolstuffinc_price']}")
            
        else:
            await message.channel.send("Sorry don't know that command!")

    

client.run(config('BOT_TOKEN')) # type: ignore