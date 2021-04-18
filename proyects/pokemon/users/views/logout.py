from django.views        import View
from django.contrib.auth import logout
from django.shortcuts    import redirect

class View(View):
  def get(self, request, *args, **kwargs):
    logout(request)
    return redirect('home')


