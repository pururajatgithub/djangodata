from django.shortcuts import render
from django.http import HttpResponse
from .filters import BankFilter
from .models import Bank
from django.db.models import Q

# Create your views here.


def index(request):
    unique_city = Bank.objects.values('city').distinct().order_by('city')
    
    if 'search' in request.GET:
        q = request.GET.get('search')
        
        data = Bank.objects.filter(Q(bank_name__icontains=q) | Q(bank_id__icontains=q) | Q(ifsc_code=q) | Q(Branch__icontains=q) | Q(city__icontains=q) | 
                                    Q(address__icontains=q) | Q(District__icontains=q) | Q(State__icontains=q))
    
    elif 'city' in request.GET:
        d = request.GET.get('city')
        data = Bank.objects.filter(city__icontains=d)
    elif 'reset' in request.GET:
        data=Bank.objects.all()
    
    else:
        data = Bank.objects.all()
    
    
    return render(request,'index.html', context={'values':data,'cities': unique_city})







