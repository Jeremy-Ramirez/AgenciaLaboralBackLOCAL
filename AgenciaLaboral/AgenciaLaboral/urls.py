"""AgenciaLaboral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('applications.Genero.urls')),
    path('api/',include('applications.Tipodocumento.urls')),
    path('api/',include('applications.Provincia.urls')),
    path('api/',include('applications.Ciudad.urls')),
    path('api/',include('applications.Tipopersona.urls')),
    path('api/',include('applications.Actividadeconomica.urls')),
    path('api/',include('applications.Ramaactividad.urls')),
    path('api/',include('applications.Tipoempresa.urls')),
    path('api/',include('applications.Sector.urls')),
    path('api/',include('applications.Empresa.urls')),
    path('api/',include('applications.Representanteempresa.urls')),
    path('api/',include('applications.Usuario.urls')),
    path('api/',include('applications.Solicitud.urls')),
    path('api/',include('applications.Tiposolicitud.urls')),
    path('api/',include('applications.Estado.urls')),
    path('api/',include('applications.Sugerencia.urls')),
    path('api/',include('applications.SugerenciaEmpresa.urls')),
    path('api/',include('applications.Aspirante.urls')),
    path('api/',include('applications.Profesiones.urls')),
    path('api/',include('applications.Estadocivil.urls')),
    path('api/',include('applications.Aspirantessolicitados.urls')),
    path('api/',include('applications.ArchivosAspirante.urls')),
    path('api/',include('applications.CategoriaDocumento.urls')),
    path('api/',include('applications.NivelEstudios.urls')),
    path('', include('home.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)