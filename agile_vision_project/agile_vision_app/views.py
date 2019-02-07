from rest_framework import views, response

def get_team_data(team):
    return {
        'name' : team.name
    }