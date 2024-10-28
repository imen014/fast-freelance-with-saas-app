from django.db import models
#from fallahin_freelance_app.models import Freelancer
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class DigitalService(models.Model):
    #user_creator = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200)
    pts_enjoy_service = models.IntegerField()
    created_at = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    # u can put URL for online videos
    video_url = models.URLField(max_length=200, blank=True, null=True)  # Champ pour le lien de la vidéo

    def __str__(self):
        return self.title
    


class DigitalServiceImage(models.Model):
    digital_service = models.ForeignKey(DigitalService, on_delete=models.CASCADE, related_name='images') 
    image = models.ImageField(upload_to='digital_service_images/')

    def __str__(self):
        return f"Image for {self.digital_service.title}"

    

@receiver(post_delete, sender=DigitalServiceImage)
def delete_image_files(sender, instance, **kwargs):
    """Supprime le fichier physique de l'image lorsque l'image est supprimée."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class Transaction(models.Model):
    #buyer = models.ForeignKey(Freelancer, related_name="transactions_buyer", on_delete=models.CASCADE)
    #seller = models.ForeignKey(Freelancer, related_name="transactions_seller", on_delete=models.CASCADE)
    service = models.ForeignKey(DigitalService, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    pts_used = models.IntegerField()

    def __str__(self):
        return f"{self.buyer.username} a acheté {self.service.title} de {self.seller.username} pour {self.pts_used} points."

    

class Notification(models.Model):
    description = models.CharField(max_length=200)
    freelancer_id = models.IntegerField()
  
   
class Offre(models.Model):
    #proposer = models.ForeignKey(Freelancer, related_name="offre_proposer", on_delete=models.SET_NULL,null=True,blank=True)
    #offer_receiver = models.ForeignKey(Freelancer, related_name="offre_receiver", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    service_in_negociation = models.ForeignKey(DigitalService, related_name="service_in_negociation", on_delete=models.CASCADE)
    state = models.CharField(max_length=200)
    proposed_service_in_reverse = models.ForeignKey(DigitalService, related_name="proposed_service_in_reverse", on_delete=models.SET_NULL, null=True, blank=True)  # Modifié ici



class AskedService(models.Model):
    service_id = models.IntegerField()
    creator_id = models.IntegerField()
    receiver_id = models.IntegerField()