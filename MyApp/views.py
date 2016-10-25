from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from MyApp.models import ComplteStockDetails, DealersInfo, Person
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# Create your views here.

class LoadView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home.html')


class StockView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			model = ComplteStockDetails
			objs = ComplteStockDetails.objects.all()
			return render_to_response('show_stock.html',
									  {'data': objs, 'itemnames': [obj.item_name for obj in objs]})
		else:
			return HttpResponseRedirect('/load/')

class BachtoHomeView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return render_to_response('login_welcome.html', {'user': request.user.username})
		else:
			return HttpResponseRedirect('/load/')

class LoginView(View):
	def post(self, request, *args, **kwargs):
		import pdb
		pdb.set_trace()
		user = authenticate(username=request.POST.get('user'), 
							password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return render_to_response('login_welcome.html', {'user': request.GET.get('user')})
			else:
				return HttpResponseRedirect('/load/')

		else:
			return HttpResponseRedirect('/load/')

class LoadContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'contact.html')

class ContactView(View):
	def get(self, request, *args, **kwargs):
		data = request.GET
		msg = MIMEMultipart()
		msg['From'] = "Pavana Medicals"
		msg['To'] = 'h.sarma212@gmail.com'
		msg['Subject'] = "Comment :: " + str(data.get('name')) + " Mobile - "+ data.get('mobile') + " Mail - " + data.get('mail')
		message = data.get('comment')
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP("smtp.mail.yahoo.com",587)
		# identify ourselves to smtp gmail client
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
		mailserver.login('h_sarma@ymail.com', 'GhsKanna212$')

		mailserver.sendmail('h_sarma@ymail.com','h.sarma212@gmail.com',msg.as_string())

		mailserver.quit()
		return HttpResponseRedirect('/load/')

class SelectedStockSearchView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			objs = ComplteStockDetails.objects.filter(item_name=str(request.GET.get('itemname')))
			return render_to_response('show_stock.html',
									  {'data': objs,
									   'itemnames': [i.item_name for i in ComplteStockDetails.objects.all()]})
		else:
			return HttpResponseRedirect('/load/')


class ShowDealerView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			objs = DealersInfo.objects.all()
			return render_to_response('dealers.html', {'data': objs})
		else:
			return HttpResponseRedirect('/load/')


class LogoutView(View):
	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/load/')