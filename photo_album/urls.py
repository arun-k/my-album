from django.conf.urls import patterns, include, url
from album import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',(r'^$',views.userlogin),(r'^register/$',views.register),(r'^album/',views.img_list),(r'^logout/$',views.usrlogout),
    # Examples:
    # url(r'^$', 'photo_album.views.home', name='home'),
    # url(r'^photo_album/', include('photo_album.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
