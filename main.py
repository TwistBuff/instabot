import time
import schedule
import requests
import random
import os
import shutil
from instagrapi import Client


def main():
    counter = 0
    
    limit = random.randint(1, 3)

    gaming_meme_subreddits = [
        'gamingmemes',
        'memes',
        'dankmemes',
        'memeeconomy',
        'gaming',
        'FortNiteBR',
        'pcmasterrace',
        'AmongUs',
        'apexlegends',
        'leagueoflegends',
        'Rainbow6',
        'Minecraft',
        'Overwatch',
        'Warframe',
        'SmashBrosUltimate',
        'terraria',
        'FIFA',
        'PS4',
        'xboxone',
        'NintendoSwitch',
        'pcgaming',
    ]


    insta_username = "username"
    insta_password = 'password'

    cl = Client()
    cl.login(insta_username, insta_password)

    subreddit = "Funnymemes"

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?=all"

    headers = {
        'User-Agent': 'put your user agent here (could be anything)'
    }

    response = requests.get(url, headers=headers)

    ls = []

    if not response.ok:
        print("Error : ", response.status_code)
        exit()

    data = response.json()['data']
    for post in data['children']:
        pdata = post['data']
        post_id = pdata['id']
        title = pdata['title']
        author = pdata['author']
        date = pdata['created_utc']
        url = pdata.get('url_overridden_by_dest')
        
        ls.append({"author" : author,
                    "title" : title,
                    "url" : url,
                    "date" : date,
                    "Post ID" : post_id})


    os.makedirs("images", exist_ok=True)


    instagram_tags = [
        '#gaming', '#gamers', '#gamerlife', '#gamingcommunity', '#videogames',
        '#gamestagram', '#instagaming', '#gamingislife', '#gamingsetup', '#gamingpc',
        '#gamergirl', '#gamerboy', '#gamingmemes', '#streamer', '#twitch',
        '#xbox', '#playstation', '#pcgaming', '#nintendo', '#esports',
        '#memes', '#funnymemes', '#dankmemes', '#memestagram', '#memepage',
        '#memelord', '#memegod', '#memehumor', '#memesdaily',
        '#funny', '#lol', '#hilarious', '#funnypost', '#humor', '#comedy',
        '#funnyvideos', '#funnypics', '#funnymoments', '#funnyshit',
        '#popular', '#instapopular', '#trending', '#viral', '#instafamous',
        '#instagood', '#photooftheday', '#picoftheday', '#instadaily'
    ]

    insta_tag = ""
    for e in instagram_tags:
        insta_tag += e + " " 

    for i in range(len(ls)):
        rs = random.choice(ls)
        image_url = rs["url"]
        image_title = rs["title"]
        author = rs["author"]
        
        img_data = requests.get(image_url).content
        
        image_path = f"images/{image_title}.jpg"
        with open(image_path, "wb") as i:
            i.write(img_data)
        
        image_title += f"Made by : {author} on reddit {random.choice(instagram_tags)} {random.choice(instagram_tags)} {random.choice(instagram_tags)} {random.choice(instagram_tags)}"
        
        try:
            time.sleep(1)
            cl.photo_upload(
                image_path,
                image_title
            )
            print(f"Uploading {image_title} succesful")
            
            counter += 1
            
            if counter == limit:
                shutil.rmtree("images")
                break
            
        except Exception as e:
            print(e)
        
schedule.every().day.at(f"08:{random.randint(10, 59)}").do(main)
schedule.every().day.at(f"12:{random.randint(10, 59)}").do(main)
schedule.every().day.at(f"21:{random.randint(10, 59)}").do(main)
schedule.every().day

while True:
 
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)