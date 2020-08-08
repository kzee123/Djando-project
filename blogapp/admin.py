from django.contrib import admin

# Register your models here.


from .models import reservations, foodorders, feedbacks

admin.site.register(reservations)
admin.site.register(foodorders)
admin.site.register(feedbacks)
