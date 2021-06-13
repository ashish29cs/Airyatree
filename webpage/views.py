from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib import auth
import sklearn 
import joblib
import pandas as pd
from django.contrib import messages

model = joblib.load(open("flight_rf.sav", "rb"))
model1 = joblib.load(open("flight_dt.sav", "rb"))
model2 = joblib.load(open("flight_knn.sav", "rb"))

def predict(request):
        date_dep = request.POST["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)


        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)


        date_arr = request.POST["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)


        dur_hour = abs(Arrival_hour*60 - Dep_hour*60)
        dur_min = abs(Arrival_min*1 - Dep_min*1)
    

        Total_stops = int(request.POST["stops"])

        airline=request.POST['airline']
        
        if(airline=='Jet Airways'):
                Jet_Airways = 1
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
            
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
        elif (airline=='IndiGo'):
                Jet_Airways = 0
                IndiGo = 1
                Air_India = 0
            
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
        
    

        elif (airline=='Air India'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 1
            
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
            
        elif (airline=='Multiple carriers'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
            
                Multiple_carriers = 1
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
            
        elif (airline=='SpiceJet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 1
            
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 
            
        elif (airline=='Vistara'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
            
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 1
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

        elif (airline=='Air Asia'):
                Jet_Airways = 0
                IndiGo = 0
           
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=1
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0 

        elif (airline=='GoAir'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
            
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 1
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

        elif (airline=='Multiple carriers Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
           
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 1
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

        elif (airline=='Jet Airways Business'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
            
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 1
                Vistara_Premium_economy = 0
                Trujet = 0

        elif (airline=='Vistara Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
           
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 1
                Trujet = 0
            
        elif (airline=='Trujet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
        
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 1

        else:
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
           
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                Air_Asia=0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

        Source = request.POST["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore=0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore=0
        
   


        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
            s_Bangalore=0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
            s_Bangalore=0
    
        elif (Source == 'Bangalore'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore=1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            s_Bangalore=0
    
        Destination = request.POST["Destination"]
        if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0
        
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0

        elif (Destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0

        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
            d_Bangalore=0

        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
            d_Bangalore=0

        elif (Destination == 'Bangalore'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
            d_Bangalore=0

        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            Air_Asia,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Bangalore,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_Bangalore,
            d_New_Delhi
        ]])

        prediction1=model1.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            Air_Asia,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Bangalore,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_Bangalore,
            d_New_Delhi
        ]])

        prediction2=model2.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            Air_Asia,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Bangalore,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_Bangalore,
            d_New_Delhi
        ]])

       

        
        global output
        global output1
        global output2
        
        output=round(prediction[0],2)
        output1=round(prediction1[0],2)
        output2=round(prediction2[0],2)
        
       
       

        return render(request,'home.html',{'prediction_text':output})


def result(request):
          return render(request,'result.html',{'prediction_text':output,'prediction_text1':output1,'prediction_text2':output2})
   
# Create your views here.
def home(request):
    return render(request,"homme.html")

def home1(request):
    return render(request,"home.html")

def intro(request):
    return render(request,"intro.html")
   
def method(request):
    return render(request,"methods.html")

def eda(request):
    return render(request,"eda.html")

def contact(request):
    return render(request,"contact.html")

def afterlogin(request):
    return render(request,"afterlogin.html")


def data(request):
    return render(request,"data.html")


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
             messages.error(request,'username alreday taken! Please try with other username')
             return render(request,'signup.html')
        else:
            x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            x.save()
            print("user created!")
            return redirect('signin')

    else:
        return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        x=auth.authenticate(username=uname,password=pwd)
        if x is not None:
            auth.login(request, x)
            return render(request,'afterlogin.html')
            
            
        else:
            messages.error(request,'username or password not correct')
            return redirect('signin')


    else:
        return render(request,'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('home')