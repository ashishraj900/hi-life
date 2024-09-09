from django.shortcuts import render
from members.models import UserDetails
from members.models import EmailID
from members.models import ContactNumber
from members.models import TransactionDetails
from django.http import HttpResponse


# Create your views here.


def home_view(request):

    return render(request, "index/index.html")
def basic_details(request):

    return render(request, "basic_details/input_form.html")

def transaction_details(request):

    return render(request, "transaction_input/transaction_input.html")


def add_user_info(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        flat_no = request.POST.get('flat_no')
        email_id = request.POST.get('email')
        primary_contact_num = request.POST.get('contact_num_1')
        alternate_contact_num = request.POST.get('alternate_num')
        user_details = UserDetails(first_name=first_name,
                                   middle_name=middle_name,
                                   last_name=last_name,
                                   flat_no=flat_no)
        user_details.save()
        user_email = EmailID(flat_no=flat_no,
                             email=email_id)
        user_email.save()
        user_contacts = ContactNumber(flat_no=flat_no,
                                      phone_number=primary_contact_num,
                                      alternate_number=alternate_contact_num)
        user_contacts.save()
        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")

def add_transaction_details(request):
    if request.method == 'POST':
        flat_no = request.POST.get('flat_no')
        purchase_date = request.POST.get('purchase_date')
        sale_agreement_date = request.POST.get('sad')
        sale_deed_date = request.POST.get('sdd')
        sale_agreement_ec_regist = request.POST.get('saecr')
        sales_person = request.POST.get('sapn')
        seller_type = request.POST.get('seller_type')
        flat_transaction = TransactionDetails(flat_no=flat_no,
                                              date_of_purchase=purchase_date,
                                              date_of_sale_agreement=sale_agreement_date,
                                              date_of_sale_deed=sale_deed_date,
                                              date_of_register_sale_agreement=sale_agreement_ec_regist,
                                              seller_name=sales_person,
                                              seller_type=seller_type)
        flat_transaction.save()
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
