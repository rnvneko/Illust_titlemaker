# coding: utf-8

# インストールした discord.py を読み込む
import discord
import illust_titlemaker1
import os

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
        await message.channel.send("佐倉さんはちょっと苦手。。。")
client.run(TOKEN)