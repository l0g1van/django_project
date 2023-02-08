from django.urls import reverse
from datetime import datetime
from catalog.models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith(reverse('admin:index')):
            return response
        else:
            Logs.objects.bulk_create([Logs(path=request.path,
                                           method=request.method,
                                           body=request.body,
                                           date_time=datetime.now(),
                                           query=request.META['QUERY_STRING'])])
            # print('path: ', request.path)
            # print('method: ', request.method)
            # print('body: ', request.body)
            # print('date-time: ', datetime.now())
            # print(request.META['QUERY_STRING'])

            return response

