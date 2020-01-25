import discord
import json

client = discord.Client()
@client.event
async def on_ready():
    print('起動完了')

# ユーザーがテキストチャンネルでチャットを送信したときのイベント　現在未使用
@client.event
async def on_message(message):
    if message.author.bot:
        return
        
    print(message)
    if message.content == '!vcset':
        print(type(message.content))
        await message.channel.send('test')

# ユーザーがボイスチャンネルに入った or 出たときのイベント
@client.event
async def on_voice_state_update(member, before, after):
    # 特定のロールの取得
    role = discord.utils.get(member.guild.roles, name='Talker')

    # ユーザーが入ったボイスチャンネルの名前がパコるフィールドだった場合
    if str(after.channel) == 'パコるフィールド☆':
        # 特定のロールをユーザーに付与する
        await member.add_roles(role)
        
    # 指定するボイスチャンネル以外に入った or 又はボイスチャンネルから抜けた場合
    else:
        # 特定のロールを削除する（特定ロールが既に付与されているかどうかに関わらず削除を実行する)
        await member.remove_roles(role)

# 設定ファイル用のconfig.jsonを読み込み辞書型にする
json_file = open('config.json', 'r')
config = json.load(json_file)

# トークンを使用したBOTの起動
client.run(config['bot_token'])
