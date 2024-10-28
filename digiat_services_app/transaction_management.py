from django.contrib import messages
from .models import Transaction, Offre, Notification
from django.db import transaction

#the buyer: celui qui achéte le service
#transfer_points(request, buyer, seller, service)


def ask_service(request,service_consumer, service_provider, service):
        transaction_trace = Transaction()
        transaction_trace.buyer = request.user
        transaction_trace.seller = service.user_creator
        transaction_trace.service = service
        transaction_trace.pts_used = service.pts_enjoy_service
        transaction_trace.save()
        state = "Pending"
        offre = Offre.objects.create(proposer=service_consumer, offer_receiver=service_provider,service_in_negociation=service,state=state)
        offre.save()
        messages.success(request, f'U asked the service {service.title} successfully!')
   


@transaction.atomic()
def paye_service(service_consumer, service_provider, service):
    #MINIMUM_BALANCE_ALLOWED = -100
    #if service_consumer.balance_pts - service.pts_enjoy_service > MINIMUM_BALANCE_ALLOWED:
    """service_consumer.balance_pts -= service.pts_enjoy_service
    service_provider.balance_pts += service.pts_enjoy_service
    service_consumer.save()
    service_provider.save()
     # Mettre à jour les badges et médailles pour le buyer et le seller
    update_badge_and_medaille(service_consumer)
    update_badge_and_medaille(service_provider)"""



def update_badge_and_medaille(freelancer):
    # Logique pour mettre à jour le badge
    if freelancer.balance_pts >= 100 and freelancer.transactions_buyer.count() >= 10:
        freelancer.badge = "competent seller"
        description = "New badge: competent seller"
    elif freelancer.balance_pts >= 10 and freelancer.balance_pts < 100:
        freelancer.badge = "active consumer"
        description = "New badge: active consumer"
    elif freelancer.balance_pts >= 0 and freelancer.balance_pts < 10:
        freelancer.badge = "new joiner Membre"
        description = "New badge: new joiner Membre"
    elif freelancer.balance_pts < 0 and freelancer.balance_pts >= -100:
        freelancer.badge = "In Recovery"
        description = "New badge: In Recovery"
    elif freelancer.balance_pts < -100 and freelancer.balance_pts >= -200:
        freelancer.badge = "At Risk Member"
        description = "New badge: At Risk Member"
    else:
        description = "No change in badge"

    # Logique pour mettre à jour la médaille
    if freelancer.balance_pts >= 5000 or freelancer.transactions_buyer.count() >= 1000:
        freelancer.medaille = "Gold"
        description += ", New Medaille: Gold"
    elif freelancer.balance_pts >= 3000 and freelancer.balance_pts < 5000:
        freelancer.medaille = "Silver"
        description += ", New Medaille: Silver"
    elif freelancer.balance_pts >= 2000 and freelancer.balance_pts < 3000:
        freelancer.medaille = "Bronze"
        description += ", New Medaille: Bronze"
    elif freelancer.balance_pts >= 1000 and freelancer.balance_pts < 2000:
        freelancer.medaille = "Excellence"
        description += ", New Medaille: Excellence"
    else:
        description += ", No change in medaille"

    # Enregistrement de la notification
    Notification.objects.create(description=description, freelancer_id=freelancer.id)  # Assurez-vous que Notification a un champ 'freelancer'



       
