from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from fooz.main.models import Player, Match

from datetime import datetime

import json

def index(request):
    matches = Match.objects.all().order_by('date')
    players = Player.objects.all()
    return render_to_response('main.html', {'matches' : matches, 'players' : players}, context_instance=RequestContext(request))

def match(request):
    p1 = Player.objects.get(id=int(request.POST.get('p1')))
    p2 = Player.objects.get(id=int(request.POST.get('p2')))
    try:
        p3 = Player.objects.get(id=int(request.POST.get('p3')))
        p4 = Player.objects.get(id=int(request.POST.get('p4')))
    except:
        p3 = None
        p4 = None
        
    s1 = int(request.POST.get('s1'))
    s2 = int(request.POST.get('s2'))
    
    if None not in (p1, p2, s1, s2):
        date = datetime.now()
        match = Match(player1=p1, player2=p2, score1=s1, score2=s2, date=date)
        match.save()
    
    return HttpResponseRedirect('/')

def test(request):
    matches = Match.objects.all().order_by('date')
    return HttpResponse(json.dumps(matches))