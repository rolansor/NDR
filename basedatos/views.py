from django.shortcuts import render

import json
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def recibirjson(request):
    if request.method=='POST':
            test = request.FILES["testing"]
            data = test.read()
            data2 = json.dumps(data)

            print ("porfinhdp")
    return StreamingHttpResponse('it was GET request')