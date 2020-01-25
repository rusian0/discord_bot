# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjcwNTI4MTAwOTMyNjQ4OTgw.Xivspg.XIL9FCW30sc9KgSbPi7TUe3Jy90'

# 接続に必要なオブジェクトを生成
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