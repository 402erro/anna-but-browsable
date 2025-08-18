import requests
from bs4 import BeautifulSoup
import time
import json
response = requests.get("https://annas-archive.org/dyn/torrents.json")
md5 = input("Please enter an md5: ")
torrents = response.json()

with open("byterecords.jsonl.seekable",mode="r",encoding="utf-8") as read:
    for line in read:
        byte_data = json.loads(line)  
        if md5 == byte_data['metadata']['md5']:
            torrent_name = byte_data['metadata']['torrent_filename']
            byte_start = byte_data['metadata']['byte_start']
            for i in torrents:
                if i['display_name']



