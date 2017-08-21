import praw
from accounts import Searednumber2
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
            pass

def vote_on_comments(reddit_account):
    "Downvotes or upvotes comments on posts accordingly"
    subreddit = reddit_account.subreddit("Civclassics").new()
    for submission in subreddit:
       for comment in submission.comments:
            if comment.author in upvote_list:
                comment.upvote()
                print("I just upvoted {}'s comment".format(comment.author))
            elif comment.author in downvote_list:
                comment.downvote()
                print("I just downvoted {}'s comment".format(comment.author))
            else:
                pass
#1:01 for the double loop in seperate function
#2:25 for the triple loop in same function
#conclusion is to use seperate functions, as that is 100~% faster