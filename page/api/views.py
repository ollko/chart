from rest_framework.generics import ListAPIView

from django.db.models import Q

from page.models import Mileage
from .serializers import MileageSerializer


class MileageListAPIView(ListAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Mileage.objects.all()

        query_filial = self.request.GET.get('filial')
        if query_filial:
            print('filial=',query_filial)
            f = query_filial.split(',')
            print('f=',f)
            queryset_list = queryset_list.filter(
                filial__slug__in = f
            )
        query_loko = self.request.GET.get('loko')
        if query_loko:
            print('loko=',query_loko)

            l = query_loko.split(',')
            print('l=',l)
            queryset_list = queryset_list.filter(
                loko__slug__in = l
            )
        query_years = self.request.GET.get('years')
        if query_years:
            y = query_years.split(',')
            queryset_list = queryset_list.filter(
                Q(year__gte = y[0]) & 
                Q(year__lte = y[1])
            )
        return queryset_list
