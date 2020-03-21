from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
	
from datetime import datetime
from covid import Covid
import pandas as pd


def index(request):
	covid = Covid()
	covid.get_data()
	countries = covid.list_countries()
	italy_cases = covid.get_status_by_country_id(32)
	lst  =[]
	for i in countries:
		va=covid.get_status_by_country_id(i['id'])
		# print(va)
		lst.append(va)
	country_1k = []
	country_10k = []
	lst_1k_active = []
	lst_10k_active = []
	for i in lst:
		if int(i['active']) <=800:
			lst_1k_active.append(i['active'])
			country_1k.append(i['country'])
		else:
			lst_10k_active.append(i['active'])
			country_10k.append(i['country'])
	return render(request,'index.html',{'covid':countries,'contry_cases':italy_cases,'country_10k':country_10k,'country_1k':country_1k,'lst_1k_active':lst_1k_active,'lst_10k_active':lst_10k_active});

def countries_form(request):
	covid = Covid()
	covid.get_data()
	italy_cases =''
	countries = covid.list_countries()
	if request.method =='POST':
		country_code = request.POST['id'];
		country_data = covid.get_status_by_country_id(country_code)

	covid = Covid()
	countries = covid.list_countries()
	
	lst  =[]
	
	for i in countries:
		va=covid.get_status_by_country_id(i['id'])
		lst.append(va)
	dic = {
    'country':'',
    'active':''}

	country_1k = []
	country_10k =[]
	lst_1k_active = []
	lst_10k_active = []


	for i in lst:
		if int(i['active']) <=800:
			lst_1k_active.append(i['active'])
			country_1k.append(i['country'])
		else:
			lst_10k_active.append(i['active'])
			country_10k.append(i['country'])

	print(active)

	context = {

	}
	print(active)
	# print ()
    	# print(i['country'],i['active'])
	return  render(request,'index.html',{	'covid':countries,	'contry_cases':country_data,'country_10k':country_10k,'country_1k':country_1k,'lst_1k_active':lst_1k_active,'lst_10k_active':lst_10k_active});
def countries_covid():
	covid = Covid()
	covid.get_data()
	print(covid)
	countries = covid.list_countries()
	for c in countries:
		country_cases = covid.get_status_by_country_id(c)
	italy_cases = covid.get_status_by_country_id(32)
	print(italy_cases)
	# dt_object = datetime.fromti mestamp(italy_cases.last_update)
	# # print(dt_object)


