import requests #used to request to get the info


base_url="https://www.googleapis.com/youtube/v3/commentThreads" #the url we are connecting to, usually we use ip address to connect to server

def get_comments(vid_ids): #variables are adjustable in python, also when u read stuff its a string
    acc_url=base_url+"?part=snippet&maxResults=100&videoId="+vid_ids
    response = requests.get(acc_url) #get the info from this url
    comments=response.json()
    print(comments)

vid_id = "_VB39Jo8mAQ"

get_comments(vid_id)

#gotta add cases based on exit code
