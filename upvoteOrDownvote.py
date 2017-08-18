upvote_list = []
downvote_list = []

class Names:
    "Database that holds the users of who I want to downvote/upvote"
    def __init__(self, name, upvote=0, downvote=0):
        #change Upvote if you want to put them in the upvote file, downvote if you want to put 
        #them in the downvote file
        global upvote_list
        global downvote_list
        #I need these as global because I have to access them outside of this class/file
        self.IGN = name
        self.upvote = upvote
        self.downvote = downvote
        if upvote == 1 and downvote == 0:
            #Append upvote_list with self.name
            upvote_list.append(self.IGN)
        elif upvote == 0 and downvote == 1:
            #Append downvote_list with self.name
            downvote_list.append(self.IGN)

Names("CrackerJack7209", 1, 0)
Names("PSN_GAMER", 1, 0)
Names("Frensin", 1, 0)
Names("Zrainh20", 1, 0)
Names("Searednumber2", 1, 0)
Names("Coni_s2", 0, 1)
Names("sintralin", 0, 1)
Names("Crimeo", 0, 1)
