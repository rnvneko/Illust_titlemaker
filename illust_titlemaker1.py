# coding: utf-8
import random
import os

# タイトルリストとポーズリストを用意する
with open("title_anime.txt", encoding = "UTF-8") as f:
    anime_title = f.read()
    # print(type(anime_title))
    # print(anime_title)

anime_titles = anime_title.split()
# print(anime_titles)

with open("title_pose.txt", encoding = "UTF-8") as f:
    anime_pose = f.read()
    # print(type(anime_pose))
    # print(anime_pose)

anime_poses = anime_pose.split()
# print(anime_poses)

# ランダムでそれぞれのリストからタイトルとポーズを決定
def randomtitle():
    title = random.choice(anime_titles)
    pose = random.choice(anime_poses)
    # タイトルとポーズの組み合わせを表示
    return "作品名；" + title + " , " + "ポーズ：" + pose
