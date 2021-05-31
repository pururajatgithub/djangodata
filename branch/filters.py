import django_filters



from .models import Bank

class BankFilter(django_filters.FilterSet):
    class Meta:
        model = Bank
        fields = [
                'bank_id', 
                'bank_name',
                'ifsc_code',
                'Branch',
                'city',
                'address',
                'District',
                'State'
                ]


