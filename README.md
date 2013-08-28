django_rest_model_hyperlink_serializers_project
===============================================

installation can be done via
pip install djangorestrelationalhyperlink


A simple serializer that allows relations to be changed using the url while still allowsing to see/update/create
objects via normal methods.

the example above is a team -> player model

our initial pull brings in the teams and the players ie

```
{  
    "player_set":  
    [  
        {"url": "http://127.0.0.1:8000/rest_api/player/4/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "George Monroe"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/9/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "John Jeffereson"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/14/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "Thomas Adams"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/19/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "James Washington"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/21/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "James Jeffereson"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/24/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "James Van Buren"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/29/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "Andrew Quincy Adams"},  
        {"url": "http://127.0.0.1:8000/rest_api/player/34/", "team": "http://127.0.0.1:8000/rest_api/team/3/", "player_name": "Martin Monroe"}  
    ],  

    "url": "http://127.0.0.1:8000/rest_api/team/3/", "team_name": "team 3"  
}  
```

but if we want to add players to a team we can use the logic of a hyper linked field, ie, only use the url

ie PUT
```
{  
    partial: true,  
    player_set: ["http://127.0.0.1:8000/rest_api/player/13/"]  
    team_name: "team 1"  
}  
```


ie we can read and write to this serializer with dictionarys like a normal serializer but we can change relations with these objects
using urls. This is useful when pulling in large JSON structures without having to post back a lot of data to the server.

please note all this does is mirror the existing hyperlinked field logic, at the moment this only supports adding to the player set so the above put will only add to the player set not remove existing players




