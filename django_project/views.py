from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm
from .forms import evenOdd
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contact.models import contactDetails
from django.core.mail import send_mail, EmailMultiAlternatives

def aboutUs(req):
    return HttpResponse("Welcome to the About Page")

def dynamic(req, id):
    return HttpResponse(id)

def homePage(req):
    subject = "Greetings"
    msg1 = "Hello User"
    msg2 = "Hello <b>User</b>"
    from_email = "kolanu.varun.cse22@itbhu.ac.in"
    to = "kolanuvarun739@gmail.com"
    # send_mail(
    #     subject,
    #     msg1,
    #     from_email,
    #     [to],
    #     fail_silently=False
    # )

    message = EmailMultiAlternatives(subject, msg2, from_email, [to])
    message.content_subtype = 'html'
    # message.send()

    # data = {
    #     'title': 'Home Page',
    #     'heading': 'Hello World',
    #     'list': ['PHP', 'Django'],
    #     'student_details': [
    #         {'name':'Varun', 'phone': '123'},
    #         {'name':'Vishwak', 'phone': '456'}
    #     ],
    #     'numbers': [10,20,30,40,50]
    # }
    # return render(req, 'index.html', data)
    # servicesData = Service.objects.all().order_by('service_title')
    newsData = News.objects.all()
    servicesData = Service.objects.all()
    # if req.method == 'GET':
    #     search = req.GET.get('search')
    #     if search:
    #         # servicesData = Service.objects.filter(service_title= search)
    #         servicesData = Service.objects.filter(service_title__icontains= search) #* icontains
    # servicesData = Service.objects.all().order_by('-service_title')  #* Descending order
    # for row in servicesData:
    #     print(row)

    paginator = Paginator(servicesData, 2)
    page_number = req.GET.get('page')
    servicesDataFinal = paginator.get_page(page_number)
    total_pages = servicesDataFinal.paginator.num_pages
    


    data = {
        # 'servicesData': servicesData,
        'servicesData': servicesDataFinal,
        'totalPages': total_pages,
        'range': range(1,total_pages+1),
        'newsData': newsData
    }
    return render(req, 'Tuition.html', data)

def userForm(req):
    sum=0
    fn = usersForm()
    data = {
        'form': fn
    }
    try:
        n1 = req.POST['num1']
        n2 = req.POST.get('num2')
        print(int(n1) + int(n2))
        sum= int(n1) + int(n2)
        return HttpResponseRedirect(f"/about-us?output={sum}")
    except:
        print("error: ")
        return render(req, 'userform.html', data)

# def submitForm(req):
    
#     return render(req, 'userform.html', data)

def calculator(request):
    c = 0
    data = {}
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            # eval: int or float
            opr = request.POST.get('operator')
            if opr == '+':
                c = n1 + n2
            if opr == '-':
                c = n1 - n2
            if opr == '*':
                c = n1 * n2
            if opr == '/':
                c = n1 / n2
            data = {
                'n1': n1,
                'n2': n2,
                'output': c
            }
    except:
        c = 'Invalid calculation'
    return render(request, 'calculator.html', data)

def even_odd(request):
    eo = evenOdd()
    data = {'form': eo, 'error': False}
    try:
        if request.method == 'POST':
            if request.POST.get('num') == "":
                data['error'] = True
                return render(request, 'even_odd.html', data)
            isEven = False
            num = int(request.POST.get('num'))
            if num % 2 == 0:
                isEven = True
            data = {
                'form': eo, 
                'isEven': isEven
            }
        return render(request, 'even_odd.html', data)
    except:
        print("error")
        return render('even_odd.html')
    
def newsDetails(request,slug):
    # newsDetails = News.objects.get(id=id)
    newsDetails = News.objects.get(news_slug=slug)
    data = {
        'newsDetails': newsDetails
    }
    print(id)
    return render(request, 'newsDetails.html', data)

def saveContact(request):
    n=''
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        dataToSave = contactDetails(name=name,email=email,mobile=mobile,message=message)
        dataToSave.save()
        n = 'Your details have been saved'
    return render(request, 'Tuition.html', {'n':n})
