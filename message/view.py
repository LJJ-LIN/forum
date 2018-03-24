from django.contrib.auth.decorators import login_required
from message.models import UserMessage
from django.shortcuts import render_to_response,redirect

@login_required
def message_list(request):
	read_messages = UserMessage.objects.filter(owner=request.user, status=1).order_by("-id")
	unread_messages = UserMessage.objects.filter(owner=request.user,status=0).order_by("-id")
	return render_to_response("message_list.html",{"read_messages":read_messages,"unread_messages":unread_messages})

def read_message(request,message_id):
	message = UserMessage.objects.get(id=int(message_id))
	message.status = 1
	message.save()
	return redirect(message.link)