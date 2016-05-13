from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^colores/$',
		views.ColorListView.as_view(),
		name="color_list"),

	url(r'^colores/(?P<pk>\d+)/$',
		views.ColorDetailView.as_view(),
		name="color_detail"),

	url(r'^colores/crear/$',
		views.ColorCreateView.as_view(),
		name="color_crear"),
]