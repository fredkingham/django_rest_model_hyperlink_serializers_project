from main.models import Team, Player
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "resets db and populates it."
    def handle(self, *args, **options):
        Team.objects.all().delete()
        Player.objects.all().delete()

        team_names = ["team 1", "team 2", "team 3", "team 4", "team 5"]

        for team in team_names:
            Team.objects.create(team_name=team)

        first_names = ["George", "John", "Thomas", "James", "Andrew", "Martin"]
        sir_names = ["Washington", "Adams", "Jeffereson", "Monroe", "Quincy Adams", "Van Buren"]

        team_number = 0
        team_count = Team.objects.count()
        for first_name in first_names:
            for sir_name in sir_names:
                team_number = (team_number + 1) % team_count + 1
                team = Team.objects.get(id = team_number)
                player_name = "%s %s" % (first_name, sir_name)
                Player.objects.create(player_name = player_name, team = team)



