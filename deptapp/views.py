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
    

def updateDept(request, dept_id):
    if request.method == "GET":
        try:
            department = Department.objects.get(dept_id=dept_id)
            return render(request, 'updatedept.html', {'dept': department})
        except Department.DoesNotExist:
            return redirect('/')  # Redirect if the department is not found

    elif request.method == "POST":
        try:
            department = Department.objects.get(dept_id=dept_id)
            department.dept_name = request.POST.get('dept_name', department.dept_name)
            department.description = request.POST.get('description', department.description)
            department.save()
            return redirect('/')
        except Department.DoesNotExist:
            return redirect('/')  # Redirect if the department is not found

    
def delete(request,dept_id):
    department = Department.objects.get(dept_id=dept_id)  
    department.status = False
    department.save()   
    return redirect('/')


def searchByText(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    context = {}

    if query:
        # Filter departments with status=True and matching the search query
        data = Department.objects.filter(dept_name__icontains=query, status=True)
    else:
        # Retrieve all departments with status=True if no query is provided
        data = Department.objects.filter(status=True)

    # Check if no results are found
    if not data.exists():
        context['message'] = "department not found!!!."
    else:
        context['depts'] = data

    return render(request, 'index.html', context)



