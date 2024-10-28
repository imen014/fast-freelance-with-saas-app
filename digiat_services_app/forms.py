from .models import DigitalService, DigitalServiceImage, Offre
from django import forms



class DigitalServiceForm(forms.ModelForm):
    video_url = forms.URLField(required=False)  # Rendre ce champ non requis
    class Meta:
        model = DigitalService
        fields = ["title","description","pts_enjoy_service","is_active","video_url"]


class DigitalServiceImageForm(forms.ModelForm):
    class Meta:
        model = DigitalServiceImage
        fields = ["image"]
    

class ChangeServiceStateForm(forms.ModelForm):

    STATE_CHOICES = [
    ('pending', 'Pending'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('completed', 'Completed'),
]
    state = forms.ChoiceField(choices=STATE_CHOICES)

    class Meta:
        model = Offre
        fields = ["state"]

"""
 service_in_negociation = models.ForeignKey(DigitalService, related_name="service_in_negociation", on_delete=models.CASCADE)
    state = models.CharField(max_length=200)
    proposed_service_in_reverse = models.ForeignKey(DigitalService, related_name="proposed_service_in_reverse", on_delete=models.SET_NULL, null=True, blank=True)  # Modifié ici
"""