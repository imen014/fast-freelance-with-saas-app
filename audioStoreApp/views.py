from django.shortcuts import render, redirect
from audioStoreApp.forms import AudioForm
from audioStoreApp.models import AudioStoreSaver
from rest_framework import viewsets
from .models import AudioStoreSaver
from .serializers import AudioStoreSaverSerializer

def create_memory(request):
    form = AudioForm()
    message = ""
    if request.method=="POST":
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "memory created !"
            return redirect('get_memories')
    return render(request, 'audioStoreApp/memory_created.html', {'form':form,'message':message})

def get_memories(request):
    memories = AudioStoreSaver.objects.all()
    return render(request, 'audioStoreApp/get_memories.html', {'memories':memories})

def modify_memory(request, id):
    memory = AudioStoreSaver.objects.get(id=id)
    form = AudioForm(instance=memory)
    if request.method=="POST":
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            memory.delete()
            form.save()
            return redirect('get_memories')
    return render(request, 'audioStoreApp/modify_memory.html', {'form':form})

def delete_memory(request,id):
    memory = AudioStoreSaver.objects.get(id=id)
    memory.delete()
    return redirect('get_memories')


def delete_memories(request):
    memories = AudioStoreSaver.objects.all()
    memories.delete()
    return redirect('get_memories')


class AudioStoreSaverViewSet(viewsets.ModelViewSet):
    queryset = AudioStoreSaver.objects.all()
    serializer_class = AudioStoreSaverSerializer