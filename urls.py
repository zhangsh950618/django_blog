from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django_blog.sitemaps import BlogSitemap, IndexSitemap
from django.http import HttpResponse
from apps.blog.views import LatestPosts
from apps.blog.views import BlogListView
from django.views.generic import TemplateView

admin.autodiscover()

sitemaps = {
    'index': IndexSitemap,
    'blog': BlogSitemap,

}

urlpatterns = patterns('',
                       url(r'^about$', TemplateView.as_view(template_name="about.html"), name='about'),
                       url(r'^blog/', include('apps.blog.urls', namespace='blog')),
                       url(r'^$', BlogListView.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'404', TemplateView.as_view(template_name="404.html")),
                       url(r'^rss/', LatestPosts(), name='feeds'),
                       url(r'^baidu_verify_2sFNvhPJ3z.html$', TemplateView.as_view(template_name="baidu_verify_2sFNvhPJ3z.html"), name='baidu_verify'),
                       )
