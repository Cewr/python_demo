from multiprocessing.dummy import Process
from django.http import JsonResponse
from . models import Chess
from .serializers import Slll
import json

import asyncio
import threading
import websockets


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

    def result(method, rules):
        return rules[method]() if rules.get(method) else {'message': "Request method '{}' does not exist".format(method)}

    return JsonResponse(data=result(method, {
        'GET': get,
        'POST': post
    }))

# -----------------------------

# --------------------------------


ls = []


async def echo(websocket, path):
    # ------
    # async for msg in websocket:
    #     await websocket.send(msg)
    # ----
    ls.append(websocket)

    while True:
        try:
            message = await websocket.recv()
            for item in ls:
                await item.send(message)
        except Exception as e:
            print('e>>>>>', e)
            ls.remove(websocket)
            break
# ---------------------------------------------------------

# asyncio.get_event_loop().run_until_complete(
#     websockets.serve(echo, '127.0.0.1', 5678)
# )
# asyncio.get_event_loop().run_forever()


# --------------------------------------------------------

async def main():
    async with websockets.serve(echo, "127.0.0.1", 5678):
        await asyncio.Future()  # run forever


def abc():
    asyncio.run(main())


if __name__ == "service.views":
    # asyncio.run(main())

    # course = threading.Thread(target=abc)
    # course.start()

    course = Process(target=abc)
    course.start()
