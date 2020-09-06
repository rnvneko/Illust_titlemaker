# coding: utf-8

# インストールした discord.py を読み込む
import discord
import illust_titlemaker1
import practice_reminder
import os
from discord.ext import tasks
from datetime import datetime, timedelta, timezone


# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 接続時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("ログインしました")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視
    if message.author.bot:
        return
    # 「/お題」と発言したらランダムにアニメタイトルとポーズを返す処理
    if message.content == "/お題":
        await message.channel.send(illust_titlemaker1.randomtitle())
    if message.content == "/唯ちゃん":
        await message.channel.send("佐倉さんはけっこう苦手。。。")
    if message.content == "/あんこーる":
        await message.channel.send(practice_reminder.random_member())


JST = timezone(timedelta(hours=+9), 'JST')

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now(JST)
    time = now.strftime('%H:%M')
    day = now.weekday()
    if time == '19:oo' and (day == 2 or day == 4):
        channel = client.get_channel(716206634979950613)
        await channel.send(practice_reminder.random_member())

#ループ処理実行
loop.start()

client.run(TOKEN)
