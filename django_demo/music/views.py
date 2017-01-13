from django.http import HttpResponse

# Create your views here.
def index(request):
    s = 0
    for i in range(1,5):
        s += i

    print(s)
    return HttpResponse("<h1> This is the Music app homepage, {}</h1>".format(i))