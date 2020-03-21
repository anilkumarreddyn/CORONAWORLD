from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
	
from datetime import datetime
from covid import Covid
import pandas as pd


def index(request):
	covid = Covid()
	covid.get_data()
	#print(covid)
	countries = covid.list_countries()
	italy_cases = covid.get_status_by_country_id(32)
	deaths =covid.get_total_deaths()
	recovered = covid.get_total_recovered()
	lst  =[]
	lst_death = []
	
	for i in countries:
		va=covid.get_status_by_country_id(i['id'])

		# print(va)
		lst.append(va)

	dic = {
    'country':'',
    'active':''}


	total_confirmed = 0
	top_country=[]    
	top_active=[]
	mid_country=[]    
	mid_active=[]
	bottom_country=[]    
	bottom_active=[]	
	death_active  =[]


	
	for i in lst:
		if i['active']>=700:
			top_country.append(i['country'])
			top_active.append(i['active'])
			
		elif i['active']<700 and i['active']>=100:
			mid_country.append(i['country'])
			mid_active.append(i['active'])
		else:
			bottom_country.append(i['country'])
			bottom_active.append(i['active'])
			
		

	top_death = []
	top_death_country = []

	bottom_death_country = []
	bottom_death =[]

	mid_death = []
	mid_death_country = []

	for i in lst:
		if i['deaths']>=700:
			top_death_country.append(i['country'])
			top_death.append(i['deaths'])

		elif i['deaths']<700 and i['deaths']>=100:
			mid_death_country.append(i['country'])
			mid_death.append(i['deaths'])
		else:
			bottom_death_country.append(i['country'])
			bottom_death.append(i['deaths'])
	top_confirmed = []
	top_confirmed_country = []
	
	mid_confirmed = []
	mid_confirmed_country = []

	bottom_confirmed = []
	bottom_confirmed_country = []

	for i in lst:
		if i['confirmed']>=700:
			top_confirmed_country.append(i['country'])
			top_confirmed.append(i['confirmed'])

		elif i['confirmed']<700 and i['confirmed']>=100:
			mid_confirmed_country.append(i['country'])
			mid_confirmed.append(i['confirmed'])
		
		else:
			bottom_confirmed_country.append(i['country'])
			bottom_confirmed.append(i['confirmed'])
		total_confirmed  = total_confirmed + i['confirmed'] 



	print(top_active)
	print(top_country)

	print(mid_active)
	print(mid_country)
	print(bottom_active)
	print(bottom_country)



	return render(request,'index.html',{'covid':countries,'contry_cases':italy_cases,'top_country':top_country,'top_active':top_active,
		'bottom_country':bottom_country,'bottom_active':bottom_active,
		'mid_country':mid_country,'mid_active':mid_active,'top_death':top_death,'top_death_country':top_death_country,'mid_death':mid_death,'mid_death_country':mid_death_country,'bottom_death':bottom_death,
		'bottom_death_country':bottom_death_country,'top_confirmed':top_confirmed,'top_confirmed_country':top_confirmed_country,'mid_confirmed':mid_confirmed,'mid_confirmed_country':mid_confirmed_country,'bottom_confirmed':bottom_confirmed,'bottom_confirmed_country':bottom_confirmed_country,'total_death':deaths,'recovered':recovered,
		'total_confirmed':total_confirmed,'total_countries':lst});

def countries_form(request):

	covid = Covid()
	covid.get_data()
	#print(covid)
	italy_cases =''
	countries = covid.list_countries()
	if request.method =='POST':
		country_code = request.POST['id'];
		country_data = covid.get_status_by_country_id(country_code)



	
	lst  =[]
	
	for i in countries:
		va=covid.get_status_by_country_id(i['id'])
		# print(va)
		lst.append(va)

	total_confirmed = 0
	top_country=[]    
	top_active=[]
	mid_country=[]    
	mid_active=[]
	bottom_country=[]    
	bottom_active=[]	
	death_active  =[]
	top_death = []
	bottom_death =[]
	mid_death = []
	top_confirmed = []
	mid_confirmed = []
	bottom_confirmed = []
	for i in lst:
		if i['active']>=700:
			top_country.append(i['country'])
			top_active.append(i['active'])
			# top_death.append(i['deaths'])
			# top_confirmed.append(i['confirmed'])
		elif i['active']<700 and i['active']>=100:
			mid_country.append(i['country'])
			mid_active.append(i['active'])
			# mid_death.append(i['deaths'])
			# mid_confirmed.append(i['confirmed'])
		else:
			bottom_country.append(i['country'])
			bottom_active.append(i['active'])
			# bottom_death.append(i['deaths'])
			# bottom_confirmed.append(i['confirmed'])
		# total_confirmed  = total_confirmed + i['confirmed'] 


	print("top active",top_active)
	print("top contry",top_country)

	print("mid active",mid_active)
	print("mid countries",mid_country)
	print("bottom active",bottom_active)
	print("bottom country",bottom_country)




	return  render(request,'country_specific.html',{'covid':countries,'contry_cases':country_data,'top_country':top_country,'top_active':top_active,
		'bottom_country':bottom_country,'bottom_active':bottom_active,'mid_country':mid_country,'mid_active':mid_active});
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



def country_vise(request):

	covid = Covid()
	covid.get_data()
	#print(covid)
	countries = covid.list_countries()

	context = {
		'covid':countries,
	}
	return render(request,'country_specific.html',context)
