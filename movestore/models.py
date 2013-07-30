from django.db import models

class PersonVocab (models.Model):
	name = models.CharField(max_length=50)
	pronoun = models.CharField(max_length=20)
	pronoun_obj = models.CharField(max_length=20)
	possessive = models.CharField(max_length=20)
	possessive_pronoun = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class VocabPair (models.Model):
	name = models.CharField(max_length=100)
	lead = models.ForeignKey(PersonVocab, related_name='+')
	follow = models.ForeignKey(PersonVocab, related_name='+')

	def translate(self, template):
		tagList = ['L', 'F', 'LPRO', 'FPRO', 'LPROOBJ', 'FPROOBJ', 'LPOS', 'FPOS', 'LPOSPRO', 'FPOSPRO']
		valueList = ['Lead', 'Follow', self.lead.pronoun, self.follow.pronoun, self.lead.pronoun_obj, self.follow.pronoun_obj, self.lead.possessive, self.follow.possessive, self.lead.possessive_pronoun, self.follow.possessive_pronoun]
		for i in range(len(tagList)):
			role = 'lead'
			if (i % 2 == 0):
				role = 'follow'
			template = template.replace('$' + tagList[i] + '$',
				'<span class="person ' + role + '">' + valueList[i] + '</span>')
		return template

	def __unicode__(self):
		return self.name

class Position (models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=2048)

	def __unicode__(self):
		return self.name
	
class Move (models.Model):
	defaultName = models.CharField(max_length=100)
	beats = models.IntegerField(default=8)
	startPosition = models.ForeignKey(Position, related_name='+')
	endPosition = models.ForeignKey(Position, related_name='+')
	
	def __unicode__(self):
		return self.defaultName

class MoveSection (models.Model):
	move = models.ForeignKey(Move)
	beats = models.IntegerField(default=2)
	timing = models.CharField(max_length=20)
	description = models.CharField(max_length=2048)
	
	def __unicode__(self):
		return "Beats " + self.timing + " of " + self.move.defaultName

class MoveName (models.Model):
	move = models.ForeignKey(Move)
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name
