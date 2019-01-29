from django.shortcuts import render



def info(request):
    return render(request, "info.html")
    
def student(request, name):
    stu = {
        '안현상':27,
        '김녹형':27,
        '강민지':28,
    }
    
    age = stu[name]
    return render(request, "student.html", {"name":name, "age":age})
    
    

