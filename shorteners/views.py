from django.shortcuts import render, redirect
from django.views import View
from common.mixins import MyLoginRequiredMixin
from tiny_url.settings import ROOT_URL
from .models import Url
from .forms import UrlForm
from .tools.shortener import shorten, get_url_by_code


class UrlView(MyLoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        urls = Url.objects.filter(creator=request.user).order_by('-id').all()
        # reverse urls
        for url in urls:
            url.long_url = url.long_url[::-1]
            url.short_url = url.short_url[::-1]
        return render(request, 'shorteners/url_list.html', {'form': form, 'urls': urls})

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if form.is_valid():
            short_url = shorten(ROOT_URL)
            form.instance.creator = request.user
            form.instance.short_url = short_url
            form.instance.long_url = form.instance.long_url[::-1]
            form.save_unique()
        return redirect('url-list')


class VisitUrlView(View):
    def get(self, request, code, *args, **kwargs):
        short_url = get_url_by_code(code)
        url = Url.objects.filter(short_url=short_url[::-1]).first()
        return redirect(url.long_url[::-1])


