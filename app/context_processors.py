from .models import *

def common(request):
    a=Student.objs.all()
    return {'a':a}

