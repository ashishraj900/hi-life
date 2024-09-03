from django.shortcuts import render
from members.models import UserDetails
from django.http import HttpResponse


# Create your views here.


def home_view(request):

    return render(request, "index/index.html")
def basic_details(request):

    return render(request, "basic_details/input_form.html")


def add_user_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        flat_no = request.POST.get('flat_no')
        user_details = UserDetails(first_name=first_name,
                                   middle_name=middle_name,
                                   last_name=last_name,
                                   flat_no=flat_no)
        user_details.save()
        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")

def get_user_info_flat_basis(request):
    return render(request, "fetch_data/user_details.html")
def get_user_info(request):
    if request.method == "GET":
        flat_no = request.GET.get('flat_no')
        user_details = UserDetails.objects.filter(flat_no=flat_no).values()
        return HttpResponse(user_details)
