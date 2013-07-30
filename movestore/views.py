from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.safestring import mark_safe

from movestore.models import Move, VocabPair

def index (request):
	moves_list = Move.objects.order_by('-defaultName')
	context = {'moves_list': moves_list}
	return render(request, 'movestore/index.html', context)


def move (request, move_id, vocabpair_id):
	move = get_object_or_404(Move, pk=move_id)      
	vocabpair = get_object_or_404(VocabPair, pk=vocabpair_id)
	move_sections = [];
	for section in move.movesection_set.all():
		move_sections.append(mark_safe(vocabpair.translate(section.description)))
	context = {'move': move, 'move_sections': move_sections }
	return render(request, 'movestore/move.html',context)
