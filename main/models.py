from datetime import datetime
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class Match(models.Model):
    player1 = models.ForeignKey(Player, related_name='match1') #team 1
    player2 = models.ForeignKey(Player, related_name='match2') #team 2
    player3 = models.ForeignKey(Player, related_name='match3', null=True, blank=True) #team 1
    player4 = models.ForeignKey(Player, related_name='match4', null=True, blank=True) #team 2
    score1 = models.IntegerField(default=0)
    score2 = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        return "%s vs. %s - %d:%d (%s)" % (self.player1, self.player2, self.score1, self.score2, str(self.date))
    
