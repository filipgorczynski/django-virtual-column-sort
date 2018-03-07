from django.db.models import CharField, Case, Value, When
from django.shortcuts import render
from rest_framework import viewsets

from .models import CaseWhen
from .serializers import CaseWhenSerializer


class CaseWhenViewSet(viewsets.ModelViewSet):
    queryset = CaseWhen.objects.all()
    serializer_class = CaseWhenSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.query_params.get('q', 'beer')

        queryset = queryset.annotate(
            exact=Case(
                When(
                    name__iexact=query,
                    then=Value('1')
                ),
                When(
                    name__istartswith=query,
                    then=Value('2')
                ),
                When(
                    name__iendswith=query,
                    then=Value('3')
                ),
                When(
                    name__icontains=query,
                    then=Value('4')
                ),
                default=Value('5'),
                output_field=CharField(),
            )
        ).order_by('exact', 'name')

        print(queryset.query)

        return queryset
