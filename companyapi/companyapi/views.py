from django.http import HttpResponse,JsonResponse
def home_page(request):
    print("HOME PAGE REQUEST")
    friends=["sakshi","mayura","arpita"]
    return JsonResponse(friends,safe=False)