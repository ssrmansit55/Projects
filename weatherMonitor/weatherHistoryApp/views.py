from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

@csrf_protect
def login_view(request):

    if request.method == 'GET':
        if request.user.is_authenticated():
            flag = False
            for gp in request.user.groups.all():
                if gp.name == "admin":
                    flag = True
                    break
            if not flag:
                return render_to_response('index.html', context_instance=RequestContext(request))
            else:
                return HttpResponseRedirect('mainpage')
        else:
            return render_to_response('index.html', context_instance=RequestContext(request))
    elif request.method == 'POST':
        try:
            username = request.POST['email']
            password = request.POST['password']
            user = User.objects.get(username=username)
            flag = False
            for gp in user.groups.all():
                if gp.name == "admin":
                    flag = True
                    break
            if not flag:
                return render_to_response("index.html", {
                    'msg': 'You are not authorized to login here. This incident will be reported.'},
                                          context_instance=RequestContext(request))

            if user.check_password(password):
                user = authenticate(username=username, password=password)
                login(request, user)

                return HttpResponseRedirect('mainpage')
            else:
                return render_to_response('index.html', {'msg': "Invalid Email/Password"},
                                          context_instance=RequestContext(request))
        except ObjectDoesNotExist:
            return render_to_response('index.html', {'msg': "This user doesn't exist"},
                                      context_instance=RequestContext(request))
        except Exception:
            return render_to_response('index.html', {'msg': "You need to login to access the page"},
                                      context_instance=RequestContext(request))

@csrf_protect
def mainPanel(request):

    stations_all = Station.objects.all()
    stations = []
    for y in stations_all:
        stations.append(y.name)

    return render_to_response('main_page.html', {'res': stations_all, 'stations': sorted(stations)},
                              context_instance=RequestContext(request))

def addStation(request):

    if request.method == 'POST':
        name = request.POST.get('name', None)
        id = request.POST.get('id', None)
        url_suffix = request.POST.get('url_suffix', None)

        response_data = {}

        name = name.strip()
        if (len(name) == 0 or len(name) > 50):
            return JsonResponse({'status': 'failure', 'message' : 'Wrong request. Check request parameters again'})

        id = id.strip()
        if (not id.isnumeric()):
            return JsonResponse({'status': 'failure', 'message': 'Wrong request. Check request parameters again'})

        url_suffix = url_suffix.strip()
        if (len(url_suffix) < 3 or len(url_suffix) > 70 or ('/' not in url_suffix[1:-1])):
            return JsonResponse({'status': 'failure', 'message': 'Wrong request. Check request parameters again'})

        try:
            Station.objects.get(id = id)
            return JsonResponse({'status': 'failure', 'message': 'ERROR! Entry with given ID already exists!'})
        except:
            try:
                s = Station(name=name, id=id, url_suffix=url_suffix)
                s.save()
            except:
                return JsonResponse({'status': 'failure', 'message': 'ERROR! unable to save object!'})

        return JsonResponse({'status': 'success', 'data': sorted([x.name for x in Station.objects.all()])})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/weather-history')
