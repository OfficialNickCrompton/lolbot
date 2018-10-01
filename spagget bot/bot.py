#spagget bot by spagget meatballs

import discord 
from discord.ext import commands
import asyncio
import random
from itertools import cycle


client = commands.Bot(command_prefix = '*')
status = ['rock paper scissors | use *help for help', 'the shrek soundtrack. ALWAYS | use *help for help', 'use *help for help']

@client.event
async def on_ready():
    print ("ye boi")
   
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(7)



@client.command(pass_context=True)
async def ok_hand(ctx):
    await client.say(":ok_hand:")

@client.command(pass_context=True)
async def k(ctx):
    await client.say(":regional_indicator_k: :regional_indicator_k: :regional_indicator_k: :regional_indicator_k: :regional_indicator_k: :regional_indicator_k: :regional_indicator_k: :regional_indicator_k: :regional_indicator_k: ")


@client.command(pass_context=True)
async def meme(ctx):
    await client.say(random.choice(["https://cdn.discordapp.com/attachments/462275631120384000/484804756985085964/pt711.jpg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484811181945651222/5a672463af8f8.jpeg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484812551570456608/1wjamt.jpg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484813667276161024/minecraft-fags_o_655701.jpg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484814009615384576/white-people-have-no-cultu-realistic-minecraft-steve-gets-a-fidget-20026120.png",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484814210346254336/22-Hilarious-Text-Memes-013-550x747.jpg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484814417889067009/1-.png",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484814918101762048/eMr0J.jpg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484815063987912714/1rx5t4.jpg",
                                "https://cdn.discordapp.com/attachments/484808860641525774/484815253306212382/maxresdefault_1.jpg",
                                "https://cdn.discordapp.com/attachments/458723226638483468/484821129371058218/MEME.png",
                                "https://cdn.discordapp.com/attachments/458723226638483468/484825790454693898/MEME_2.png"]))



@client.command(pass_context=True)
async def roast(ctx, user: discord.Member):
    await client.say(random.choice(["Scientists can't determine whether the earth is round or flat because all they can see in the satellites is your fat ass.",
                                 "You're so bad at driving, you got arrested for drunk driving even though you weren't drunk!",
                                 "I wanted to kick you in the teeth, but I also didn't want to improve your looks."]))

client.loop.create_task(change_status())
client.login(process.env."NDgxODA4OTU5NDUyNDc5NTQ5.Dl7_1g.gNqKfZY7rksAXCwBXtWzTvdlzGY")