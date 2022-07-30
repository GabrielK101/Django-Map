from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Location
from .serializers import LocationSerializer

@api_view(['GET'])
def getData(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addLocation(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)