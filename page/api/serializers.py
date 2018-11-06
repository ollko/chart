from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
    )

from page.models import Mileage

class MileageSerializer(ModelSerializer):
    revenue = SerializerMethodField()
    loko_rate = SerializerMethodField()
    filial = SerializerMethodField()
    loko = SerializerMethodField()

    class Meta:
        model = Mileage
        fields = ('filial','loko', 'year', 'mileage', 'loko_rate', 'revenue')
       

    def get_filial(self, obj):
        return obj.filial.slug

    def get_loko(self, obj):
        return obj.loko.slug

    def get_revenue(self, obj):
        return obj.mileage * obj.loko.rate

    def get_loko_rate(self, obj):
        return obj.loko.rate