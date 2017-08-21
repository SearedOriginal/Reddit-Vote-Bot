import praw
from accounts import *
from upvoteOrDownvote import *
from Massupdown import *


def massvote():
    vote_posts(Searednumber2)
    vote_on_comments(Searednumber2)
    vote_posts(KillAllTrolls)
    vote_on_comments(KillAllTrolls)



#Call what option you want