from django.db.models import Count, Max

from rest_framework.views import APIView
from rest_framework.response import Response

from salient.models import Doc

from .utils import stem_word

class DocWordFrequencyAPIView(APIView):

    def get_object(self, pk):
        try:
            return Doc.objects.get(pk=pk)
        except Doc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doc = self.get_object(pk)

        frequencies = doc.worddoc_set \
            .values('word_stemmed') \
            .annotate(freq=Count('word_stemmed')) \
            .order_by('-freq')

        return Response(frequencies)


class DocWordXRayAPIView(APIView):

    def get_object(self, pk):
        try:
            return Doc.objects.get(pk=pk)
        except Doc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        query = request.GET.get('q', None)
        if not query:
            raise Http404

        doc = self.get_object(pk)

        xray = {}

        xray['positions'] = doc.worddoc_set \
            .filter(word_stemmed=stem_word(query)) \
            .order_by('position') \
            .values('word_stemmed', 'word_raw', 'position')
        xray['min_position'] = 0
        xray.update(doc.worddoc_set.aggregate(max_position=Max('position')))

        return Response(xray)
