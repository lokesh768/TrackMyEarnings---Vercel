from django.shortcuts import render, redirect
from src.models import Borrower,Farmer, Crop, SavingExpense, Networth
from datetime import datetime
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
def Home(request):
    return render(request,'homepage.html')

def Register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # checking password and confirm_password field
        if password != confirm_password :
            messages.warning(request,"Both Passwords must match")
            return redirect('/register/')

        # checking username is already  registered or not 
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username Already taken")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )

        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Succesfully")
        
        return redirect('/login/')
        

    return render(request,'register.html')

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Username Doesn't Exists! (or) Enter Correct Username")
            return redirect('/login/')

        # authentication - checking credentials
        user = authenticate(username=username,password=password)
        if user is None :
            messages.warning(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def Logout(request):
    user = (request.user.first_name +" " + request.user.last_name) if request.user.is_authenticated else 'Guest'
    logout(request)
    return render(request,'logout.html',{'user':user})

@login_required(login_url="/login/")
def InterestFromLendingMoney(request):
    if request.method=="POST":
        if 'save-borrower-details' in request.POST:
            borrower_name = request.POST.get('borrower_name')
            amount_lent = float(request.POST.get('amount_lent'))
            date_lent = request.POST.get('date_lent')
            interest = float(request.POST.get('interest'))
            
            # calcualting simple interest
            lent_date = datetime.strptime(date_lent, '%Y-%m-%d')
            current_date = datetime.now()
            num_months = (current_date.year - lent_date.year) * 12 + (current_date.month - lent_date.month)
            simple_interest = (amount_lent * interest * num_months) / 100
            total_amount_to_be_paid = amount_lent + simple_interest

            Borrower.objects.create(
                user = request.user,
                borrower_name=borrower_name,
                amount_lent=amount_lent,
                date_lent=date_lent,
                interest=interest,
                total_amount_to_be_paid = total_amount_to_be_paid,
            ).save()

            messages.success(request,"borrower Added Successfully")

            return redirect('/interest-from-lending-money/')
        
        if 'update-borrower-details' in request.POST:
            borrower_name = request.POST.get('borrower_name')
            interest_paid = Decimal(request.POST.get('interest_paid'))
            date_paid = request.POST.get('date_paid')
            principal_paid = request.POST.get('principal_paid')
        
            try:
                borrower = Borrower.objects.get(user=request.user,borrower_name=borrower_name)
            except:
                messages.warning(request,"enter correct name")
                return redirect('/interest-from-lending-money/') 
        
            # Subtract interest paid from total amount to be paid
            borrower.total_amount_to_be_paid -= interest_paid
            borrower.date_lent = date_paid
            # Check if principal is paid, and subtract principal as well
            if principal_paid == 'on ':  # Assuming the checkbox sends 'True' as a string
                borrower.total_amount_to_be_paid -= borrower.amount_lent  # Subtract principal

            # Save updated borrower object
            borrower.save()

            messages.success(request,"Details Updated Successfully")

            return redirect('/interest-from-lending-money/')
    borrowers = Borrower.objects.filter(user=request.user)
    return render(request,'interestfromlendingmoney.html',{'borrowers':borrowers})

@login_required(login_url="/login/")
def Business(request):
    if request.method == "POST":
        farmer_name = request.POST.get('farmer_name')
        farmer_cost = int(request.POST.get('farmer_cost'))
        labour_expenses = int(request.POST.get('labour_expenses'))
        vehicle_expenses = int(request.POST.get('vehicle_expenses'))
        other_expenses = int(request.POST.get('other_expenses'))
        patti = int(request.POST.get('patti'))
        total_profit_or_loss = patti - farmer_cost - (labour_expenses//2) - vehicle_expenses - other_expenses
        Farmer.objects.create(
            user = request.user,
            farmer_name = farmer_name,
            farmer_cost = farmer_cost,
            labour_expenses = labour_expenses,
            vehicle_expenses = vehicle_expenses,
            other_expenses = other_expenses,
            patti = patti,
            total_profit_or_loss = total_profit_or_loss
        ).save()

        messages.success(request,"Farmer Added Successfully")

        return redirect('/business/')
    records = Farmer.objects.filter(user=request.user)
    return render(request,'business.html',{'records':records})

@login_required(login_url="/login/")
def Agriculture(request):
    
    if request.method == "POST":
        if 'add_new' in request.POST:
            crop_name = request.POST.get('crop_name')
            investment = int(request.POST.get('investment'))
            pesticides_expenses = int(request.POST.get('pesticides_expenses'))
            labour_expenses = int(request.POST.get('labour_expenses'))
            other_expenses = int(request.POST.get('other_expenses'))

            present_profit_or_loss = 0 - investment - pesticides_expenses - labour_expenses - other_expenses

            Crop.objects.create(
                user = request.user,
                crop_name=crop_name,
                investment=investment,
                pesticides_expenses=pesticides_expenses,
                labour_expenses=labour_expenses,
                other_expenses=other_expenses,
                income = 0,
                present_profit_or_loss=present_profit_or_loss,
            ).save()

            messages.success(request,'Crop Details Added Successfully')
            return redirect('/agriculture/')

        if 'update' in request.POST:
            crop_name = request.POST.get('crop_name')
            investment = int(request.POST.get('investment'))
            pesticides_expenses = int(request.POST.get('pesticides_expenses'))
            labour_expenses = int(request.POST.get('labour_expenses'))
            other_expenses = int(request.POST.get('other_expenses'))
            income = int(request.POST.get('income'))

            try:
                crop = Crop.objects.get(user=request.user,crop_name=crop_name)
            except:
                messages.warning(request,"enter correct crop name")
                return redirect('/agriculture/') 
            
            crop.investment += investment
            crop.pesticides_expenses += pesticides_expenses
            crop.labour_expenses += labour_expenses
            crop.other_expenses += other_expenses
            crop.present_profit_or_loss = crop.present_profit_or_loss + income - investment - pesticides_expenses - labour_expenses - other_expenses

            crop.save() 

            messages.success(request,"Crop Details Updated Successfully")

            return redirect('/agriculture/')
        
    records = Crop.objects.filter(user=request.user)
            
    return render(request,'agriculture.html',{'records':records})


@login_required(login_url="/login/")
def SavingsAndExpense(request):
    if request.method == "POST":
        type = request.POST.get('type')
        purpose = request.POST.get('purpose')
        amount =int(request.POST.get('amount'))

        SavingExpense.objects.create(
            user=request.user,
            type=type,
            purpose=purpose,
            amount=amount,
        ).save()

        messages.success(request,f"{type} added successfully")

        try:
            networth = Networth.objects.get(user=request.user)
        except:
            networth = Networth.objects.create(
                user=request.user,
                total_savings = 0,
                total_expenses = 0,
                net_worth=0,
            ).save()

        if type == "Saving" :
            networth.total_savings += amount
            networth.net_worth += amount
        if type == "Expense" :
            networth.total_expenses += amount
            networth.net_worth -= amount

        networth.save()

        print(networth.net_worth)
        return redirect('/saving-expense/')

    records = SavingExpense.objects.filter(user=request.user)
    try:
        networth = Networth.objects.get(user=request.user)
    except:
        networth = Networth.objects.create(
                user=request.user,
                total_savings = 0,
                total_expenses = 0,
                net_worth=0,
            ).save()
            

    return render(request,'savingexpense.html',{'records':records,'networth':networth})