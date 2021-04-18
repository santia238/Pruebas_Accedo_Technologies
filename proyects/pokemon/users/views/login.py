from django.shortcuts       import redirect
from django.http            import HttpResponse
from django.views           import View
from django.template.loader import get_template


class View(View):

  def get(self, request, *args, **kwargs):

    if request.user != None and not request.user.is_anonymous:
      return redirect('details')

    template = get_template('login.html')

    ctx = {
    }

    return HttpResponse(template.render(context=ctx, request=request))
  
  def post(self, request, *args, **kwargs):
    from django.contrib.auth import authenticate, get_user_model, login
    from django.contrib import messages

    email    = request.POST.get('email')
    password = request.POST.get('password')

    if email and password:
      user = authenticate(username=email, password=password)

      if user is not None:
        login(request,user)
        return redirect('details')
      else:
        messages.success(request, "Correo o contraseña incorrecto, vuelve a intentarlo")

    template = get_template('login.html')

    ctx = { }

    return HttpResponse(template.render(context=ctx, request=request))