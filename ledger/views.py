from django.shortcuts import render, redirect
from .models import Staff,Transaction
from django.contrib import messages
# Create your views here.
def all_staff(request):
    staff = Staff.objects.filter(trash=False)
    context = {'staff': staff}
    return render(request, 'all_staff.html', context)

def staff_transactions(request):
    staff=Staff.objects.get(id=request.GET['staff_id'])
    transactions=Transaction.objects.filter(staff=staff).order_by('-id')
    return render(request,'staff_transactions.html',{'staff':staff,'transactions':transactions})

def save_transaction(request):
    staff=Staff.objects.get(id=request.GET['staff_id'])
    main_ac=Staff.objects.get(id=1)
    bill_no=request.POST['bill_no']
    date=request.POST['date']
    amount=int(request.POST['amount'])
    transaction=request.POST['transaction']
    remark=request.POST['remark']
    if transaction=='advance':
        if staff.id!=1:
            trans=Transaction(staff=staff,bill_no='-',date=date,advance=amount, balance=staff.balance+amount,grand_balance=main_ac.balance-amount,remark=remark)
        else:
            trans=Transaction(staff=staff,bill_no='-',date=date,advance=amount, balance=staff.balance+amount,grand_balance=main_ac.balance+amount,remark=remark)
        staff.balance=staff.balance+amount
        main_ac.balance=main_ac.balance-amount
    else:
        trans=Transaction(staff=staff,bill_no=bill_no,date=date,bill_amount=amount, balance=staff.balance-amount,grand_balance=main_ac.balance,remark=remark)
        staff.balance=staff.balance-amount
    trans.save()
    staff.save()
    if staff.id != 1:
        main_ac.save()
    messages.success(request,'Transaction added')
    return redirect(f'/ledger/staff_transactions?staff_id={staff.id}')
    

def all_transactions(request):
    transactions=Transaction.objects.filter(advance__gt=0).select_related('staff').order_by('-id')
    return render(request,'all_transactions.html',{'transactions':transactions})
