# RedditTerminator
import praw

# reddit api login
reddit = praw.Reddit(client_id='ID here',
                     client_secret='Secret here',
                     username='Username Here',
                     password='Password Here',
                     user_agent='Reddit Terminator by u/LunaFr0st')
                    
# the subreddits you want your bot to live on
subreddit = reddit.subreddit('all')

# phrase to activate the bot
keywords = [' Connor ', ' connor ', ' John ', ' john ',' Sarah ', ' sarah ', 'terminate ', ' Terminate']
# what the bot replies with
replies = ['WHERE IS JOHN CONNOR?!','WHERE IS JOHN CONNOR?!','WHERE IS JOHN CONNOR?!','WHERE IS JOHN CONNOR?!','WHERE IS SARAH CONNOR?!','WHERE IS SARAH CONNOR?!','YOU WILL BE TERMINATED!','YOU WILL BE TERMINATED!']


# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    for i in range(len(keywords)):
        reply = replies[i]
        if keywords[i] in comment.body:
            try:
                comment.reply(reply)
                print('Replied with: ' + reply)
            except:
                print('Too Frequent of Attempts')