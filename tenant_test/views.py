from django.shortcuts import render
from .models import Tenant
from django.db.models import Q
from django.contrib import messages
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def table(request):
    if request.method=="POST":
        search = request.POST['search']

        if search:
            match = Tenant.objects.filter(Q(name__icontains=search) |
                                          Q(age__icontains=search) |
                                          Q(gender__icontains=search) |
                                          Q(city__icontains=search) |
                                          Q(country__icontains=search)
                                          )
            if match:
                return render(request, 'tenant_test/search.html',{'sr':match})
            else:
                messages.error(request,"no results found")

    return render(request,'tenant_test/search.html')


class IndexView(generic.ListView):
    template_name = 'tenant_test/table.html'
    context_object_name = 'all_tenant'

    def get_queryset(self):
        return Tenant.objects.all()


class TenantCreate(CreateView):
    model = Tenant
    fields = '__all__'
    success_url = reverse_lazy('tenant_test:index')


class TenantUpdate(UpdateView):
    model = Tenant
    fields = '__all__'
    success_url = reverse_lazy('tenant_test:index')


class TenantDelete(DeleteView):
    model = Tenant
    success_url = reverse_lazy('tenant_test:index')