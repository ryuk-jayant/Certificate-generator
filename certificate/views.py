from django.shortcuts import render
from django.shortcuts import redirect
from certificate.models import student
from certificate.forms import StudentForm
import pandas as pd
import io
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#converting certificate view to image
from html2image import Html2Image
hti = Html2Image(browser='edge',browser_executable='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',output_path="/screenshots")
# Create your views here.
def home(request):
    student_list=student.objects.all()
    return render(request,"certificate/home.html",{"list":student_list})

def form_view(request):
    if(request.method=="POST"):
        file=(request.FILES['csv_file'])
        if not file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("myapp:upload_csv"))
        # if form.is_valid():
        #     data=form.cleaned_data
        #     print(data)
            # student.objects.create(
            #     author=request.user,
            #     name=data['name'],
            #     email=data['email'],
            # )
        file_data = file.read().decode("utf-8")
        data=pd.read_csv(io.StringIO(file_data))
        data=data.to_dict(orient="records")
        for record in data:
            student.objects.create(
                author=request.user,
                name=record['name'],
                email=record['email'],
            )
        return redirect('Home') 
    form=StudentForm()
    return render(request,"certificate/form.html")
    
def certificate_view(request,pk):
    info=student.objects.get(pk=pk)
    return render(request,"certificate/temp2.html",{"info":info})

def remove_element(request,pk):
    info=student.objects.get(pk=pk)
    print(info)
    info.delete()
    return redirect('Home')

def Mail_cert(request,pk):
    info=student.objects.get(pk=pk)
    subject = f'Hey {info.name},Congrats'
    message = f'Hi,{info.name} thank you for attending our Event in person.'
    html_message = render_to_string('certificate/mail_template.html', {'info': info})
    plain_message = f"Hey{info.name} Congrats on attending our Event.We Congratulate you from depths of our lungs.😂"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [info.email]
    hti.size=(1600,700)
    loc=hti.screenshot(url="http://127.0.0.1:8000/certificate/"+str(pk))
    email = EmailMessage(
    subject,
    plain_message,
    email_from,
    recipient_list,
    [],
    )
    email.attach_file(str(loc[0]))
    email.send(fail_silently=False)
    # print(str(loc[0]))
    #send_mail( subject, plain_message , email_from, recipient_list,html_message=html_message )
    return redirect("Home")