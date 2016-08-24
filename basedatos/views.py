from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from NDR.settings import MEDIA_ROOT
from basedatos.forms import UploadFileForm


@csrf_exempt
def recibirjson(request):
    context = {}
    """if request.method=='POST':
            test = request.FILES["archivo"]
            data = test.read()
            data2 = json.dumps(data)

            print ("porfinhdp")
    """
    if request.method == 'POST':
        save_file(request.FILES['archivo'])
        return render(request, 'ingreso.html', context)
    else:
        return render(request, '/recibirjson', context)

def save_file(file, path=''):
    filename = file._get_name()
    fd = open('%s/preparacion/encuesta/%s' % (MEDIA_ROOT, str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()