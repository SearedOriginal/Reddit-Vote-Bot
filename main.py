import praw
from accounts import *
import logging


#Upvote_Users says who you want to upvote. Do caps matters?
upvote_users = ("PSN_GAMER", "CrackerJack7209", "Frensin", "Zrainh20", "Searednumber2")
#downvote_users says who you want to downvote. Do caps matter?
downvote_users = ("Coni_s2", "sintralin", "Crimeo")

def vote_posts(reddit_account):
#You can add as many reddit accounts to this as you want, just make sure to call them later on with the account
    "Downvotes posts or upvotes posts accordingly to who you want to downvote/upvote"
    subreddit = reddit_account.subreddit("Civclassics").new()
    for submission in subreddit:
        if submission.author in downvote_users:
            submission.downvote()
            print("I downvoted {}, posted by {}".format(submission.title, submission.author))
        elif submission.author in upvote_users:
            submission.upvote()
            print("I upvoted {}, posted by {}".format(submission.title, submission.author))

def vote_on_comments(reddit_account):
    "Downvotes or upvotes comments on posts accordingly"
    subreddit = reddit_account.subreddit("Civclassics").stream.comments()
    for comment in subreddit:
        if comment.author in upvote_users:
            comment.upvote()
            print("I just upvoted {}. The text body was '{}'".format(comment.author, comment.body))
        elif comment.author in downvote_users:
            comment.downvote()
            print("I just downvoted {}. The text body was '{}'".format(comment.author, comment.body))

#vote_posts(SearedNumber2)
#vote_on_comments(SearedNumber2)

vote_posts(KillAllTrolls)       
vote_on_comments(KillAllTrolls)