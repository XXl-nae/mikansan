import discord
from discord.ext import commands
import json
import requests
import random

settings = {
    'token': 'Nzc3MTE2MzIxMjI5NTcwMTA4.X6-v-Q.rhwBEMvfDtwdBcvYqbYT6z0MOe0',
    'bot': 'Mikan',
    'id': 777116321229570108,
    'prefix': '!'
}

bot = commands.Bot(command_prefix = settings['prefix'])

# await member.create_dm()
# await member.dm_channel.send()     мессадж в лс, не забыть
# cd c:\users\servi\desktop\тест

#проверки, обязательные для каждого бота
#оаоаоаоаоаоаоа
'''@bot.event
async def on_message(message):
    if message.author == bot.user:
        return'''

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send('Неизвестная команда. Проверь правильность написания или напиши "!help" для помощи')
    elif isinstance(error, commands.errors.CheckFailure):
        await ctx.send('Тебе низя эту команду')

@bot.command() 
async def hello(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Hello, {author.mention}!') 

@bot.event
async def on_member_join(ctx): #когда пользователь приходит на сервер, Микан приветствует.
    await ctx.send(f'Хей, хей, {ctx.event.author}! Добро пожаловать в Суши Сквад! Читай правила и веселись!')

@bot.group() #делаем групповуху команд
async def randpict(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Я не узнала, какую картинку тебе скинуть... Напиши "!help randpict", если не знаешь, что писать.')

@randpict.command() #редачим вторую часть команды ranpict
async def dog(ctx): #проверка того, что написали
    response = requests.get('https://some-random-api.ml/img/dog') #просим то, что находится в сайте
    json_data = json.loads(response.text) #извлекаем json
    embed = discord.Embed(color = 0xa34f00, title = 'Случайная собачка') #создаём embed, цвет коричневый
    embed.set_image(url = json_data['link']) #делаем наш json как картинку в embed-е
    await ctx.send(embed = embed) #отправляем embed
@randpict.command() #повторяем для всех животных
async def cat(ctx): 
    response = requests.get('https://some-random-api.ml/img/cat') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0x8000ff, title = 'Случайная котя :3') #цвет - фиолетовый
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
@randpict.command() 
async def red_panda(ctx): 
    response = requests.get('https://some-random-api.ml/img/red_panda') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xff0000, title = 'Красная панда?..') #цвет - красный
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
@randpict.command()
async def panda(ctx): 
    response = requests.get('https://some-random-api.ml/img/panda') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xffffff, title = 'Случайная панда')  #цвет - белый
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
@randpict.command() 
async def birb(ctx): 
    response = requests.get('https://some-random-api.ml/img/birb') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xffee00, title = 'Случайная птица', folder = 'Ни один RHM Птица не пострадал') #цвет - жёлтый
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
@randpict.command() 
async def fox(ctx): 
    response = requests.get('https://some-random-api.ml/img/fox') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0xff9900, title = 'Случайная лисичка') #цвет - оранжевый
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
@randpict.command() 
async def koala(ctx): 
    response = requests.get('https://some-random-api.ml/img/koala') 
    json_data = json.loads(response.text) 
    embed = discord.Embed(color = 0x878787, title = 'Случайная коала') #цвет - серый
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)

bot.run('Nzc3MTE2MzIxMjI5NTcwMTA4.X6-v-Q.rhwBEMvfDtwdBcvYqbYT6z0MOe0') 