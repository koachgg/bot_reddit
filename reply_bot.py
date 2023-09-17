import praw
from PyDictionary import PyDictionary
import enchant

# reddit = praw.Reddit("koachgg")
#
# #reddit.login(REDDIT_USERNAME, REDDIT_PASS)

reddit = praw.Reddit(
    client_id= "UVGE-yneC4-_ALY7tutc2A",
    client_secret="mJwu7Q7knbrzn5jyucdLESwlmfwx-Q",
    username = "Acceptable_Till_600",
    password = "redditbot",
    user_agent="Acceptable_Till_600"
)

dictionary = PyDictionary()
d = enchant.Dict("en_US")

# check if the word is real
def isWord(word):
    return d.check(word)

subreddit = reddit.subreddit('words')

# phrase to activate the bot
keyphrase = '!actbot'

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
            if isWord(word):
                # get meaning as object, get the index of a sentence and reply it
                words = dictionary.meaning(word)
                reply = [item[0] for item in words.values()]
                comment.reply(word + ': '  + reply[0])
                print('posted')
            else:
                reply = 'This is not a word.'
                comment.reply(reply)
                print('posted')
        except:
            print('to frequent')
