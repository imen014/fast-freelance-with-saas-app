from django.shortcuts import render, redirect, get_object_or_404

from photo_management_app.models import PhotoModel
from photo_management_app.forms import PhotoForm


def upload_photo(request):
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'photo_management_app/photo_upload.html', {'form':form})


def home(request):
    photos = PhotoModel.objects.all()
    return render(request, 'photo_management_app/home.html', {'photos':photos})


def modifier_photo(request, id):
    photo = get_object_or_404(PhotoModel, id=id)
    form = PhotoForm(instance=photo)
    if request.method == "POST":
        form = PhotoForm(request.POST,request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    return render(request, 'photo_management_app/photo_modified.html', {'form':form})
        
    
def delete_photo(request, id):
    photo = get_object_or_404(PhotoModel, id=id)
    photo.delete()
    message = 'image deleted succefully !'
    return render(request, 'photo_management_app/image_deleted.html', {'message':message})
    

