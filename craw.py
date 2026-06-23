from operator import truediv

import yt_dlp
import requests
from bs4 import BeautifulSoup
import csv

from yt_dlp import YoutubeDL
import os


# url = "https://music.youtube.com/search?q=刘德华歌曲大全"
#
# ydl_opts = {
#     "extract_flat": True,
#     "quiet": True
# }
#
# with YoutubeDL(ydl_opts) as ydl:
#     info = ydl.extract_info(url, download=False)
#
#     for item in info.get("entries", []):
#         print(item.get("title"))

url = "https://so.tv.sohu.com/list_p1_p2_p3_p4_p5_p6_p7_p8_p9_p10_p11_p12_p13_p14.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).text

print(html[:1000])
html = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
).text

soup = BeautifulSoup(html, "html.parser")

for a in soup.find_all("a", href=True):

    href = a["href"]

    if "tv.sohu.com" in href:

        title = a.get_text(strip=True)

        if title:
            print(title, href)
rows = []

for a in soup.find_all("a", href=True):

    href = a["href"]

    if "tv.sohu.com" in href:

        title = a.get_text(strip=True)

        if title:

            rows.append([
                title,
                href
            ])

with open(
    "sohu_videos.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "title",
        "url"
    ])

    writer.writerows(rows)

print("完成")