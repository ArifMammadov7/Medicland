from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register(Setting)
admin.site.register(CarouselItem)
admin.site.register(Testimonial)
admin.site.register(About)
admin.site.register(Subscriber)



@admin.register(Service)  
class MediclandAdmin(admin.ModelAdmin):
    list_display=['title','like','dislike','view','created_at','updated_at']
    search_fields=['title','content']
    list_filter=['created_at','updated_at']

    ordering=['-created_at']
    readonly_fields=('like','dislike','view','created_at','updated_at')


admin.site.site_header="Medicland Admin"
admin.site.site_title="Medicland Admin Portal"

