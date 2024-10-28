from django.shortcuts import render, redirect
from videoStoreApp.forms import VideoForm
from videoStoreApp.models import VideoLoader
from rest_framework import generics
from .models import VideoLoader
from .serializers import VideoLoaderSerializer


def upload_video(request):
    form = VideoForm()
    message = ""
    if request.method=="POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "video uploaded !"
            return redirect('get_videos')
    return render(request, 'videoStoreApp/upload_video.html', {'message':message,'form':form})


def get_videos(request):
    videos = VideoLoader.objects.all()
    return render(request, 'videoStoreApp/get_videos.html', {'videos':videos})

def modify_video(request,id):
    video = VideoLoader.objects.get(id=id)
    form = VideoForm(instance=video)
    message=""
    if request.method=="POST":
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            video.delete()
            form.save()
            message = "video modified"
            return redirect('get_videos')

    return render(request, 'videoStoreApp/modify_video.html', {'message':message,'form':form})

def delete_video(request,id):
    video = VideoLoader.objects.get(id=id)
    video.delete()
    return redirect('get_videos')

def clear_box_videos(request):
    videos = VideoLoader.objects.all()
    videos.delete()
    return redirect('get_videos')


class VideoLoaderListCreateView(generics.ListCreateAPIView):
    queryset = VideoLoader.objects.all()
    serializer_class = VideoLoaderSerializer

class VideoLoaderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoLoader.objects.all()
    serializer_class = VideoLoaderSerializer