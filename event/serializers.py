import datetime

from rest_framework import serializers

from event.models import Event, Ticket


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'location', 'date']

    def validate_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError('Событие не может быть в прошлом!')
        return value


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(many=False, queryset=Event.objects.all(), view_name='event-detail')

    class Meta:
        model = Ticket
        fields = ['event', 'price']
