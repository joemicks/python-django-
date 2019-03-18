

from django.http import HttpResponse
from django.db.models import Subquery
from django.shortcuts import render,redirect
from tech.forms import Registration,Loginform
from tech.forms import Regs,UserProfileDetails,project_emp,profit_portal
from tech.models import RegistrationDatas,master,DistrictModel,profit_loss,BloodModel,UserProfileModel,bussiness,project_employee,dontation_portal,profit_account
from passlib.hash import pbkdf2_sha512
from django.shortcuts import get_object_or_404
from django import forms
from passlib.hash import pbkdf2_sha256
from django.core.files.storage import FileSystemStorage
from datetime import datetime


# Current date time in local system


def dashboard11(request):
    return render(request,'account/filenames/homepage.html')
def edit_advance(req):

    return render(req,'account/filenames/dataviewpage.html')

def datatable(req):
    return render(req,'account1/pages/tables/datatable_editadv.html')

def template(req):
    return render(req,'account/filenames/index.html')

def dashboard22(request):
    return render(request,'account/filenames/index2.html')

def login_redirect(request):
    return redirect('/tech/login')

def userprofile_redirect(request):
    return redirect('profile_views')

def profile(request):
    return render(request,'account/filenames/dataviewpage.html')

def index(request):
    a=project_employee.objects.all()
    return render(request,'account/filenames/homepage.html',{'sample':a})
def base(request):
    return render(request,'base.html')
def register(request):
    context={"form":Registration}
    return render(request,"account/regform.html",context)
def register1(request):
    context={"form":Loginform}
    return render(request,"account/login.html",context)



def savefirst(request):

    print("welcome")
    username =  request.POST['username']
    password=  request.POST['password']
    retype= request.POST['retype']
    usertype = request.POST['usertype']
    phone = request.POST['contact']
    file_save = RegistrationDatas(username=username,password=password,retype=retype,usertype=usertype,phone=phone)
    file_save.save()
    return redirect('login_redirect')

def saveuser(request):
    donor = request.POST.get('t1')
    father = request.POST.get('t2')
    mobile = request.POST.get('t3')
    dob = request.POST.get('t4')
    address = request.POST.get('t5')
    district = request.POST.get('t6')
    aadhar = request.POST.get('t7')
    blood = request.POST.get('t8')
    email = request.POST.get('t9')
    company = request.POST.get('t10')
    pancard = request.POST.get('t11')
    gst= request.POST.get('t12')
    designation = request.POST.get('t13')
    bsns=request.POST.get('showform')
    a=request.session['userid']
    filesaving = UserProfileModel(donor=donor,father=father,mobile=mobile,dob=dob,address=address,district=district,aadhar=aadhar,blood=blood,email=email,company=company,pancard=pancard,gst=gst,designation=designation,bs_type=bsns,project_id=a)
    filesaving.save()
    return redirect('District_save')


def profit_type(req):
 type_transaction =req.POST.get('profit1')
 bill_name=req.POST.get('profit3')
 amount=req.POST.get('profit2')
 project_id=req.POST.get('profit4')
 date=req.POST.get('profit5')
 expense_name=req.POST.get('profit6')
 foreign_key=req.POST.get('frg_key')
 profit= profit_account(type_transaction=type_transaction,bill_name=bill_name,amount=amount,project_id=project_id,date=date,expense_name=expense_name,foreign_id=foreign_key)
 profit.save()
 return redirect('project_save')

def project_emps(request):

    title = request.POST.get('p1')
    category = request.POST.get('p2')
    start_date = request.POST.get('p4')
    email = request.POST.get('p8')
    money = request.POST.get('p3')
    descrption = request.POST.get('p5')
    contact = request.POST.get('p6')
    images = request.FILES.get('p7')
    end_date=request.POST.get('p9')
    status=request.POST.get('radio')
    saveas = project_employee(title=title,category=category,date=start_date,email=email,money=money,descrption=descrption,phone=contact,image=images,end_date=end_date,status=status)
    saveas.save()
    return redirect('project_save')

def donation_portal(request):

    fund_amount = request.POST.get('d1')
    bank_name = request.POST.get('d2')
    bank_acc_number = request.POST.get('d3')
    chequee_number = request.POST.get('d4')
    transaction_date= request.POST.get('d5')
    foreign_donation_id=request.POST.get('frg_key')
    a=request.session['userid']
    print a
    print foreign_donation_id
    saveportal= dontation_portal(fund_amount=fund_amount,bank_name=bank_name,bank_acc_number=bank_acc_number,chequee_number=chequee_number,transaction_date=transaction_date,foreign_donation_id=foreign_donation_id,value_id=a)
    saveportal.save()
    if saveportal.id !=0 or saveportal.id != None or saveportal.id != '' :
        print saveportal.id
        savecredit=profit_account(amount=fund_amount,project_id=foreign_donation_id,date=transaction_date,type_transaction='CREDIT',foreign_id=saveportal.id)
        savecredit.save()
        print savecredit
        return redirect('project_view')


def saveupdate(request):
    donor = request.POST.get('t1')
    father = request.POST.get('t2')
    mobile = request.POST.get('t3')
    dob = request.POST.get('t4')
    address = request.POST.get('t5')
    district = request.POST.get('t6')
    aadhar = request.POST.get('t7')
    blood = request.POST.get('t8')
    email = request.POST.get('t9')
    company = request.POST.get('t10')
    pancard = request.POST.get('t11')
    gst= request.POST.get('t12')
    designation = request.POST.get('t13')
    filesaving = UserProfileModel.objects.filter(donor=donor,father=father,mobile=mobile,dob=dob,address=address,district=district,aadhar=aadhar,blood=blood,email=email,company=company,pancard=pancard,gst=gst,designation=designation)
    filesaving.update(donor=donor,father=father,mobile=mobile,dob=dob,address=address,district=district,aadhar=aadhar,blood=blood,email=email,company=company,pancard=pancard,gst=gst,designation=designation)
    return redirect('District_save')


"""
def logins(request):
    username =request.POST.get('username1', 'this is the default')
    password = request.POST.get('password1', 'this is the default')
    user_data = RegistrationDatas.objects.filter(username=username).filter(password=password)

    for a in user_data:
        if a in user_data:

         return render(request,"account/logout.html")
    else:
        return render(request, "account/login_validation.html")

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")
"""

def register_savefile_retreive(request):
    print(request.session)
    a = master.objects.all()
    return render(request,"account/cpy_index_base_reg.html",{ 'myData': a})


#def update_mobile(request,pk):
 #   UserProfileModel.objects.all().filter(id=pk)
  #  print pk
   # item=UserProfileModel.objects.all()



    #context={
     #   'form':item

    #}
    ##c = BloodModel.objects.all()
    #b = DistrictModel.objects.all()

    #return render(request,"account/filenames/edit_profile.html", {'myData2': c, 'myData1': b},context)

#def update_mobile(req,pk):
 #   post=get_object_or_404(UserProfileModel,id=pk)
  #  if req.method=="POST":
   #     form=UserProfileDetails(req.POST,instance=post)
    #    if form.is_valid():
     #       post=form.save(commit=False)
      #      post.author=req.user
       #     return redirect('District_save')

#    else:
 #       form = UserProfileDetails(instance=post)
  #      template = "account/filenames/edit_profile.html"
   #     context = {'form': form}
    #    c = BloodModel.objects.all()
     #   b = DistrictModel.objects.all()
      #  return render(req, template, {'myData2': c, 'myData1': b}, context)
#edit button for Donor module
def edit_item(request,pk,cls):
    item = get_object_or_404(UserProfileModel,id=pk)
    if request.method == "POST":
        form = cls(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserProfileDetails()
        c = BloodModel.objects.all()
        b = DistrictModel.objects.all()
        e=UserProfileModel.objects.filter(id=pk)
        #retrieve = UserProfileModel.objects.filter(id=pk).values("id", "donor", "father", "address", "district",
         #                                                        "mobile", "dob", "aadhar", "blood", "email", "company",
          #                                                       "designation", "pancard", "gst")
        #print 'sample'
        #print retrieve[0]['district']
        return render(request, "account/filenames/edit_profile.html", {'myData2': c, 'myData1': b,'form': form,'data':e})


#return the edit button
def edit_laptop(request, pk):
    return edit_item(request,pk,UserProfileDetails)


#for view project
def edit_view(request,pk,cls):
    item = get_object_or_404(project_employee,id=pk)
    if request.method == "POST":
        form = cls(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = project_emp()
        c = project_employee.objects.all()
        x = UserProfileModel.objects.all()
        e=project_employee.objects.filter(id=pk)
        l=dontation_portal.objects.filter(foreign_donation_id=pk)


        a = dontation_portal.objects.raw("SELECT project.id,donation.foreign_donation_id,tech_registrationdatas.username,donation.value_id,donation.fund_amount, project.money FROM tech_project_employee as project LEFT join tech_registrationdatas on donation.value_id = tech_registrationdatas.id INNER JOIN tech_dontation_portal as donation ON project.id="+pk+" and donation.foreign_donation_id="+pk+"");

        tot=0
        for value in a:

             tot=tot + value.fund_amount
             print tot


        # donation income and expenses
        income_expenses = profit_account.objects.raw("select project.id,profit.foreign_id,profit.amount,profit.type_transaction,profit.expense_name from tech_project_employee as project  join tech_profit_account as profit on project.id=" + pk + " and profit.project_id=" + pk + "");
        print income_expenses
        income_expenses_data = [];
        sub_total = 0;
        for val in income_expenses:
         temp = {}

         if val.type_transaction == 'CREDIT' :
             if val.amount != None or val.amount != '':
              sub_total += val.amount
             temp['type'] = 'CREDIT'
             temp['amount'] = val.amount
             temp['sub_total'] = sub_total
             income_expenses_data.append(temp)
         else:
             if val.amount != None or val.amount != '':
                 sub_total -= val.amount
                 temp['type'] = 'Debit'
                 temp['amount'] = val.amount
                 temp['sub_total'] = sub_total
                 income_expenses_data.append(temp)
        #else:
           #             if val.amount != None or val.amount != '':
            #              sub_total -= val.amount
             #         temp['type'] = 'Debit'
              #        temp['amount'] = val.amount
               #temp['sub_total'] = sub_total
       # income_expenses_data.append(temp)

        # print income_expenses_data


        return render(request, "account/filenames/viewprojectnxtpge.html",{'myData2': c, 'form': form, 'book': e, 'wel': l, 'ww': x, 'view': a,'total':tot,'profit_loss':income_expenses_data})

        # Get all of the articles within this publication
       # ee=dontation_portal.objects.filter(foreign_donation_id=pk)
        #a=UserProfileModel.objects.filter(id = ee)
        #print a

        #join=dontation_portal.objects.raw("SELECT  tech_dontation_portal.id,tech_userprofilemodel.donor,tech_dontation_portal.fund_amount FROM tech_dontation_portal INNER JOIN tech_userprofilemodel ON  tech_dontation_portal.value_id = tech_userprofilemodel.id WHERE tech_dontation_portal.id =" + pk);
        #join =dontation_portal.objects.raw("select * from tech_dontation_portal")
        #join = UserProfileModel.objects.filter(id=pk).select_related()
       # for y in join:
        #    print y

        #state_ids =UserProfileModel.objects.filter(id=pk)
        #z=dontation_portal.objects.filter(value_id=Subquery(state_ids))
#        for a in dontation_portal.objects.raw("SELECT  tech_dontation_portal.id,tech_userprofilemodel.donor,tech_dontation_portal.fund_amount FROM tech_dontation_portal JOIN tech_userprofilemodel ON  tech_dontation_portal.value_id = tech_userprofilemodel.id"):


            # This will be retrieved by the original query







#return the edit button
def edit_views(request, pk):
    return edit_view(request,pk,project_employee)


#for Invoice


#for view project(invoice total)
def  invoice(request,pk,cls):
    item = get_object_or_404(project_employee,id=pk)
    if request.method == "POST":
        form = cls(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = project_emp()
        c = project_employee.objects.all()
        x = UserProfileModel.objects.all()
        e=project_employee.objects.filter(id=pk)
        l=dontation_portal.objects.filter(foreign_donation_id=pk)

        session_id=request.session['userid']
        session=str(session_id)

      #  a = dontation_portal.objects.raw("SELECT project.id,project.descrption,project.title,donation.bank_name,donation.transaction_date,donation.value_id,tech_userprofilemodel.gst,tech_userprofilemodel.pancard,tech_registrationdatas.id,tech_registrationdatas.username,donation.foreign_donation_id,donation.fund_amount,account.type_transaction FROM tech_userprofilemodel,tech_profit_account as account,tech_project_employee as project LEFT join tech_registrationdatas on donation.value_id = tech_registrationdatas.id  JOIN tech_dontation_portal as donation ON project.id="+pk+" and donation.foreign_donation_id="+pk+"");
        income_expenses1= dontation_portal.objects.raw( "select donation.fund_amount,donation.id from tech_dontation_portal as donation where donation.foreign_donation_id="+ pk +" and donation.value_id="+ session+"");

     #   print income_expenses1
    #    print 'before loop'
        income_expenses_data1 = [];
        total = 0
        for value in income_expenses1:
            temp={}
      #      print 'for loop'

            total+=value.fund_amount
            temp['amount'] = value.fund_amount
            temp['total']=total
        income_expenses_data1.append(temp)
       # print income_expenses_data1
        #print total
        # donation income and expenses
        #income_expenses = profit_account.objects.raw("select project.id,profit.foreign_id,profit.amount,profit.type_transaction,profit.expense_name from tech_project_employee as project  join tech_profit_account as profit on project.id=" + pk + " and profit.project_id=" + pk + "");
        #print income_expenses
        #income_expenses_data = [];
        #sub_total = 0;
        #for val in income_expenses:
        #            temp = {}

         #           if val.type_transaction =='CREDIT':
          #              sub_total+=val.amount
           #             temp['type'] =  'CREDIT'
            #            temp['amount'] = val.amount
             #           temp['sub_total'] =  sub_total
              #          income_expenses_data.append(temp)
               #         print sub_total
                #    else:
                 #       sub_total-=  val.amount
                  #     temp['type'] = 'Debit'
                   #     temp['amount'] = val.amount
                    #    temp['sub_total'] = sub_total
                     #   income_expenses_data.append(temp)
       # print 'xxxx'
        #print sub_total



        #for details of project and descrption field
        a = project_employee.objects.raw("select project.id,project.title,project.descrption,donation.value_id from tech_project_employee as project join tech_dontation_portal as donation on project.id="+pk+" and donation.value_id="+session+"");
        #print a

        income_expenses_data2 = [];
        sub_total = 0;
        for val in a:
         temp1 = {}



         temp1['title'] = val.title
         temp1['id'] = val.id
         temp1['descrption'] = val.descrption



        #print 'xxxx'

        income_expenses_data2.append(temp1)

#for username
        username=RegistrationDatas.objects.raw("select reg.id,reg.username from tech_registrationdatas as reg where id="+session+"")
        income_expenses_data3 = [];
        #print username
        for val in username:
            temp2 = {}

            temp2['username'] = val.username


        #print 'xxxx'

        income_expenses_data3.append(temp2)
        #print income_expenses_data3

 # for gst,pancard
        print 'start'
        values = RegistrationDatas.objects.raw("select sample.project_id,sample.id,sample.address, sample.pancard, sample.gst from tech_userprofilemodel as sample where sample.project_id = "+session+" limit 1")

        print values


        print 'end'

        return render(request,"account/filenames/invoice.html",{'myData2': c, 'form': form, 'book': e, 'wel': l, 'ww': x,'view':income_expenses_data1,'view1':income_expenses_data2,'view2':income_expenses_data3,'view3':values})




#return the edit button
def invoice_generate(request,pk):
    return invoice(request,pk,project_employee)


#for print page invoice:
def  invoice_page_redirect(request,pk,cls):
    item = get_object_or_404(project_employee,id=pk)
    if request.method == "POST":
        form = cls(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = project_emp()
        c = project_employee.objects.all()
        x = UserProfileModel.objects.all()
        e=project_employee.objects.filter(id=pk)
        l=dontation_portal.objects.filter(foreign_donation_id=pk)
        date=datetime.date(datetime.now())

        session_id = request.session['userid']
        session = str(session_id)

        #  a = dontation_portal.objects.raw("SELECT project.id,project.descrption,project.title,donation.bank_name,donation.transaction_date,donation.value_id,tech_userprofilemodel.gst,tech_userprofilemodel.pancard,tech_registrationdatas.id,tech_registrationdatas.username,donation.foreign_donation_id,donation.fund_amount,account.type_transaction FROM tech_userprofilemodel,tech_profit_account as account,tech_project_employee as project LEFT join tech_registrationdatas on donation.value_id = tech_registrationdatas.id  JOIN tech_dontation_portal as donation ON project.id="+pk+" and donation.foreign_donation_id="+pk+"");
        income_expenses1 = dontation_portal.objects.raw(
            "select donation.fund_amount,donation.id from tech_dontation_portal as donation where donation.foreign_donation_id=" + pk + " and donation.value_id=" + session + "");

       # print income_expenses1
        #print 'before loop'
        income_expenses_data1 = [];
        total = 0
        for value in income_expenses1:
            temp = {}
           # print 'for loop'

            total += value.fund_amount
            temp['amount'] = value.fund_amount
            temp['total'] = total
        income_expenses_data1.append(temp)
        #print income_expenses_data1
        #print total
        # donation income and expenses
        # income_expenses = profit_account.objects.raw("select project.id,profit.foreign_id,profit.amount,profit.type_transaction,profit.expense_name from tech_project_employee as project  join tech_profit_account as profit on project.id=" + pk + " and profit.project_id=" + pk + "");
        # print income_expenses
        # income_expenses_data = [];
        # sub_total = 0;
        # for val in income_expenses:
        #            temp = {}

        #           if val.type_transaction =='CREDIT':
        #              sub_total+=val.amount
        #             temp['type'] =  'CREDIT'
        #            temp['amount'] = val.amount
        #           temp['sub_total'] =  sub_total
        #          income_expenses_data.append(temp)
        #         print sub_total
        #    else:
        #       sub_total-=  val.amount
        #     temp['type'] = 'Debit'
        #     temp['amount'] = val.amount
        #    temp['sub_total'] = sub_total
        #   income_expenses_data.append(temp)
        # print 'xxxx'
        # print sub_total

        # for details of project and descrption field
        a = project_employee.objects.raw(
            "select project.id,project.title,project.descrption,donation.value_id from tech_project_employee as project join tech_dontation_portal as donation on project.id=" + pk + " and donation.value_id=" + session + "");
        #print a

        income_expenses_data2 = [];
        sub_total = 0;
        for val in a:
            temp = {}

            temp['title'] = val.title
            temp['id'] = val.id
            temp['descrption'] = val.descrption

        #print 'xxxx'

        income_expenses_data2.append(temp)

        # for username
        username = RegistrationDatas.objects.raw("select reg.id,reg.username from tech_registrationdatas as reg where id=" + session + "")
        income_expenses_data3 = [];
        #print username
        for val in username:
            temp = {}

            temp['username'] = val.username

        #print 'xxxx'

        income_expenses_data3.append(temp)
        #print income_expenses_data3

        # for gst,pancard

        xsd = RegistrationDatas.objects.raw("select users.project_id,users.id,users.address, users.pancard, users.gst from tech_userprofilemodel as users where users.project_id = " + session + " limit 1")
        income_expenses_data44 = [];
        print "start loop"
        print xsd

        for val in xsd:
          temp = {}
          temp['address'] = val.address
          temp['gst'] = val.gst
          temp['pancard'] = val.pancard
        print 'xxxx'
        income_expenses_data44.append(temp)
        print income_expenses_data44

        return render(request, "account/filenames/invoice-print.html",{'date':date,'myData2': c, 'form': form, 'book': e, 'wel': l, 'ww': x, 'view':income_expenses_data1,'view1':income_expenses_data2,'view2':income_expenses_data3,'view3':income_expenses_data44})






#return the edit button
def invoice_print(request, pk):
    return invoice_page_redirect(request,pk,project_employee)

#def edit_vieww(request,pk,cls):
    #a = get_object_or_404(project_employee,id=pk)
    #if request.method == "POST":
       # form = cls(request.POST,instance=a)
       # if form.is_valid():
      #      form.save()
     #       return redirect('index')
    #else:
    #    form = project_emp()
   #     c = project_employee.objects.all()
  #      e=project_employee.objects.filter(id=pk)
        #retrieve = UserProfileModel.objects.filter(id=pk).values("id", "donor", "father", "address", "district",
         #                                                        "mobile", "dob", "aadhar", "blood", "email", "company",
          #                                                       "designation", "pancard", "gst")
        #print 'sample'
        #print retrieve[0]['district']
 #       return render(request, "account/filenames/donatioin_payement.html", {'myData2': c,'form': form,'book':e})


#return the edit button
#def edit_view1(request, pk):
#    return edit_vieww(request,pk,project_employee)








# delete Button

def delete_mobile(request, pk):
    UserProfileModel.objects.filter(id=pk).delete()

    items = UserProfileModel.objects.all()

    context = {
        'items': items,
    }
    c = BloodModel.objects.all()
    b = DistrictModel.objects.all()
    cc= UserProfileModel.objects.all()
    datas = UserProfileModel.objects.raw("select * from tech_userprofilemodel ORDER BY id DESC")
    return render(request,"account/filenames/dataviewpage.html",{'myData2':c,'myData4':cc,'myData1':b,'books':datas}, context)

def projectview(request, pk, cls):
        items = get_object_or_404(project_employee, id=pk)
        if request.method == "POST":
            form = cls(request.POST, instance=items)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = project_employee()
            c = project_employee.objects.all()
            e = project_employee.objects.filter(id=pk)
            # retrieve = UserProfileModel.objects.filter(id=pk).values("id", "donor", "father", "address", "district",
            #                                                        "mobile", "dob", "aadhar", "blood", "email", "company",
            #                                                       "designation", "pancard", "gst")
            # print 'sample'
            # print retrieve[0]['district']
            return render(request, "account/filenames/edit_profile.html",
                          {'myData1': c, 'form': form, 'data': e})



def edit_project(request,pk,cls):
    item = get_object_or_404(project_employee, id=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = project_emp()
        v = project_employee.objects.filter(id=pk)
        # retrieve = UserProfileModel.objects.filter(id=pk).values("id", "donor", "father", "address", "district",
        #                                                        "mobile", "dob", "aadhar", "blood", "email", "company",
        #                                                       "designation", "pancard", "gst")
        # print 'sample'
        # print retrieve[0]['district']
        return render(request, "account/filenames/edit_project.html", {'form': form, 'data':v})


def edit_laptop1(request, pk):
    return edit_project(request,pk,project_emp)

# for foreign key
def donation(request,pk,cls):
    print 'donation called'+ pk
    a = get_object_or_404(dontation_portal, id=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = donation_portal()
        v = project_employee.objects.filter(id=pk)
        return render(request, "account/filenames/donatioin_payement.html", {'form': form, 'data': v})


def donation_money(request, id):
        v = project_employee.objects.filter(id=id)
        return  render(request,"account/filenames/donatioin_payement.html",{'data':v})
#end




'''
#for project view page
def project_view(request,pk,cls):
    item = get_object_or_404(project_employee, id=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = project_emp()
        ab = project_employee.objects.filter(id=pk)
        # retrieve = UserProfileModel.objects.filter(id=pk).values("id", "donor", "father", "address", "district",
        #                                                        "mobile", "dob", "aadhar", "blood", "email", "company",
        #                                                       "designation", "pancard", "gst")
        # print 'sample'
        # print retrieve[0]['district']
        return render(request, "account/filenames/viewprojectnxtpge.html", {'form': form, 'data':ab})

#return project_view
def edit_viewproject(request, pk):
    return project_view(request,pk,project_emp)

'''

def delete_project(request, pk):
    project_employee.objects.filter(id=pk).delete()

    items = project_employee.objects.all()

    context = {
        'items': items,
    }
    val = project_employee.objects.all()
    datas = project_employee.objects.raw("select * from tech_projectdetails ORDER BY id DESC")
    return render(request, "account/filenames/projectdetails_emp.html",{'book':val,'books': datas}, context)





#old:
def edit(req,id):
    books=UserProfileModel.objects.get(pk=id)
    context ={
               'item':books
    }
    return render(req,'account/filenames/dataviewpage.html',context)

def blood_save(request):
    c=BloodModel.objects.all()
    return render(request, "account/filenames/dataviewpage.html", {'myData2': c})

def District_save(request):
    c = BloodModel.objects.all()
    b = DistrictModel.objects.all()
    cc=UserProfileModel.objects.all()
    datas=UserProfileModel.objects.raw("select * from tech_userprofilemodel ORDER BY id DESC")
    return render(request,"account/filenames/dataviewpage.html",{'myData2':c,'myData1':b,'books':datas,'bb':cc})

#def save(request):
   # c = project_employee.objects.all()
    #return render(request,"account/filenames/projectdetails_emp.html",{'book':c})

def project_save(req):
     val=project_employee.objects.all()
     return render(req,"account/filenames/projectdetails_emp.html",{'book':val})
def view(req):
    val = project_employee.objects.all()
    return render(req, "account/filenames/projectview1.html", {'book': val})

def project_view(req):
    val = project_employee.objects.all()
    return render(req, "account/filenames/project_viewpage.html", {'book': val})

def sample(req):

    if  req.session.role == '1':
        val = project_employee.objects.all()
        return render(req, "account/filenames/homepage.html", {'book': val})
    elif  req.session.role == '2':
        val = project_employee.objects.all()
        return render(req, "account/filenames/modulnav.html", {'book': val})
    elif req.session.role == '3':
        val = project_employee.objects.all()
        return render(req, "account/filenames/project_viewpage.html", {'book': val})


#def dropdown(request):
 #   context={"form":District_save}
  #  context1={"form":blood_save}
   # return render(request,context,context1)

def querys():
    return master.objects.get(id=1)

def addUser1(request):

    form = Regs(request.POST)
    if form .is_valid():

        reg=master(id=form.cleaned_data['id'],
                  type = form.cleaned_data['type'],)
        reg.save()


def addUser(request):

    form = Registration(request.POST)
    if form .is_valid():

        register=RegistrationDatas(username=form.cleaned_data['username'],
                                  password = form.cleaned_data['password'],
                                     phone = form.cleaned_data['phone'],
                                     usertype = form.cleaned_data['usertype'],)
        register.save()

    return redirect('login_redirect')

def __str__(self):
    return self.username

def homepage(req):
    a=project_employee.objects.all()
    return render(req,'account/filenames/homepage.html',{'aa':a})
def mainpage(req):
    return render(req,'account/filenames/modulenav.html')
def project_employe(req):
    cc = project_employee.objects.all()
    return render(req, "account/filenames/projectdetails_emp.html",
                  {'bb': cc})


#def donation_money(req):
  #  return render(req,'account/filenames/donatioin_payement.html')


def profit_loss1(req):
    a=project_employee.objects.all()
    print a
    return render(req,'account/filenames/p&l.html',{'project_name':a})


#def upload(req):
 #   if req.method == 'POST':
  #      upload_file=req.FILES.get('document')
   #     fs=FileSystemStorage()
    #    name=fs.save(upload_file.name,upload_file)
     #   context=[url]=fs.url(name)
      #  return render(req,'account/filenames/image.html',context)