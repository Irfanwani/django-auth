from django.contrib import admin
from .models import Emails, PasswordCodes, SignUpCodes

admin.site.register(Emails)
admin.site.register(SignUpCodes)
admin.site.register(PasswordCodes)