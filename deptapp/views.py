from django.shortcuts import render,redirect
from deptapp.models import Department,Role


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

def role(request):       
    data = Role.objects.filter(status=True)
    print(type(data)) # QuerySet of List containing
    print(data)
    context={}
    context['roles']=data
    return render(request,'roles.html',context)

# def createRole(request):
#     print(request.method)
#     if request.method == 'GET':      
#       return render(request,'createroles.html')
#     else:
#         #1. capture form data
#         n=request.POST.get['role_name']
#         d=request.POST.get['description']   
#         details = Role.objects.create(roles_name=n,description=d)
#         details.save()
#         return redirect('/')


    
def createRole(request):
    print(request.method)
    if request.method == 'GET':      
        return render(request, 'createroles.html')
    else:
        # 1. Capture form data
        n = request.POST.get('role_name')  # Correct usage of .get
        d = request.POST.get('description')  # Correct usage of .get

        # 2. Ensure values are not None (optional validation)
        if n is None or d is None:
            return render(request, 'createroles.html', {'error': 'All fields are required!'})

        # 3. Save the role
        details = Role.objects.create(role_name=n, description=d)
        details.save()

        # 4. Redirect to the homepage or another page
        return redirect('/roles')

def searchByTextRole(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    context = {}

    if query:
        # Filter departments with status=True and matching the search query
        data = Role.objects.filter(role_name__icontains=query, status=True)
    else:
        # Retrieve all departments with status=True if no query is provided
        data = Role.objects.filter(status=True)

    # Check if no results are found
    if not data.exists():
        context['message'] = "Role not found!!!."
    else:
        context['roles'] = data

    return render(request, 'roles.html', context)

def updateRole(request, role_id):
    if request.method == "GET":
        try:
            roles = Role.objects.get(role_id=role_id)
            return render(request, 'updaterole.html', {'role': roles})
        except Role.DoesNotExist:
            return redirect('/roles')  # Redirect if the department is not found

    elif request.method == "POST":
        try:
            roles = Role.objects.get(role_id=role_id)
            roles.role_name = request.POST.get('role_name', roles.role_name)
            roles.description = request.POST.get('description', roles.description)
            roles.save()
            return redirect('/roles')
        except Role.DoesNotExist:
            return redirect('/roles')  # Redirect if the department is not found


def deleteRole(request,role_id):
    roles = Role.objects.get(role_id=role_id)  
    roles.status = False
    roles.save()   
    return redirect('/roles')