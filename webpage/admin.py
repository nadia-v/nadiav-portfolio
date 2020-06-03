from django.contrib import admin
from .models import Project
from .models import Detail
from .models import Comment
# from .models import Technology
from .models import Picture

# Register your models here
admin.site.register(Project)
admin.site.register(Detail)
admin.site.register(Comment)
# admin.site.register(Technology)
admin.site.register(Picture)