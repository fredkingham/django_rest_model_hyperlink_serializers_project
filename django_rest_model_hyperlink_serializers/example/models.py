from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=250)

    def __repr__(self):
        return "%s:%s" % (self.__class__, self.team_name)

class Player(models.Model):
    team = models.ForeignKey(Team)
    player_name = models.CharField(max_length=250)

    def __repr__(self):
        return "%s: %s-%s" % (self.__class__, self.player_name, self.team.team_name, )
