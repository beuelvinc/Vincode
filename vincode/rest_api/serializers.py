from rest_framework import serializers
from mainApp.models import Vincode,Image

class VincodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vincode
		fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = '__all__'