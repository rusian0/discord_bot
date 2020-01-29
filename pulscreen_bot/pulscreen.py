#!/usr/bin/python3
from pytube import extract
import discord
import json
import re
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../dev-pulscreen-firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
docRef = db.collection(u'room').document(u'rtdoeyqTA8Ze1GSbBhdP')

bot = commands.Bot(command_prefix='!')

# 設定ファイル用のconfig.jsonを読み込み辞書型にする
json_file = open('config.json', 'r')
config = json.load(json_file)

@bot.event
async def on_ready():
    print('起動完了')


# コマンドの受信イベント　現在未使用
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

    content = message.content
    print(content)

    # youtubeのURLが入力されているかを確認する
    match = re.search(r'youtube.com|youtu\.be', content)
    if not match:
        print('not video url')
        return


    # 動画URLから動画IDをを抽出する
    try:
        videoId = extract.video_id(content)
        print(videoId)
    except:
        await message.channel.send('無効な動画URLです。')
        return

    # 取得した動画IDが11文字以外だったら無効なURLとする
    if(len(videoId) != 11):
        await message.channel.send('動画の追加に失敗しました。正しいYoutubeURLが入力されているか確認してください。')
        return
        

    # firestoreへ新しい動画IDを追加
    try:
        doc = docRef.get()

        currentQueue = doc.to_dict()['video_queue']
        print(currentQueue)

        currentQueue.insert(0, videoId)
        print(currentQueue)

        docRef.update({u'video_queue':currentQueue})
    except:
        print('追加失敗')
        return

    # 追加完了した旨をテキストチャンネルへ送信
    try:
        await message.channel.send('*上記の動画をリアルタイム共有に追加しました*')
        await message.channel.send('__**共有URL：https://dev.pulscreen.com/room?id=rtdoeyqTA8Ze1GSbBhdP**__')
    except:
        print('送信失敗')


bot.run(config['bot_token'])
