import praw
from accounts import KillAllTrolls
from upvoteOrDownvote import *

def vote_posts(reddit_account):
#You can add as many reddit accounts to this as you want, just make sure to call them later on with the account
    "Downvotes posts or upvotes posts accordingly to who you want to downvote/upvote"
    subreddit = reddit_account.subreddit("Civclassics").new()
    for submission in subreddit:
        if submission.author in downvote_list:
            submission.downvote()
            print("I downvoted {}, posted by {}".format(submission.title, submission.author))
        elif submission.author in upvote_list:
            submission.upvote()
            print("I upvoted {}, posted by {}".format(submission.title, submission.author))
        else:
            print("This submission was posted by {}".format(submission.author))

def vote_on_comments(reddit_account):
    "Downvotes or upvotes comments on posts accordingly"
    subreddit = reddit_account.subreddit("Civclassics").stream.comments()
    for comment in subreddit:
        if comment.author in upvote_list:
            comment.upvote()
            print("I just upvoted {}'s comment".format(comment.author))
        elif comment.author in downvote_list:
            comment.downvote()
            print("I just downvoted {}'s comment".format(comment.author))
        else:
            print("This comment was posted by {}".format(comment.author))

vote_posts(KillAllTrolls)
vote_on_comments(KillAllTrolls)