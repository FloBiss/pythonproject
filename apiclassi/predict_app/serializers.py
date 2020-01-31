from rest_framework import serializers
class SubjectSerializer(serializers.Serializer):
	AGE = serializers.IntegerField()
	SPORT = serializers.IntegerField()
	WEIGHT = serializers.IntegerField()
	HEIGHT = serializers.IntegerField()
	label = serializers.FloatField()
	zchest = serializers.FloatField()
	zwrist = serializers.FloatField()
	temp = serializers.FloatField()
	
	activity = serializers.FloatField(allow_null=True)
	
	
	def create(self, validated_data):
		return Subject.objects.create(**validated_data)
	