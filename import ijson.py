import json

with open("byterecords.jsonl.seekable",mode="r",encoding="utf-8") as read:
    for line in read:
        byte_data = json.loads(line)
        print(byte_data)