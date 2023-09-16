import praw
import pdb
import re
import os

reddit = praw.Reddit("koachgg")

#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

if not os.path.isfile('post_replied_to.txt'):
    post_replied_to = []

else:
    with opem("post_replied_to.txt","r") as f:
        post_replied_to = f.read()
        post_replied_to = post_replied_to.split("\n")
        post_replied_to = list(filter(None,post_replied_to))

    subreddit = reddit.subreddit("'pythonforengineers")
    for submission in subreddit.hot(limit=5):
        if submission not in post_replied_to:
            if re.search('i love python',submission.title,re.IGNORECASE):
                submission.reply("koachgg bot says: It's all about the credit (and Python)")
                print("Bot replying to : ", submission.title)

                posts_replied_to.append(submission.id)



     with open("posts_replied_to.txt", "w") as f:
         for post_id in posts_replied_to:
             f.write(post_id + "\n")
