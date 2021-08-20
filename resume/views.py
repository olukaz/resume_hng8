from django.http import HttpResponse
from django.shortcuts import render



def index(request):
	if request.method =='POST':

		name = request.POST.get('full-name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('message')

		data = {
				'name': name,
				'email': email,
				'subject': subject,
				'message': message
		}

		print(data)

		return HttpResponse("Thank you for submitting the form, we will be in touch soon")

	return render(request, 'home.html', {})


