from gdata import youtube as yt
from gdata.youtube import service as yts

client = yts.YouTubeService()
client.ClientLogin("k.jinuraj@gmail.com", "123kottackal@") #the pwd might need to be application specific fyi

comments = client.GetYouTubeVideoComments(video_id='GDEshyq7wRY')
a_comment = comments.entry[0]