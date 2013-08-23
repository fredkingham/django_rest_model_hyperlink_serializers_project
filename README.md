django_rest_model_hyperlink_serializers_project
===============================================

installation can be done via
pip install djangorestrelationalhyperlink


A simple serializer that allows relations to be changed using the url while still allowsing to see/update/create
objects via normal methods.

ie we can read and write to this serializer with dictionarys like a normal serializer but we can change relations with these objects
using urls

so if we had a Team Serialzer(ModelSerializer) which had a Player Serializer (HyperLinkedRelationalSerializer)

the team serializer can change add players to their team using only the player url

ie with args such as
{partial: true, player_set: ["http://127.0.0.1:8000/rest_api/player/28/"], team_name: "team 1"}





