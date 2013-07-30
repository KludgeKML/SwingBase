from django.contrib import admin
from movestore.models import PersonVocab
from movestore.models import VocabPair
from movestore.models import Position
from movestore.models import Move
from movestore.models import MoveSection
from movestore.models import MoveName

admin.site.register(PersonVocab)
admin.site.register(VocabPair)
admin.site.register(Position)
admin.site.register(Move)
admin.site.register(MoveSection)
admin.site.register(MoveName)
