import requests
from bs4 import BeautifulSoup
import time
import re
book_md5 = input("Please input the md5: ")
response = requests.get(f"https://annas-archive.org/md5/{book_md5}")

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a', href=True)
for i in links:
    if "member_codes?prefix=sha256:" in i["href"]:
        dirty_sha256 = i.contents[0]
        match = re.search(r"[a-f0-9]{64}", dirty_sha256)
        if match:
            hash_value = match.group()
            print(hash_value)

#a5e5b0eee9b748e2b523761d8944e411
#py-0.5 truncate max-w-[35px]
#<span class="py-0.5 bg-[#aaa] mr-1 px-1 truncate max-w-[50px] flex-shrink-0">SHA-256</span>, <span class="py-0.5 truncate max-w-[35px]">d2763ceacee618362fb7d2a55a67f31ea5f41da657ef23e88de4dce73fa57317</span>,
#<a class="rounded-sm flex mb-1 mr-1 pr-1 border border-[#aaa] opacity-60 hover:opacity-80 aria-selected:opacity-100 custom-a js-md5-codes-tabs-tab max-w-[calc(50%-8px)]" href="#" aria-selected="false" id="md5-codes-tab-18" aria-controls="md5-codes-panel-18" tabindex="-1" role="tab" aria-expanded="false"><span class="py-0.5 bg-[#aaa] mr-1 px-1 truncate max-w-[50px] flex-shrink-0">SHA-256</span><span class="py-0.5 truncate max-w-[35px]">d2763ceacee618362fb7d2a55a67f31ea5f41da657ef23e88de4dce73fa57317</span></a>

# <div id="md5-codes-panel-24" role="tabpanel" aria-labelledby="md5-codes-tab-24" hidden class="text-sm mt-2">
           # <div><strong>SHA-256:</strong>
#4e2f11e34dca294affdb2df7bd445e6af7595252a03c1c660b8a06812d3773df <button class="inline-block font-sans font-normal text-xs button bg-gray-500 hover:bg-gray-600 px-1 py-0.5 rounded-md text-white ml-1 align-[2px]" onclick="if (navigator.clipboard) { navigator.clipboard.writeText('4e2f11e34dca294affdb2df7bd445e6af7595252a03c1c660b8a06812d3773df').then(() => { this.setAttribute('aria-selected', 'true'); }); }" aria-selected="false"><span class="icon-[solar--clipboard-bold] [[aria-selected=true]_&]:icon-[solar--clipboard-check-bold] align-[-5px] text-lg"></span> <span class="[[aria-selected=true]_&]:hidden">copy</span><span class="[[aria-selected=false]_&]:hidden">copied!</span></button></div>
#<div class="">Website: <a href="https://en.wikipedia.org/wiki/SHA-2" rel="noopener noreferrer nofollow">https://en.wikipedia.org/wiki/SHA-2</a></div>            <div>AA: <a href='/search?q="sha256:4e2f11e34dca294affdb2df7bd445e6af7595252a03c1c660b8a06812d3773df"'>Search Anna’s Archive for “sha256:4e2f11e34dca294affdb2df7bd445e6af7595252a03c1c660b8a06812d3773df”</a></div>
#            <div>Codes Explorer: <a href="/member_codes?prefix=sha256:4e2f11e34dca294affdb2df7bd445e6af7595252a03c1c660b8a06812d3773df">View in Codes Explorer “sha256:4e2f11e34dca294affdb2df7bd445e6af7595252a03c1c660b8a06812d3773df”</a></div>
#          </div>
