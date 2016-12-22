from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Poke
# from django.db import models
from django.db.models import Count

def index(request):
    return render(request, 'mainapp/index.html')

def register_process(request):
	if request.method == "POST":
		result = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'], request.POST['confirm_password'], request.POST['dateofbirth'])

		if result[0]==True:
			request.session['id'] = result[1].id
			print result, "*******************************************************"
			# request.session.pop('errors')
			return redirect('/success')
		else:

			# request.session['errors'] = result[1]
			messages.add_message(request, messages.WARNING, result[1][0])


			return redirect('/')
	else:

		return redirect ('/')

def login_process(request):
	print "------------ POST ----------------\n", request.POST
	result = User.objects.login(request.POST['email'],request.POST['password'])

	if result[0] == True:
		request.session['id'] = result[1][0].id
		# We have result[1][0] this refers to the results of the query (user query returned) and index of zero which is what we just unwrapped.
		return redirect('/success')
	else:
		messages.add_message(request, messages.WARNING, result[1][0])

		# request.session['errors'] = result[1]
		return redirect('/')

def success(request):
    if not 'id' in request.session:
        return redirect('/')
    else:
        session = request.session['id']
        loggedInUser = User.objects.get(id=session)
        res = User.objects.all().exclude(id=session).order_by('-created_at')
        allpokes = Poke.objects.all().values('poked').annotate(poke_count=Count('poked'))
        pokerCount = Poke.objects.filter(poked_id=session).values('poker').annotate(poke_count=Count('poker'))

        peoplewhopoked = {}
        for poking in pokerCount:
            todictionary = User.objects.get(id=poking['poker']).first_name
            peoplewhopoked[todictionary] = poking['poke_count']

        print "our dictionary", peoplewhopoked




        pokelist = Poke.objects.filter(poked_id=session).annotate(poker_name=Count('poker')).order_by('created_at')






        print pokerCount, "^"*100
        data = {
            'allUsers': res,
            'loggedInUser': loggedInUser,
            'allpokes': allpokes,
            'pokerCount': pokerCount,
            'pokelist': pokelist,
            'peoplewhopoked': sorted(peoplewhopoked.items())
            }
        return render(request, 'mainapp/success.html', data)

def poke(request, id):
    session = request.session['id']
    Poke.objects.poke(session, id)
    return redirect('/success')

def logout(request):
    del request.session['id']
    return redirect('/')
