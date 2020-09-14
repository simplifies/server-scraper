import requests #type pip install requests - in cmd
import shutil #type pip install shutil  - in cmd - do it for the rest!
from discord.ext import commands 
import discord
print("[!] [!] [!] CONSIDER MAKING A SEPERATE FOLDER - THIS WILL MAKE A LOT OF FILES! [!] [!] [!]")
token = "ABC.DEF" #usertoken here - note selfbots are against tos so this is just a demonstration(obviously)
prefix = "!" 
client = commands.Bot(prefix, self_bot=True)
bot = commands.Bot(description="Discord self-bot" , command_prefix="!")


#this is made for creation of accounts - I made them all jpgs - 1) it's easier - if I wanted the correct ending I could make it read up to the . or just check the last 3 digits and see if it's a jpg,gif,ebp (webp) etc and save it correctly but
#when peeps create new accs they obviously wont have nitro so yeah, jpgs are probably the way to go 
@client.command()
async def memberstat(ctx):
    await ctx.message.delete() # so i dont get caught lol
    for member in ctx.guild.members:
        try:
            print(f"{member.name}")
            userAvatarUrl = member.avatar_url
            print(userAvatarUrl)
            response = requests.get(userAvatarUrl, stream=True)
            with open(member.name+".jpg", 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            f = open("usernames.txt", "a")
            f.write(member.name)
            f.close()
        except:
            if member != ctx.author:
                error = "lol"





client.run(token, bot=False)
