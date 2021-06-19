from django.db import models
from django.contrib.auth.models import User

class Emails(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	email = models.EmailField()

	def __str__(self):
		return f'New email {self.email} added to the user {self.user}'


class SignUpCodes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.PositiveBigIntegerField()

	def __str__(self):
		return f'{self.code} created for user {self.user}'


class PasswordCodes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	code = models.PositiveBigIntegerField()

	def __str__(self):
		return f'{self.code} created for user {self.user}'