from django.shortcuts import render
from django.http import HttpResponse
from .models import reservations
from .models import foodorders
from .models import feedbacks
# Create your views here.

def index(request):
	return render(None,"index.html", {'testvar':'test string 2'})

def form(request):
	return render(request,"form.html", {'testvar':'test string 2'})

def about(request):
	return render(request,"about.html", {'testvar':'test string 2'})

def rooms(request):
	return render(request,"rooms.html", {'testvar':'test string 2'})

def contact(request):
	return render(request,"contact.html", {'testvar':'test string 2'})

def order(request):
	return render(request,"foodform.html", {'testvar':'test string 2'})	

def feedback1(request):


	return render(request,"feedbackform.html", {'testvar':'test string 2'})

def feedback(request):
	#here

	cnic = request.POST.get('cnic', False)

	feed = request.POST.get('feed', False)

	feed = feedbacks(cnic = cnic, feed = feed)
	feed.save()

	return render(request,"feedinsert.html", {'testvar':'test string 2'})	

def foodorder(request):
	name = request.POST.get('name', False)

	room = request.POST.get('room', False)
	items =  request.POST.get('items', False)

	cnic =  request.POST.get('cnic', False)

	food = foodorders(name = name,room = room, items = items, cnic = cnic)

	food.save() 

	return render(request,"finsert.html", {'testvar':'test string 2'})	

def reserve(request):
	date_from = request.POST.get('date_from', '00:00:00')
	date_to = request.POST.get('date_to', '00:00:00')
	room_type = request.POST.get('room_type', False)
	adults = request.POST.get('adults', False)
	children = request.POST.get('children', False)
	name = request.POST.get('name', False)
	gender = request.POST.get('gender', False)
	email = request.POST.get('email', False)
	phone = request.POST.get('phone', False)
	age = request.POST.get('age', False)
	cnic = request.POST.get('cnic', False)
	method = request.POST.get('method', False)

	reserve = reservations(date_from = date_from,date_to = date_to,room_type = room_type, adults = adults,children = children, name = name, gender = gender, email = email, phone = phone, age = age, cnic = cnic, method = method)
	reserve.save()



	return render(request,"insert.html", {'testvar':'test string 2'})	