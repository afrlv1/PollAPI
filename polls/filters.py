"""class RoomFilter(django_filters.rest_framework.FilterSet):
    public = CaseInsensitiveBooleanFilter(name="public", lookup_type='eq')
    destroyed = CaseInsensitiveBooleanFilter(name="destroyed", lookup_type='eq')

    class Meta:
        model = Room
        filter_fields = ['question_set', 'destroyed', 'public']"""