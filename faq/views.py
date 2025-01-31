from rest_framework import viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
  queryset = FAQ.objects.all()
  serializer_class = FAQSerializer

  def list(self, request, *args, **kwargs):
    lang = request.query_params.get('lang', 'en')
    faqs = self.get_queryset()
    data = [
      {
        'question': faq.get_translation(lang)[0],
        'answer': faq.get_translation(lang)[1]
      }
      for faq in faqs
    ]
    return Response(data)

def home(request):
  return HttpResponse("Welcome to the FAQ Management System!")