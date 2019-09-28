import pafy 
  
# url of video 
url = "https://www.youtube.com/watch?v=auJWhRCcZSM"
  
# instant created 
video = pafy.new(url) 
  
# print title 
print("Title:"+video.title) 
  
# print rating 
print("Rating:{}".format(video.rating))
  
# print viewcount 
print("Views:{}".format(video.viewcount))
  
# print author & video length 
print(video.author, video.length)

#print like and dislikes
print("likes:{} Dislike:{}".format(video.likes,video.dislikes))

# print duration& description 
print(video.duration, video.description) 


