from django.shortcuts import render

# Create your views here.
from app.models import *

def innerEquijoins(request):
    JDED=Emp.objects.select_related('DEPTNO').all()
    JDED=Emp.objects.select_related('DEPTNO').filter(JOB='CLERK')
    
    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)