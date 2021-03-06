from django.contrib import admin
from first_app.models import AccessRecord,Webpage,Topic
# Register your models here.
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(AccessRecord)