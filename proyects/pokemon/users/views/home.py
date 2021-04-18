from django.shortcuts       import redirect
from django.http            import HttpResponse
from django.views           import View
from django.template.loader import get_template


class View(View):

  def get(self, request, *args, **kwargs):
    template = get_template('home.html')

    ctx = {
    }

    return HttpResponse(template.render(context=ctx, request=request))