from django.shortcuts import render,redirect
from deptapp.models import Department

# Create your views here.
def home(request):    
   
    data = Department.objects.filter(status=True)
    print(type(data)) # QuerySet of List containing
    print(data)
    context={}
    context['depts']=data
    return render(request,'index.html',context)

def create(request):
    print(request.method)
    if request.method == 'GET':
      
      return render(request,'createdept.html')
    else:
        #1. capture form data
        n=request.POST['dept_name']
        d=request.POST['description']   
        details = Department.objects.create(dept_name=n,description=d)
        details.save()
        return redirect('/')
    
def updateDept(request,dept_id):
    if request.method == "GET":
        b=Department.objects.filter(dept_id=dept_id)
        context ={}
        context['depts'] = b[0]
        return render(request,'updatedept.html',context)
    else:
        b=Department.objects.filter(dept_id=dept_id)
        n=request.POST['dept_name']
        d=request.POST['description']
       
        b.update(dept_name=n,description=d)
        return redirect('/')    
    
def delete(request,dept_id):
    department = Department.objects.get(dept_id=dept_id)  
    department.status = False
    department.save()   
    return redirect('/')

def searchByText(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    context = {}

    if query:
        # Filter Cloth objects based on the search query (you can adjust fields to match your needs)
        data = Department.objects.filter(dept_name__icontains=query)  # Assuming 'name' is a field in your Cloth model
        context['depts'] = data
    else:
        data=Department.objects.all()
        context['depts'] = data
    return render(request, 'index.html', context)


