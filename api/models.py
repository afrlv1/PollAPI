from django.db import models


class HeaderModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('created', 'updated')
		abstract = True


class QuestionSet(HeaderModel):
	name = models.CharField(max_length=50)
	owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='questionSet')

	class Meta(HeaderModel.Meta):
		unique_together = ('name', 'owner')

	def __str__(self):
		return self.name


class Question(HeaderModel):
	question_text = models.TextField()
	set = models.ForeignKey('QuestionSet', on_delete=models.CASCADE, related_name='question')

	def __str__(self):
		return self.question_text


class Choice(HeaderModel):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
	choice_text = models.TextField()
	votes = models.PositiveIntegerField(default=0)
	users = models.ManyToManyField('auth.User', related_name='choiceVoted')
	CHOICE_TYPE = (
		('1', 'Ответ текстом'),
		('2', 'ответ с выбором одного варианта'),
		('3', 'ответ с выбором нескольких вариантов'),
	)
	TypeOfChoice = models.CharField(max_length=1, choices=CHOICE_TYPE, default='1',)

	def __str__(self):
		return self.choice_text


class Room(HeaderModel):
	name = models.CharField(max_length=50)
	description = models.TextField()
	owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='roomOwner')
	users = models.ManyToManyField('auth.User', related_name='roomUser', blank=True)
	question_set = models.ForeignKey('QuestionSet', on_delete=models.CASCADE, related_name='room')
	destroyed = models.BooleanField(default=False)
	public = models.BooleanField(blank=False)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)

	def __str__(self):
		return self.name
