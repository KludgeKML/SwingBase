from django.db import models

class PersonVocab (models.Model):
	name = models.CharField()
	pronoun = models.CharField()
	pronoun_obj = models.CharField()
	possessive = models.CharField()
	possessive_pronoun = models.CharField()

class Position (models.Model):
	name = models.CharField()
	description = models.CharField()
	
class Move (models.Model):
	defaultName = models.CharField()
	beats = models.IntegerField(default=8)
	startPosition = models.foreignKey(Position)
	endPosition = models.foreignKey(Position)
	
class MoveSection (models.Model):
	move = models.ForeignKey(Move)
	beats = models.IntegerField(default=2)
	timing = models.CharField()
	description = models.CharField()
	
class MoveNames (models.Model):
	move = models.ForeignKey(Move)
	name = models.CharField()