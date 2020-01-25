#!/usrbin/env python3
# インストールした discord.py を読み込む
import discord

TOKEN = 'NjcwNTI4MTAwOTMyNjQ4OTgw.XiwO5w.PRoVQfbqsa6tbSi7hucDtpxaRp8'

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

client.run(TOKEN)