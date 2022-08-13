from django.forms import ModelForm
from django.db import IntegrityError
from .models import Url
from .tools.shortener import shorten
from tiny_url.settings import ROOT_URL

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']

    def save_unique(self, count=10):
        """
        Catch Integrity Error for short_url column and
        keep reassigning new short url until value is saved or count equals to 0
        param: count, amount of time that save-action is limited to operate, default 10
        """
        _saved = False
        _count = count
        while not _saved and _count > 0:
            try:
                self.save()
                _saved = True
            except IntegrityError as e:
                # reassign a short url if current one already exists
                if e.args[0] == 'UNIQUE constraint failed: shorteners_url.short_url':
                    self.instance.short_url = shorten(ROOT_URL)
                    _count -= 1
                else:
                    _count = 0
            except Exception as e:
                # print(e)
                _count = 0





