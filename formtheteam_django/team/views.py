from django.shortcuts import render

def teams_list(request):
    return render(request, "team/teams_list.html")