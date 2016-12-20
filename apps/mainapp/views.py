from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Poker

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
        pokes = Poker.objects.filter(user_id=5)
        pokeCount = pokes.count()
        print pokeCount, "%"*300
        data = {
            'allUsers': res,
            'loggedInUser': loggedInUser,
            'pokeCount': pokeCount
            }
        return render(request, 'mainapp/success.html', data)

def poke(request, id):
    session = request.session['id']
    Poker.objects.poke(session, id)
    return redirect('/success')

def logout(request):
    del request.session['id']
    return redirect('/')
