from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.conf import settings

from main.decorators import check_recaptcha
from main.forms import ContactForm
from main.models import Project, MasterClass

def index(request):
    latest_projects = Project.objects.filter(status=1).order_by('-updated_on')
    context = {
        'latest_projects':latest_projects
    }
    return render(request, "main/index.html", context)

def about(request):

    return render(request, "main/about.html")

def clients(request):

    return render(request, "main/clients.html")

class ProjectsView(ListView):
    model = Project
    queryset = Project.objects.filter(status=1).order_by('-updated_on')
    context_object_name = 'projects'
    template_name = 'main/works.html'
    paginate_by = 12

def services(request):

    return render(request, "main/services.html")

def events(request):

    return render(request, "main/services/events.html")

def media(request):

    return render(request, "main/services/media.html")

def travels(request):

    return render(request, "main/services/travels.html")

def printing(request):

    return render(request, "main/services/printing.html")

@check_recaptcha
def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid() and request.recaptcha_is_valid:
            subject = "Webstite Enquiry"
            body = {
            'full_name': 'Name: ' + contact_form.cleaned_data['full_name'],
			'subject': 'Subject: ' + contact_form.cleaned_data['subject'],
            'email_address': 'Email Address: ' + contact_form.cleaned_data['email_address'],
			'message':'Message: ' + contact_form.cleaned_data['message'],
			}
            from_email = contact_form.cleaned_data['email_address']
            message = "\n".join(body.values())
            recipents = ['info@realitiesmedia.org']
            try:
                send_mail(subject, message, from_email, recipents, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, "Thanks, We will get back to you Shortly..")
            return redirect("contact")
        else:
            messages.error(request, "Message was not sent, Please Try Again Later!")
            return redirect("contact")
            
    contact_form = ContactForm()
    site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY
    context = {
        'form': contact_form,
        'site_key': site_key,
    }

    return render(request, "main/contact.html", context)

def masterclass(request):

    item = MasterClass.objects.latest()
    
    context = {
        'item': item,
    }

    return render(request, "main/masterclass.html", context)

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)