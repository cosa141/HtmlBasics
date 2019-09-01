from django.contrib import admin
from first_app.models import Topic,Webpage,AccessRecord
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

# Python manage.py migrate
# Python manage.py makemigrations first_app
# Python manage.py migrate
# Python manage.py createsuperuser
# Python manage.py runserver

#to get to the admin just include /admin on browser
