from rest_framework import generics
from ..models import Color
from .serializers import ColorSerializer

class ColorListView(generics.ListAPIView):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer

class ColorDetailView(generics.RetrieveAPIView):
	queryset = Color.objects.all()
	serializers_class = ColorSerializer


from rest_framework.permissions import IsAdminUser

class ColorCreateView(generics.ListCreateAPIView):
	queryset = Color.objects.all()
	serializer_class = ColorSerializer
	permission_classes = (IsAdminUser,)