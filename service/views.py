from django.http import JsonResponse
from . models import Chess
from .serializers import Slll
import json


def chess(request):
    method = request.method

    def get():
        res = Slll(Chess.objects.all()[0]).data
        res['list'] = res['list'].split(',')

        return res

    def post():
        body = request.body
        # entry = Chess.objects.all()[0]
        entry = Chess.objects.get(id=1)
        body = json.loads(body)

        for key in body:
            exec("entry.%s = body[key]" % (key))

        # entry.update(**body)
        entry.save()

        return {
            'message': 'success'
        }

    result = {
        'GET': get,
        'POST': post
    }[method]() or {'message': 'error'}
    return JsonResponse(data=result)
