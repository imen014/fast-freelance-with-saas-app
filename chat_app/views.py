from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
#from fallahin_freelance_app.models import Freelancer
from chat_app.models import Message, Answer
from chat_app.forms import MessengerForm, Answer_message, Create_a_new_message
from django.contrib.auth.decorators import login_required


def create_message(request):
    message_form = MessengerForm()
    new_message = Message()
    message = ""
    if request.method == "POST":
        message_form = MessengerForm(request.POST)
        if message_form.is_valid():
            new_message.sender = request.user
            new_message.receiver = message_form.cleaned_data['receiver']
            new_message.content = message_form.cleaned_data['content']
            new_message.save()
            message = "message created"
            return redirect('get_my_message')
    return render(request, 'chat_app/message_created.html', {'message':message,'message_form':message_form})

@login_required
def get_my_message(request):
    message_form = MessengerForm()
    new_message = Message()
    if request.method == "POST":
        message_form = MessengerForm(request.POST)
        if message_form.is_valid():
            new_message.sender = request.user
            new_message.receiver = message_form.cleaned_data['receiver']
            new_message.content = message_form.cleaned_data['content']
            new_message.save()
    messages = Message.objects.filter(Q(receiver=request.user) | Q(sender=request.user))
    answers = Answer.objects.filter(Q(receiver=request.user) | Q(sender=request.user))
    username = request.user.username
    return render(request, 'chat_app/get_my_messages.html', {'message_form':message_form,'messages':messages, 'request.user':request.user,'answers':answers, 'username':username})

@login_required
def answer_message(request):
    answer_form = Answer_message()
    message = ""
    username_sender = ""
    if request.method == "POST":
        answer_form = Answer_message(request.POST)
        if answer_form.is_valid():
            answer = Answer()  # Create a new Answer instance
            answer.content = answer_form.cleaned_data['content']
            answer.sender = request.user
            
            # Get the latest message sent by someone other than the current user
            latest_message = Message.objects.exclude(sender=request.user).order_by('-time').first()
            
            if latest_message is not None:
                username_sender = latest_message.sender.username
                answer.receiver = latest_message.sender  # Set the receiver correctly
            else:
                message = "No messages found to reply to."  # Handle case where no messages exist
                return render(request, 'chat_app/answer.html', {'answer_form': answer_form, 'message': message, 'username_sender': username_sender})

            answer.save()
            message = "Answer sent"
            return redirect('get_my_message')
    return render(request, 'chat_app/answer.html', {'answer_form': answer_form, 'message': message, 'username_sender': username_sender})

def answer_message_from_a_list(request, id):
    message = get_object_or_404(Message, id=id)
    answer_form = Answer_message(instance=message)
    answer = Answer()
    comment = ""
    if request.method == "POST":
        answer_form = Answer_message(request.POST)
        if answer_form.is_valid():
            answer.content = answer_form.cleaned_data['content']
            answer.sender = request.user
            answer.receiver = message.sender
            answer.save()
            comment = "answer sent"
    return render(request, 'chat_app/answer_choosed_message.html', {'answer_form':answer_form, 'comment':comment, 'sender':request.user})

def delete_all_my_messages(request):
    message_sended = Message.objects.filter(sender=request.user)
    message_received = Message.objects.filter(receiver=request.user)
    answer_sended = Answer.objects.filter(sender=request.user)
    answer_received = Answer.objects.filter(receiver=request.user)
    message_sended.delete()
    message_received.delete()
    answer_sended.delete()
    answer_received.delete()
    return redirect('home')

def answer_an_answer_from_a_list(request, id):
    answer = get_object_or_404(Answer, id=id)
    answer_form = Answer_message(instance=answer)
    answer = Answer()
    comment = ""
    if request.method == "POST":
        answer_form = Answer_message(request.POST)
        if answer_form.is_valid():
            answer.content = answer_form.cleaned_data['content']
            answer.sender = request.user
            answer.receiver = answer.sender
            answer.save()
            comment = "answer sent"
    return render(request, 'chat_app/answer_choosed_answer.html', {'answer_form':answer_form, 'comment':comment, 'sender':request.user})
