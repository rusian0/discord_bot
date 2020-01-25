import discord
import json

client = discord.Client()
@client.event
async def on_ready():
    print('起動完了')

@client.event
async def on_message(message):
    if message.author.bot:
        return
        
    print(message)
    if message.content == '!vcset':
        print(type(message.content))
        await message.channel.send('test')

@client.event
async def on_voice_state_update(member, before, after):
    role = discord.utils.get(member.guild.roles, name='Talker')
    if str(after.channel) == 'パコるフィールド☆':
        await member.add_roles(role)
        print('ロール付与')

    else:
        await member.remove_roles(role)
        print('ロール削除')

json_file = open('config.json', 'r')
config = json.load(json_file)

client.run(config['bot_token'])
