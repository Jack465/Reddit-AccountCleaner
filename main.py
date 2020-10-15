import praw

reddit = praw.Reddit(client_id='#####',
                client_secret='####',
                user_agent='Reddit Account Cleaning Script',
                username='####',
                password='#####')

#change the .submissions to .comments to scrub all your comments. 
for sub in reddit.redditor('YourUserName').submissions.new(limit=None):
    try:
        sub.edit("deleted") # prevents caching software like removeddit.com from showing your deleted content
    except:
        continue
    sub.delete()
    print("deleted ", sub.id)
