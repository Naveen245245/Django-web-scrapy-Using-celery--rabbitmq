from rest_framework import serializers

from playstore.models import App,Tasks


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
        # exclude = ('watchlist',)

class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"