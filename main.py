import praw

Searednumber2 = praw.Reddit(client_id = "",
                    client_secret = "",
                    password = "",
                    user_agent = "Seared",
                    username = "")

KillAllTrolls = praw.Reddit(client_id = "",
                    client_secret = "",
                    password = "",
                    user_agent = "Seared2",
                    username = "")

#Upvote_Users says who you want to upvote. Do caps matters?
upvote_users = ("PSN_GAMER", "CrackerJack7209", "Frensin", "Zrainh20", "Searednumber2")
#downvote_users says who you want to downvote. Do caps matter?
downvote_users = ("Coni_s2", "sintralin", "Crimeo")

def vote_posts(reddit_account):
#You can add as many reddit accounts to this as you want, just make sure to call them later on with the account
    "Downvotes posts or upvotes posts accordingly to who you want to downvote/upvote"
    for submission in reddit_account.subreddit("Civclassics").new():
        if submission.author in downvote_users:
            submission.downvote()
            print("I downvoted {}, posted by {}".format(submission.title, submission.author))
        elif submission.author in upvote_users:
            submission.upvote()
            print("I upvoted {}, posted by {}".format(submission.title, submission.author, ))

vote_posts(Searednumber2)
vote_posts(KillAllTrolls)