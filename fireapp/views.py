import time
from datetime import datetime, timezone
import pytz
from django.shortcuts import redirect, render
from django.contrib import messages
import pyrebase

app_config = {
    "apiKey": "AIzaSyAgPotrNQzZcM22I6a5Ic_v-fp1DDSUwRA",
    "authDomain": "iqubedj.firebaseapp.com",
    "projectId": "iqubedj",
    "storageBucket": "iqubedj.appspot.com",
    "messagingSenderId": "635827728558",
    "appId": "1:635827728558:web:c2af1752d667eb61a4fd3f",
    "measurementId": "G-HQ300JWPHP",
    "databaseURL" : "https://iqubedj-default-rtdb.firebaseio.com/",
}

firebase = pyrebase.initialize_app(app_config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.
def index(request):
    return render(request, "fireapp/index.html")

def post_form(request):

    if request.method == "POST":
        # data collection
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        country = request.POST.get('country')

        # id creation
        time_zone = pytz.timezone("Asia/Kolkata")
        time_now = datetime.now(timezone.utc).astimezone(time_zone)
        milli = int(time.mktime(time_now.timetuple())) 

        if password1 == password2:
            data = {
                "fullname" : fullname,
                "username" : username,
                "email"    : email,
                "password1" : password1,
                "password2" : password2,
                "mobile"   : mobile,
                "country"  : country,
            }

            database.child('data').child(username).child('user_data').set(data)
            msg = "Successfully added to database"
            messages.success(request, msg)
        else:
            msg = "Passwords don't match"
            messages.error(request, msg)

    return redirect('index')

