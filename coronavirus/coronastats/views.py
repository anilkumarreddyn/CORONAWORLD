from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
	
from datetime import datetime
from covid import Covid
import pandas as pd

import schedule
import time



def active_cases(lst):
    top_country_active = []
    top_active  = []
    mid_active_country  = []
    mid_active  = []
    bottom_country_active  = []
    bottom_active  = []
    
    top_country_recovered = []
    top_recovered  = []
    mid_recovered_country  = []
    mid_recovered = []
    bottom_country_recovered  = []
    bottom_recovered  = []
    
    top_country_death = []
    top_deaths  = []
    mid_deaths = []
    mid_deaths_country = []
    bottom_country_deaths = []
    bottom_deaths = []
    
    lst_confirmed_700 = []
    lst_confirmed_country = []
    lst_confirmed_100 = []
    lst_confirmed_100_country = []
    lst_confirmed_10 = []
    lst_confirmed_10_country = []
    
    total_active=0
    for i in lst:
        if i['active']>=700:
            top_country_active.append(i['country'])
            top_active.append(i['active'])
        elif i['active']<700 and i['active']>=100:
            mid_active_country.append(i['country'])
            mid_active.append(i['active'])
        else:
            bottom_country_active.append(i['country'])
            bottom_active.append(i['active'])
            
        if i['recovered']>=700:
            top_country_recovered.append(i['country'])
            top_recovered.append(i['recovered'])
        elif i['recovered']<700 and i['recovered']>=100:
            mid_recovered_country.append(i['country'])
            mid_recovered.append(i['recovered'])
        else:
            bottom_country_recovered.append(i['country'])
            bottom_recovered.append(i['recovered'])
            
        if i['deaths']>=700:
            top_country_death.append(i['country'])
            top_deaths.append(i['deaths'])
	        # elif i['deaths']<700 and i['deaths']>=100:
	        #     mid_deaths_country.append(i['country'])
	        #     mid_deaths.append(i['deaths'])
        else:
            bottom_country_deaths.append(i['country'])
            bottom_deaths.append(i['deaths'])
        
        if i['confirmed'] >=5000:
            lst_confirmed_700.append(i['confirmed'])
            lst_confirmed_700_country.append(i['country'])
        elif i['confirmed']<5000 and i['confirmed']>=150:
            lst_confirmed_100.append(i['confirmed'])
            lst_confirmed_100_country.append(i['country'])
        else:
            lst_confirmed_10.append(i['confirmed'])
            lst_confirmed_10_country.append(i['country'])   

       #total_confirmed = i['confirmed']+total_confirmed
        total_active = i['active']+total_active
        #al_deaths=total_deaths+i['deaths']



    return top_country_active,top_active,mid_active_country,mid_active,bottom_country_active,bottom_active,top_country_recovered,top_recovered,mid_recovered_country,mid_recovered,bottom_country_recovered,bottom_recovered,top_country_death,top_deaths,mid_deaths,mid_deaths_country,bottom_country_deaths,bottom_deaths,lst_confirmed_700,lst_confirmed_700_country,lst_confirmed_100,lst_confirmed_100_country,lst_confirmed_10,lst_confirmed_10_country,total_active
           
from covid import Covid
covid = Covid()
covid.get_data()
countries = covid.list_countries()
lst  =[]
for i in countries:
    va=covid.get_status_by_country_id(i['id'])
    lst.append(va)
top_country_active = []
top_active  = []
mid_active_country  = []
mid_active  = []
bottom_country_active  = []
bottom_active  = []

top_country_recovered = []
top_recovered  = []
mid_recovered_country  = []
mid_recovered = []
bottom_country_recovered  = []
bottom_recovered  = []

top_country_death = []
top_deaths  = []
mid_deaths = []
mid_deaths_country = []
bottom_country_deaths = []
bottom_deaths = []

lst_confirmed_700 = []
lst_confirmed_700_country =[]
lst_confirmed_country = []
lst_confirmed_100 = []
lst_confirmed_100_country = []
lst_confirmed_10 = []
lst_confirmed_10_country = []


# top_country_active,top_active,mid_active_country,mid_active,bottom_country_active,bottom_active,top_country_recovered,top_recovered,mid_recovered_country,mid_recovered,bottom_country_recovered,bottom_recovered,top_country_death,top_deaths,mid_deaths,mid_deaths_country,bottom_country_deaths,bottom_deaths,lst_confirmed_700,lst_confirmed_700_country,lst_confirmed_100,lst_confirmed_100_country,lst_confirmed_10,lst_confirmed_10_country = active_cases(lst)








schedule.every(10).seconds.do(active_cases,lst)


def getDate(request):
	covid = Covid()
	covid.get_data()
	countries = covid.list_countries()
	lst  =[]
	for i in countries:
		va=covid.get_status_by_country_id(i['id'])
		lst.append(va)
		#print(va)
	top_country=[]    
	top_active=[]
	for i in lst:
		if i['active']>=700:
			top_country.append(i['country'])
			top_active.append(i['active'])
	print(top_active)
	print(top_country)		
	return render(request,'graphs.html',{'top_country':top_country,'top_active':top_active});
	
 

def index(request):
	# covid = Covid()
	covid.get_data()
	countries = covid.list_countries()
	lst  =[]
	for i in countries:
		va=covid.get_status_by_country_id(i['id'])
		lst.append(va)
	# top_country=[]    
	# top_active=[]
	# for i in lst:
	# 	if i['active']>=700:
	# 		top_country.append(i['country'])
	# 		top_active.append(i['active'])
	# print(top_active)
	# print(top_country)

	# top_country_active = []    
	# top_active = []

	# mid_active_country = []    
	# mid_active = []
	# bottom_country_active = [] 

	# bottom_active = []	
	# death_active  = []

	# for i in lst:
	# 	if i['active']>=700:
	# 		top_country_active.append(i['country'])
	# 		top_active.append(i['active'])
			
	# 	elif i['active']<700 and i['active']>=100:
	# 		mid_active_country.append(i['country'])
	# 		mid_active.append(i['active'])
	# 	else:
	# 		bottom_country_active.append(i['country'])
	# 		bottom_active.append(i['active'])

	# print (mid_active)
	# print(mid_active_country)

	# top_confirmed = []
	# top_confirmed_country = []
	
	# mid_confirmed = []
	# mid_confirmed_country = []

	# bottom_confirmed = []
	# bottom_confirmed_country = []
	# total_confirmed = 0

	# for i in lst:
	# 	if i['confirmed']>=700:
	# 		top_confirmed_country.append(i['country'])
	# 		top_confirmed.append(i['confirmed'])

	# 	elif i['confirmed']<700 and i['confirmed'] >=100:
	# 		mid_confirmed_country.append(i['country'])
	# 		mid_confirmed.append(i['confirmed'])
		
	# 	else:
	# 		bottom_confirmed_country.append(i['country'])
	# 		bottom_confirmed.append(i['confirmed'])
	# 	# total_confirmed  = total_confirmed + i['confirmed'] 
	top_country_active = []
	top_active  = []
	mid_active_country  = []
	mid_active  = []
	bottom_country_active  = []
	bottom_active  = []

	top_country_recovered = []
	top_recovered  = []
	mid_recovered_country  = []
	mid_recovered = []
	bottom_country_recovered  = []
	bottom_recovered  = []

	top_country_death = []
	top_deaths  = []
	mid_deaths = []
	mid_deaths_country = []
	bottom_country_deaths = []
	bottom_deaths = []

	lst_confirmed_700 = []
	lst_confirmed_700_country =[]
	lst_confirmed_country = []
	lst_confirmed_100 = []
	lst_confirmed_100_country = []
	lst_confirmed_10 = []
	lst_confirmed_10_country = []
	top_country_active,top_active,mid_active_country,mid_active,bottom_country_active,bottom_active,top_country_recovered,top_recovered,mid_recovered_country,mid_recovered,bottom_country_recovered,bottom_recovered,top_country_death,top_deaths,mid_deaths,mid_deaths_country,bottom_country_deaths,bottom_deaths,lst_confirmed_700,lst_confirmed_700_country,lst_confirmed_100,lst_confirmed_100_country,lst_confirmed_10,lst_confirmed_10_country,total_active = active_cases(lst)
	#print(top_country_active,top_active,mid_active_country,mid_active,bottom_country_active,bottom_active,top_country_recovered,top_recovered,mid_recovered_country,mid_recovered,bottom_country_recovered,bottom_recovered,top_country_death,top_deaths,mid_deaths,mid_deaths_country,bottom_country_deaths,bottom_deaths,lst_confirmed_700,lst_confirmed_700_country,lst_confirmed_100,lst_confirmed_100_country,lst_confirmed_10,lst_confirmed_10_country)
	# print("Mid Deaths Country",mid_deaths_country)
	# print("Mid Active",mid_deaths)
	# print(total_active)


	# context = 	{
	# 	'covid':countries,
	# 	# 'total_countries':lst,
	# 	'top_country':top_country_active,
	# 	'top_active':top_active
	# 	# 'mid_active':mid_active,
	# 	# 'mid_country':mid_active_country,
	# 	# 'bottom_active':bottom_active,
	# 	# 'bottom_country':bottom_country_active
	# 	# 'top_confirmed':top_confirmed,
	# 	# 'top_confirmed_country':top_confirmed_country,
	# 	# 'mid_confirmed':mid_confirmed,
	# 	# 'mid_confirmed_country':mid_confirmed_country,
	# 	# 'bottom_confirmed':bottom_confirmed,
	# 	# 'bottom_confirmed_country':bottom_confirmed_country
	# 	}

	total_confirmed = covid.get_total_confirmed_cases()
	total_recovered = covid.get_total_recovered()
	total_deaths = covid.get_total_deaths()

	return render(request,'index2.html',{'top_country_active':top_country_active,
			'top_active':top_active,'mid_active_country':mid_active_country,'mid_active':mid_active,
			'bottom_country_active':bottom_country_active,'bottom_active':bottom_active,'top_country_recovered':top_country_recovered,
			'top_recovered':top_recovered,'mid_recovered_country':mid_recovered_country,
			'mid_recovered':mid_recovered,'bottom_country_recovered':bottom_country_recovered,'bottom_recovered':bottom_recovered,
			'top_country_death':top_country_death,'top_deaths':top_deaths,'mid_deaths_country':mid_deaths_country,'mid_deaths':mid_deaths,
			'bottom_country_deaths':bottom_country_deaths,'bottom_deaths':bottom_deaths,'lst_confirmed_700_country':lst_confirmed_700_country,
			'lst_confirmed_700':lst_confirmed_700,'lst_confirmed_100_country':lst_confirmed_100_country,'lst_confirmed_100':lst_confirmed_100,
			'lst_confirmed_10_country':lst_confirmed_10_country,'lst_confirmed_10':lst_confirmed_10,
			'total_active':total_active,'total_confirmed':total_confirmed,'total_recovered':total_recovered,'total_deaths':total_deaths,
			'total_countries':lst


			});


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


	# print("top active",top_active)
	# print("top contry",top_country)

	# print("mid active",mid_active)
	# print("mid countries",mid_country)
	# print("bottom active",bottom_active)
	# print("bottom country",bottom_country)
	print (countries)

	return  render(request,'country_specific.html',{'covid':countries,'contry_cases':country_data});


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
	va=covid.get_status_by_country_id(32)


	context = {
		'covid':countries,
		'contry_cases':va
	}

	return render(request,'country_specific.html',context)



