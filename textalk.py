import discord

# TOKEN = 'NjcwNTI4MTAwOTMyNjQ4OTgw.XiwRGg.2yrGp4klU-1oDBpuHjl6foG4j2Q'

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
print(TOKEN)
client.run('NjcwNTI4MTAwOTMyNjQ4OTgw.XiwUig.kvUUKRFQtQ_uSo8Z1JVPN5-tHaA')