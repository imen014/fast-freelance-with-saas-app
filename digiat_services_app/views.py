from django.shortcuts import render, redirect, get_object_or_404
from .forms import DigitalServiceForm, DigitalServiceImageForm, ChangeServiceStateForm
#from .models import DigitalService, Freelancer
from django.contrib.auth.decorators import login_required
from .manage_youtube_video import extract_youtube_id, is_youtube_video
from .models import DigitalServiceImage, Transaction, Notification, Offre
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .transaction_management import ask_service, paye_service, update_badge_and_medaille
import logging


logger = logging.getLogger(__name__)

@login_required
def create_digital_service(request):
    service_form = DigitalServiceForm()
    message = ""

    if request.method == "POST":
        service_form = DigitalServiceForm(request.POST, request.FILES)
        service_creator = request.user
        service_title = request.POST.get("title")
        service_description = request.POST.get("description")

        # Check if a service with the same title and description already exists
        service = DigitalService.objects.filter(title=service_title, description=service_description).first()
        
        if not service:
            if service_form.is_valid():
                video_url = service_form.cleaned_data.get('video_url')  # Get validated URL from cleaned_data
                
                digital_service = service_form.save(commit=False)  # Do not save yet
                digital_service.user_creator = service_creator  # Associate with the logged-in user
                
                # Check if video_url is provided
                if video_url:
                    # Validate YouTube URL
                    if is_youtube_video(video_url):
                        youtube_id = extract_youtube_id(video_url)  # Extract YouTube ID
                        digital_service.video_url = f"https://www.youtube.com/embed/{youtube_id}"  # Embed URL
                    else:
                        message = "The URL provided is not a valid YouTube video URL."
                        # Do not proceed to save the digital_service if video_url is invalid
                        return render(request, "digiat_services_app/create_digital_service.html", {
                            "message": message,
                            "service": service_form,
                            "form_images": DigitalServiceImageForm()
                        })
                
                # Save the DigitalService instance
                digital_service.save()

                # Handle image uploads if any
                images = request.FILES.getlist('images')  # Assuming you have an input named 'images'
                for image in images:
                    DigitalServiceImage.objects.create(digital_service=digital_service, image=image)

                return redirect("get_my_digital_services")
            else:
                message = "Invalid information!"
        else:
            message = "A service with this title and description already exists."

    return render(request, "digiat_services_app/create_digital_service.html", {
        "message": message,
        "service": service_form,
        "form_images": DigitalServiceImageForm()  # You can directly instantiate it here if needed
    })



def get_all_digital_services(request):
    services = DigitalService.objects.all()
     # Récupérer les services que l'utilisateur a déjà achetés
    user_transactions = Transaction.objects.filter(buyer=request.user)
    bought_services = [transaction.service for transaction in user_transactions]

    return render(request, "digiat_services_app/get_all_digital_services.html", {"services":services,"bought_services":bought_services})


@login_required
def get_my_services(request):
    #services = get_list_or_404(DigitalService, user_creator=request.user)
    services = DigitalService.objects.filter(user_creator=request.user)
    return render(request, "digiat_services_app/get_own_services.html", {"services":services})



@login_required
def delete_digital_service(request, id):
    service = get_object_or_404(DigitalService, id=id)
    service.delete()
    return redirect('home')


def update_digital_service(request,id):
    instance = DigitalService.objects.filter(id=id).first()
    service = DigitalServiceForm(instance=instance)
    if request.method=="POST":
        service = DigitalServiceForm(request.POST, instance=instance)
        if service.is_valid():
            service.save()
            return redirect('get_my_digital_services')
        else:
            message = "Invalid data"
            service = DigitalServiceForm(instance)
    message = ""
    return render(request, "digiat_services_app/update_own_digital_service.html", {"message":message,"service":service})


def get_service_details(request,id):
    service = DigitalService.objects.filter(id=id).first()
    images = DigitalServiceImage.objects.filter(digital_service=service)
    return render(request, "digiat_services_app/get_service_details.html",{"service":service,"images":images})



def get_my_balance(request):
    balance = request.user.balance_pts
    return render(request, 'digiat_services_app/get_my_profile.html', {'balance': balance})


def get_my_buyed_services(request):
    user = request.user
    transactions = Transaction.objects.filter(buyer = user)
    return render(request, "digiat_services_app/dashboard.html", {"transactions":transactions})


def get_my_selled_services(request):
    user = request.user
    selled_services = Transaction.objects.filter(seller = user)
    return render(request, "digiat_services_app/dashboard.html", {"selled_services":selled_services})

def get_notifications(request):
    notifications = Notification.objects.filter(freelancer_id = request.user.id)
    return render(request, "digiat_services_app/get_notifications.html", {"notifications":notifications})


def sended_offres(request):
    user = request.user
    offres = Offre.objects.filter(proposer=user)
    return render(request, "digiat_services_app/sended_offres.html", {"offres":offres})

def received_offres(request):
    user = request.user
    offres = Offre.objects.filter(offer_receiver=user)
    return render(request, "digiat_services_app/received_offres.html", {"offres":offres})

#def get_user_services(request,id):
    #user = Freelancer.objects.filter(id=id).first()
    #services = DigitalService.objects.filter(user_creator=user)
    #return render(request, "digiat_services_app/user_services.html", {"services":services})


