from django.contrib import admin

from .Origen_Video_model import Origen_Video
from .Video_model import Video
from .Estados_Video_model import Estado_Video

@admin.register( Origen_Video )
class Origen_VideoAdmin(admin.ModelAdmin):
	list_display = ( "id" ,"nombre", "estructura_html")


@admin.register( Estado_Video )
class Estado_VideoAdmin(admin.ModelAdmin):
	list_display = ( "id","nombre", )


@admin.register( Video )
class VideoAdmin(admin.ModelAdmin):
	list_display = ( 'id','id_user','titulo','direccion','id_origen','id_estado','cantidad_reproducciones' , 'fecha_ingreso' )
	fields = ( 'id_user','titulo','direccion','id_origen','id_estado' )
	
	def get_form( self , request , obj=None, **kwargs ):
		form = super( VideoAdmin , self ).get_form(request, obj, **kwargs)
		form.id_user = request.user
		return form