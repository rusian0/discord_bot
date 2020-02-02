#!/usr/bin/python3
import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# 設定ファイル用のconfig.jsonを読み込み辞書型にする
json_file = open('config.json', 'r')
config = json.load(json_file)

# client = discord.Client()
@bot.event
async def on_ready():
    print('起動完了')

@bot.command()
async def test(ctx, arg = ""):
    if arg == "":
        print('パラメータなし')
        return

    await ctx.send(arg)

# ユーザーがテキストチャンネルでチャットを送信したときのイベント
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    # print(message.content)
    await bot.process_commands(message)

    if (message.content == 'ジーザス'):
        await message.channel.send('sup')
        return

    # ユーザーのチャット内容が語録に入っているものだったらBOTが復唱する
    if message.content in config['analects']:
        await message.channel.send(message.content)
        return

    # 発言者がジーザスだったら注意する
    if (message.author.discriminator == '1727'):
        await message.channel.send('暴言や下品なチャットは控えましょう')
        return

    # ユーザーのチャット内容が禁止語録に入っているものだったら注意する
    if message.content in config['ban_analects']:
        await message.channel.send('暴言や下品なチャットは控えましょう')
        return
        

# ユーザーがボイスチャンネルに入った or 出たときのイベント
@bot.event
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


# トークンを使用したBOTの起動
# client.run(config['bot_token'])
bot.run(config['bot_token'])
