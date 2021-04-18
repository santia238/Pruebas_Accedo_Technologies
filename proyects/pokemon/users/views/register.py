from django.shortcuts       import redirect
from django.http            import HttpResponse
from django.views           import View
from django.template.loader import get_template


class View(View):

  def get(self, request, *args, **kwargs):

    template = get_template('register.html')

    ctx = { }

    return HttpResponse(template.render(context=ctx, request=request))
  
  def post(self, request, *args, **kwargs):

    from django.contrib.auth import authenticate, get_user_model, login
    from django.contrib import messages

    User = get_user_model()

    name      = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email     = request.POST.get('email')
    password  = request.POST.get('password')

    if email and password:
      if User.objects.filter(username=email).count() != 0:
        messages.success(request, "El usuario ya se encuentra registrado, ingresa un correo electrónico diferente")
      else:
        user = User(
          username   = email,
          first_name = name,
          last_name  = last_name,
          email      = email
        )
        user.set_password(password)
        user.save()
        user = authenticate(username=email, password=password)
        login(request,user)
        return redirect('details')

    template = get_template('register.html')

    ctx = { }

    return HttpResponse(template.render(context=ctx, request=request))