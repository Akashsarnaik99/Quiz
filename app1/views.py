from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    quiz ='who is PM of India?'

    options = ['narendra modi', 'rahul gandhi','amit shah','Yogi Adityanath']

    return render(request, 'home.html',{'question':quiz,'option':options})

def result(request):
    if request.method=='POST':
        answer =request.POST.get('selected_items')
        if answer=='narendra modi':
            messages.info( request,'correct answer')
        else:
            messages.info( request,'wrong answer')

        return render(request, 'result.html', {'answer': answer})
    
    return render(request, 'result.html')


def quiz(request):
   
   questions = []
   options=[]

   
   d= {
    'what is the currency of japan?' :['yen','Rupees','Yon','dollar'],
    'what is the capital of India?':['Ahemdabad','Luknow','New Delhi','Agra'],
    'who is first man on moon?':['J Robert', 'Micheal Donald', 'Rajiv Dixit', 'Neil Armstrong'],
    'who is President of India':['Ramnath Kovind','Droupadi Murmu','Pranab Mukherjee', 'Narendra Modi']
    }
   for i in d:
        question=i
        questions.append(question)
   for i in d.values():
        option = i
        options.append(option)

   zipped_data = zip(questions, options)

   context = {
              'zipped_data': zipped_data,
              'count':count,
              }

   return render(request,'quiz.html',context)
    
count=0
def evaluate(request):
    global count
    form_submitted = False

    if request.method == 'POST':
        selected_option1 = request.POST.get('response_1')
        if selected_option1=='yen':
             count+=1
        selected_option2 = request.POST.get('response_2')
        if selected_option2=='New Delhi':
            count+=1
        selected_option3 = request.POST.get('response_3')
        if selected_option3=='Neil Armstrong':
            count+=1
        selected_option4 = request.POST.get('response_4')
        if selected_option4=='Droupadi Murmu':
            count+=1
        form_submitted = True
    total=count
    count=0

    

    return render(request, 'quiz.html',{'count':total,'form_submitted':form_submitted})


def result2(request):
    count=0
    if request.method =='POST':
        options =['yen','New Delhi','Neil Armstrong','Droupadi Murmu']
        i=1
        for i in range(len(options)):
            selected_option = request.POST.get(f"response_{i+1}")
            if selected_option==options[i]:
                count+=1

    total=count
    return render(request, 'result2.html',{'count':total})
