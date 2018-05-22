import discord
import configparser
from discord.ext import commands
from plugins import rand_joke, cryptoPrice, saucenao, translater, image, helper

config = configparser.ConfigParser()
config.read('CONFIG.INI')
token = config['DEFAULT']['BOT_TOKEN']

description = '''A cool awesome bot created by isaychris'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='translate', description='Translates english to japanese')
async def translate(*args : str):
    message = ' '.join(args)
    result = translater.getTranslation(message)

    await bot.say(result)


@bot.command(name='price', description='Retrieves the price of a cryptocurrency.')
async def price(name : str ):
    coin = cryptoPrice.getPrice(name)

    if coin is None:
        await bot.say('Unable to retrieve information ... ')
        return

    await bot.say('{}: {}'.format(name, coin['price_usd']))


@bot.command(name='sauce', description='Retrieves the source of an anime picture, returning its name, episode, and time.')
async def sauce(url : str):
    if helper.validate(url):
        await bot.say('The image url you provided is invalid. Please try again.')
        return

    anime = saucenao.getSauce(url)

    if anime is None:
        await bot.say('Unable to retrieve information ... ')
        return

    await bot.say('{} - Episode {} - {}'.format(anime['source'], anime['part'], anime['est_time']))

@bot.command(name='search', description='Returns the first image result on bing search engine.')
async def search(*args : str):
    input = ' '.join(args)
    result = image.getImage(input)
    await bot.say(result)

@bot.command(name='joke', description='Returns a random joke to the user.')
async def joke():
    result = rand_joke.getJoke()
    await bot.say(result)


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

bot.run(token)