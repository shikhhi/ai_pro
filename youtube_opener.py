import json
import time
import urllib

from selenium import webdriver


def look_for_new_video():
    api_key="AIzaSyC3NbuZvctnUW-MZ1gcY_QgwqGq4R_y__g"
    channel_id="UCz8hqZBa8bOthT5PE3TdUmg"

    base_video_url= 'https://www.youtube.com/watch?v='
    base_search_url= 'https://www.googleapis.com/youtube/v3/search?'

    url=base_search_url+'key={}&channelId={}&part=snippet,id&or=date&maxResults=1'.format(api_key, channel_id)
    inp=urllib.urlopen(url)
    resp=json.load(inp)

    vidID=resp['items'][0]['id']['videoId']

    with open('videoid.json','r') as json_file:
        data=json.load(json_file)
        if data['videoId']!=vidID:
            driver=webdriver.Firefox()
            driver.get(base_video_url+viddID)
            video_exists=True
            if video_exists:
                with open('videoid.json','w') as json_file:
                    data= {'videoId': vidID}
                    json.dump(data, json_file)

try: 
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print("stopping")