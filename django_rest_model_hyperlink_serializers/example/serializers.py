from rest_framework.relations import HyperlinkedRelatedField
from rest_framework import serializers
from hyperlinked_relational_serializer.serializers import HyperLinkedRelationalSerializer
from example.models import *


# a) I want to look at how the rest framework deals with relationships
# b) for this we can just create our player to team model, I think neither framework handles this well
# c) so if we delete the relationship what happens
class PlayerSerializer(HyperLinkedRelationalSerializer):
    class Meta:
        view_name = "player-detail"
        queryset = Player.objects.all()


class TeamSerializer(HyperLinkedRelationalSerializer):
    player_set = PlayerSerializer(many=True, required=False)

    class Meta:
        model = Team




