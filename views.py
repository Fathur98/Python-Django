from django.shortcuts import render, redirect  
from Djangoku.forms import KaryawanForm  
from Djangoku.models import Karyawan
# Create your views here.
def index(request):  
    employees = Karyawan.objects.all()  
    return render(request,"show.html",{'employees':employees}) 

def addnew(request):  
    if request.method == "POST":  
        form = KaryawanForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = KaryawanForm()  
        return render(request,'add.html',{'form':form})

def update(request, id):  
    employee = Karyawan.objects.get(id=id)  
    form = KaryawanForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
        return render(request, 'edit.html', {'employee': employee})
    else:  
        employee = Karyawan.objects.get(id=id)  
        return render(request,'edit.html', {'employee':employee})
    
def delete(request, id):  
    employee = Karyawan.objects.get(id=id)  
    employee.delete()  
    return redirect("/")  