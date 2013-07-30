from django.http import HttpResponse

from movestore.models import Move

def index (request):
	move_list = Move.objects.order_by('-defaultName')
	output = ', '.join([m.defaultName for m in move_list])
	return HttpResponse(output)


def move (request, move_id):
        
	return HttpResponse('Hello! This is move %s.' % move_id)
