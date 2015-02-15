from django.shortcuts import render
from salient.models import Volume, Doc
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import DocSerializer, DocDetailSerializer, VolumeSerializer

class DocAPIView(APIView):
    """
    List all docs.
    """
    def get(self, request, format=None):
        docs = Doc.objects.filter(user=request.user)
        serializer = DocSerializer(docs, many=True)
        return Response(serializer.data)

class DocDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Doc.objects.get(pk=pk)
        except Doc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doc = self.get_object(pk)
        serializer = DocDetailSerializer(doc)
        return Response(serializer.data)

class VolumeAPIView(APIView):
    """
    List all volumes.
    """
    def get(self, request, format=None):
        volumes = Volume.objects.filter(user=request.user)
        serializer = VolumeSerializer(volumes, many=True)
        return Response(serializer.data)
