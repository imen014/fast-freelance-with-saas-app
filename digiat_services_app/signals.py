from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction, Notification, Offre
from .transaction_management import paye_service, update_badge_and_medaille
from django.db import transaction
import logging

@receiver(post_save, sender=Transaction)
def update_freelancer_badge_and_medaille(sender, instance, created, **kwargs):
    if created:
        # Récupérer le vendeur et l'acheteur
        buyer = instance.buyer
        seller = instance.seller

        # Mettre à jour le badge et la médaille du buyer
        update_badge_and_medaille(buyer)
        buyer.save()

        # Mettre à jour le badge et la médaille du seller
        update_badge_and_medaille(seller)
        seller.save()


"""
# Configurez le logger
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Offre)
def check_offer_status(sender, instance, created, **kwargs):
    # Vérifier si l'état de l'offre a changé et que c'est une mise à jour
    if not created and instance.state == "Completed":
        logger.info("L'état de l'offre a changé en 'Completed'. Début du transfert de points.")
        
        # Récupérer les détails du consommateur, fournisseur et du service
        service_consumer = instance.proposer  
        service_provider = instance.offer_receiver
        service = instance.service_in_negociation

        # Utilisation d'une transaction atomique pour garantir le bon déroulement du transfert
        with transaction.atomic():
            try:
                logger.info("Appel de la fonction paye_service.")
                paye_service(service_consumer, service_provider, service)
                logger.info("Transfert de points effectué avec succès.")
            except Exception as e:
                logger.error(f"Erreur lors du transfert des points : {e}")
"""