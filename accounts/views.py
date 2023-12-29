from django.shortcuts import render

# Create your views here.
from djoser.views import UserViewSet

from rest_framework.response import Response
 
class ActivateUser(UserViewSet):
  
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
 
        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
 
        return serializer_class(*args, **kwargs)
 
    def activation(self, request, uid, token, *args, **kwargs):
        template_name = "html/activation_message.html"
        response = super().activation(request, *args, **kwargs)
     
        if response.status_code == 204:
            # Utilisez le modèle d'email d'activation fourni par Djoser
          return render(request, template_name, {})
        
        else:
            # En cas d'échec, retournez la réponse de Djoser telle quelle
            return response