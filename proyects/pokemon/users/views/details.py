from django.shortcuts       import redirect
from django.http            import HttpResponse
from django.views           import View
from django.template.loader import get_template


class View(View):

  def get(self, request, *args, **kwargs):
    if request.user == None or request.user.is_anonymous:
      return redirect('../logout/')

    template = get_template('details.html')

    ctx = {
    }

    return HttpResponse(template.render(context=ctx, request=request))