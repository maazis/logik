from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View


class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)   