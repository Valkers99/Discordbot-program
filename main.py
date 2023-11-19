import json
import discord
from decouple import config
import requests

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
    
    if message.content.startswith('t!'):
        command = message.content[3:]

        # HELLO COMMAND
        if command[:5] == "hello":
            await message.channel.send('Hello!')

        # FINDCARD COMMAND
        elif command[:8] == "findcard":
            response = requests.get(f"https://db.ygoprodeck.com/api/v7/cardinfo.php?name={command[9:]}")
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

    

client.run(config('BOT_TOKEN'))