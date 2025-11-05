from django.shortcuts import render, HttpResponse
from main.models import Contact
from main.models import Sign_up

# Create your views here.
def harry(request):
    #return HttpResponse("Haris Ali Khan, also known as Harry, is an Indian YouTuber who makes videos about coding and teaches many programming languages through YouTube videos on his channel CodeWithHarry which has over 1 million subscribers. He is from Rampur, Uttar Pradesh and has graduted from IIT Kharagpur in B.Tech. He is a full-time software engineer in a company.     His channel's about page says that its his attempt to teach coding basics to people which took him ages to learn.He also has created his own website from Python Flask (codewithharry.com). He has two more channels, namely ProgrammingWithHarry which has over 50K subscribers and HindiGamingZone which has about 16K subscribers.")
    return render(request,'harry.html')
def shraddha(request):
    #return HttpResponse("Shradha Khapra aka Apna College Girl is a well-known educator, content creator, coding teacher & YouTuber from Haryana, India. She is also known by the name 'Microsoft Wali Didi'.      She is known in the country for being one of the best educators of coding, who left her job at Microsoft to help Indian aspirants to learn to code. She is also the co-founder of Apna College, an online EdTech platform that provides education to JEE and NEET aspirants and student aspirants of coding.")
    return render(request,'shraddha.html')
def codehelp(request):
    #return HttpResponse("Code Help was founded in 2020 by Love Babbar (Ex-Amazon, Ex-Microsoft) to deliver “to the point, short and practical” educational content for learning programming, coding, and preparing for job placements, and interviews. He has been mentoring students through his Youtube channel which has now gained more than 17 million views and is now looking forward to providing his guidance in different courses through Code Help.")
    return render(request,'codehelp.html')
def teachers(request):
    return render(request,'teachers.html')
def index(request):
    return render(request,'index.html')
def courses(request):
    return render(request,'courses.html')
def roadmaps(request):
    return render(request,'roadmaps.html')
def welcome(request):
    return render(request,'welcome.html')
def contact(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        Message=request.POST['Message']
        ins=Contact(fname=fname,lname=lname,email=email,Message=Message)
        ins.save()
        print("data written to db")
    return render(request,'contact.html')

def doubts(request):
    return render(request,'doubts.html')
def signin(request):
    return render(request,'signin.html')
def signup(request):
    if request.method=="POST":
        upemail=request.POST['upemail']
        sname=request.POST['sname']
        password=request.POST['password']
        abc=Sign_up(upemail=upemail,sname=sname,password=password)
        abc.save()
        print("data written")
    return render(request,'signup.html')