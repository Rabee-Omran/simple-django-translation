from django.shortcuts import render

# should install 'sudo apt install gettext'
from django.utils import translation  
from django.utils.translation import gettext as _  

# Create your views here.

def index(request):

    #translation
    # user_language = "es"
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language


    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    context = {
        "hello": _("hello")
    }
    return render(request, "index.html", context)