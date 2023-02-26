from rest_framework import serializers

from students.models import Comment, Major, Region, Student


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    major = serializers.PrimaryKeyRelatedField(queryset=Major.objects.all())
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())

    class Meta:
        model = Student
        fields = "__all__"
        depth = 1

    def validate(self, attrs):
        super().validate(attrs)
        errors = {}
        required = {
            'discount': ('percent', 'discount_from', 'discount_to'),
            'super_contract': ('super_contract_sum', )
        }
        for required_flag, required_fields in required.items():
            if required_flag in attrs and attrs[required_flag] == True:
                for field in required_fields:
                    if field not in attrs or attrs[field] == None:
                        errors.update(
                            {field: f'You must fill in the field {field}'})

        if len(errors) != 0:
            raise serializers.ValidationError(errors)
        return attrs


class StudentStatisticsSerializer(serializers.Serializer):
    all_students = serializers.IntegerField()
    approved_students = serializers.IntegerField()
    recently_added = serializers.IntegerField()
    male = serializers.IntegerField()
    female = serializers.IntegerField()
