from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .models import IceCream, ShavedIce, SnackBar
from .serializers import IceCreamSerializer, ShavedIceSerializer, SnackBarSerializer


class IceCreamModelViewset(viewsets.ModelViewSet):

    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer

class ShavedIceModelViewset(viewsets.ModelViewSet):

    queryset = ShavedIce.objects.all()
    serializer_class = ShavedIceSerializer

class SnackBarModelViewset(viewsets.ModelViewSet):

    queryset = SnackBar.objects.all()
    serializer_class = SnackBarSerializer

class BuyFoodAPIView(views.APIView):

    def get(self, request):
        ice_cream = IceCream.objects.filter(sold=False)
        ice_cream_serializer = IceCreamSerializer(ice_cream, many=True)
        shaved_ice = ShavedIce.objects.filter(sold=False)
        shaved_ice_serializer = ShavedIceSerializer(shaved_ice, many=True)
        snack_bar = SnackBar.objects.filter(sold=False)
        snack_bar_serializer = SnackBarSerializer(snack_bar, many=True)

        data = [{"Ice Creams":ice_cream_serializer.data}, {"Shaved Ice":shaved_ice_serializer.data}, {"Snackbars":snack_bar_serializer.data}]

        return Response({'status_code':status.HTTP_200_OK,'Available Items': data})

    def post(self, request):

        req = request.data
        try:
            for key in request.data:
                for id in req[key]:
                    if key == "ice_creams":
                        obj = IceCream.objects.filter(sold=False).get(id=id)
                    elif key == "shaved_ice":
                        obj = ShavedIce.objects.filter(sold=False).get(id=id)
                    elif key == "snackbars":
                        obj = SnackBar.objects.filter(sold=False).get(id=id)
                    obj.sold = True
                    obj.save()
        except:
            return Response({"status_code": status.HTTP_400_BAD_REQUEST, "message": "SORRY!"})

        return Response({"status_code": status.HTTP_200_OK, "message": "ENJOY!"})

class TotalPriceAPIView(views.APIView):

    def get(self, request):

        total = 0
        ice_creams = IceCream.objects.filter(sold=True)
        shaved_ice = IceCream.objects.filter(sold=True)
        snackbars = IceCream.objects.filter(sold=True)

        for ice_cream in ice_creams:
            if ice_cream.sold == True:
                total += ice_cream.price

        for shavedIce in shaved_ice:
            if shavedIce.sold == True:
                total += ice_cream.price

        for snackbar in snackbars:
            if snackbar.sold == True:
                total += ice_cream.price

        ice_cream_all = IceCreamModelViewset.queryset
        ice_cream_serializer = IceCreamSerializer(ice_cream_all, many=True)
        shaved_ice_all = ShavedIceModelViewset.queryset
        shaved_ice_serializer = ShavedIceSerializer(shaved_ice_all, many=True)
        snackbar_all = SnackBarModelViewset.queryset
        snack_bar_serializer = SnackBarSerializer(snackbar_all, many=True)

        inventory = [{"Ice Creams":ice_cream_serializer.data}, {"Shaved Ice":shaved_ice_serializer.data}, {"Snackbars":snack_bar_serializer.data}]

        return Response({"status_code": status.HTTP_200_OK, "Total Amount": total, "Inventory":inventory})