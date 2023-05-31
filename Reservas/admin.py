from django.contrib import admin
from Reservas.models import UserExtraInfo, TipoHabitacion, Habitacion, EstadoHabitacion


class UserExtraInfoAdmin(admin.ModelAdmin):
    verbose_name = 'Usuarios Info Extra'
    list_display = ('user',)
    pass

class TipoHabitacionAdmin(admin.ModelAdmin):
    verbose_name = 'Tipos Habitaciones'
    list_display = ('tipo',)
    pass

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero',)
    pass

class EstadoHabitacionAdmin(admin.ModelAdmin):
    list_display = ('estado',)
    pass


admin.site.register(UserExtraInfo, UserExtraInfoAdmin)
admin.site.register(TipoHabitacion, TipoHabitacionAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(EstadoHabitacion, EstadoHabitacionAdmin)