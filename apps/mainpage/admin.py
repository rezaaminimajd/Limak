from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin
from .models import Information


@admin.register(Information)
class InformationAdmin(ModelAdmin):
    def save_model(self, request, obj, form, change):
        query = Information.objects.all()
        if len(query) == 0:
            super(InformationAdmin, self).save_model(request, obj, form,
                                                     change)
        else:
            storage = messages.get_messages(request)
            for _ in storage:
                pass
            if len(storage._loaded_messages) == 1:
                del storage._loaded_messages[0]
            storage.used = True
            messages.add_message(request, messages.ERROR,
                                 "can not save 2 information")