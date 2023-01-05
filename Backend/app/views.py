from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.views import View
from django.core import serializers

from models_db.Video_model import Video
from models_db.Origen_Video_model import Origen_Video
from models_db.Estados_Video_model import Estado_Video

class Home( View ):

	def get( self , request ):
		return render( request , 'home.html')

class Api_Videos_User( View ):

	def get( self , request ):
		request_data = request.GET.dict()
		
		all_videos_user = Video.objects.filter( id_user=2 ).select_related("id_origen","id_estado")
		all_videos_user = all_videos_user[int(request_data["limite_inferior"]):int(request_data["limite_superior"])]
		
		#--Serializador -->>
		videos_user = []
		for video in all_videos_user:
			videos_user.append( {
				"titulo": video.titulo , "direccion": video.direccion,
				"cantidad_reproducciones":video.cantidad_reproducciones,
				"fecha_ingreso":video.fecha_ingreso,
				"Origen_Video":{
								"nombre":video.id_origen.nombre ,
								"estructura_html":video.id_origen.estructura_html
								},
				"Estado_Video":{"nombre":video.id_estado.nombre}
			} )
		#----------------->>

		return JsonResponse( {"videos_user": videos_user } )
	
class Api_Top_Videos( View ):

	def get( self , request ):
		request_data = request.GET.dict()

		all_videos_public_users = Video.objects.filter( id_estado__nombre = "Publico" ).select_related("id_origen","id_estado").order_by('-cantidad_reproducciones')
		all_videos_public_users = all_videos_public_users[int(request_data["limite_inferior"]):int(request_data["limite_superior"])]
		
		#--Serializador -->>
		top_videos = []
		for video_public in all_videos_public_users:
			if len(top_videos) == 0:
				video_public.cantidad_reproducciones +=1
				video_public.save()
			top_videos.append( {
				"titulo": video_public.titulo , "direccion": video_public.direccion,
				"cantidad_reproducciones":video_public.cantidad_reproducciones,
				"fecha_ingreso":video_public.fecha_ingreso,
				"Origen_Video":{
								"nombre":video_public.id_origen.nombre ,
								"estructura_html":video_public.id_origen.estructura_html
								},
				"Estado_Video":{"nombre":video_public.id_estado.nombre}
			} )
		#----------------->>

		return JsonResponse( {"top_videos": top_videos } )