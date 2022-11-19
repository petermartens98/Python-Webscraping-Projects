from youtube_comment_scraper_python import *
import pandas as pd

youtube.open("https://www.youtube.com/watch?v=klpbY7pwYF4")
youtube.keypress("pagedown")

data = []
currentpagesource = youtube.get_page_source()
lastpagesource = ''

while (True):
    if (lastpagesource == currentpagesource):
        break

    lastpagesource = currentpagesource
    response = youtube.video_comments()

    for c in response['body']:
        data.append(c)

    youtube.scroll()
    currentpagesource = youtube.get_page_source()

df = pd.DataFrame(data)
df = df.replace('\n',' ', regex=True)
df = df[['Comment', 'Likes']].drop_duplicates(keep="first")
df.to_csv('data.csv',index=False)

print("code completed")
