from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.
#############Aaaaaaaa########
# Function based View

def about(request):
    return HttpResponse("About page")

def show(request):
    return HttpResponse(2+2)

def home(request):
    return HttpResponse("Home page")

def courses(request):
    return render(request,"courses.html",{})

def kfc(request):
    return render(request,"kfc.html",{})

def students(request):
    print("**********************")
    print(request.method)
    print("**********************")
    context={"id":None,
            "name":"Nisha",
            "subjects":["Maths","Science","English"]
            }
    return render(request,"students.html",context)

def books(request):
    context={"id":101,
            "name":"how to win",
            "genres":["non-fic","sci-fi","fic","Graphic"]
            }
    return render(request,"books.html",context)

def book1(request):
    print(request.GET.get("bookname"))
    print(request.GET.get("price"))
    context={"bookname":request.GET.get("bookname"),
            "price":request.GET.get("price")}
    return render(request,"book1.html",context)

def product(request):
    print(request.GET.get("productname"))
    print(request.GET.get("price"))
    context={"productname":request.GET.get("productname"),
            "price":request.GET.get("price")}
    return render(request,"product.html",context)

def employee(request):
    if request.method=='GET':
        return render(request,"employee.html")
    if request.method=='POST':
        employeeName=request.POST.get("employeename")
        return render(request,"employee.html",{"empname":employeeName})
    
class MyView(View):

    def get(self,request):
        return render(request,"my_view.html")
    
    def post(self,request):
        return render(request,"success.html")
    
def learnFilters(request):
    return render(request,"template_filters.html",{"data":"Django"})