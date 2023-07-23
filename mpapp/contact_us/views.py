
# from django.shortcuts import redirect,render,HttpResponse
# from django.views.generic import View
# from django.core.mail import EmailMessage
# from reportlab.pdfgen import canvas
# from io import BytesIO
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch
# from mpapp.settings import EMAIL_HOST_USER
# from .models import Contactinfo


# # Create your views here.


# class Mycontactform(View):
#     def post(self, request):
#         fullname = request.POST['fullname']
#         phone = request.POST['phonenumber']
#         myemail = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         location = request.POST['location']
        
        

#         contact_create = Contactinfo.objects.create(fullname=fullname,phone=phone,
#                                             email=myemail,meg=message,location=location,subject=subject )
#         contact_create.save()
        
   
#         return HttpResponse('sucessfully created')
    
#     def my_view(self):
        
#         return redirect('contact_us/index.html')

    

#     def get(self, request):
#          return render(request, 'contact_us/index.html')

from django.shortcuts import redirect, render, HttpResponse
from django.views.generic import View
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from mpapp.settings import EMAIL_HOST_USER
from .models import Contactinfo

class Mycontactform(View):
    def post(self, request):
        # Retrieve form data from the POST request
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phonenumber')
        myemail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        location = request.POST.get('location')

        # Create a PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        mypdf = p.beginText()
        mypdf.setTextOrigin(inch,inch)
        mypdf.setFont('Helvetica', 14)
        
        createmessage = [
            f"fullname: {fullname}",
            f"Phone: {phone}",
            f"subject: {subject}",
            f"message: {message}",
            f"location: {location}"
        ]
        
        for mywrite in createmessage:
            mypdf.textLine(mywrite)
        p.drawText(mypdf)
        p.showPage()
        p.save()
        
     

        # Send the email with the PDF attachment
        email = EmailMessage(
            'Contact Form Submitted',
            'Thank you for contacting us. We will get back to you shortly.',
            EMAIL_HOST_USER,
            [myemail, 'ugwudavidejeh@gmail.com'],
        )
        email.attach('contactinfo.pdf', buffer.getvalue(), 'application/pdf')
        email.send()

        # Save the form data in the Contactinfo model
        contact_create = Contactinfo.objects.create(
            fullname=fullname,
            phone=phone,
            email=myemail,
            subject=subject,
            meg=message,
            location=location
        )
        contact_create.save()

        return HttpResponse('Successfully created')

    def get(self, request):
        return render(request, 'contact_us/index.html')
