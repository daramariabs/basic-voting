#Adicionando a aplicação na inteface de administração
from django.contrib import admin
from .models import Question

admin.site.register(Question)
