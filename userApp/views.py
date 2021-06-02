from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dynamictariff.url import get_url
import math, requests

@login_required(login_url='/accounts/')
def home_view(request):
    User = request.user
    url = get_url("appF.php")
    pload = {'function':'Home'}
    response = requests.post(url, data = pload).text
    loadCurve = response[10:].split('~')[0].split('+')
    unitPrice = response[10:].split('~')[1].split('+')

    pload = {'function':'Analytics'}
    response = requests.post(url, data = pload).text
    loadTypeData = response[10:].split('~')[0].split('+')
    loadType = []
    total = 0
    for i in range(0,3):
        item = loadTypeData[i].replace('[', '')
        item = item.replace(']', '')
        item = float(item)
        loadType.append(item)
        total += item
    loadType = [x/total*100 for x in loadType]
    
    dispatchData = response[10:].split('~')[1].split('+')
    dispatchDataData = []
    dispatchThermal = []
    dispatchSolar = []
    dispatchHydel = []

    for i in range(0,24):
        item = dispatchData[i].replace('[', '')
        item = item.replace(']', '')
        dispatchDataData.append(item)
    for i in range(24):
        dispatchThermal.append(dispatchDataData[i].split(',')[0])
        dispatchSolar.append(dispatchDataData[i].split(',')[1])
        dispatchHydel.append(dispatchDataData[i].split(',')[2])
    
    relComp = response[10:].split('~')[2].split('+')
    relCompData = []
    brt = []
    dt = []
    adt = []

    for i in range(12):
        item = relComp[i].replace('[', '')
        item = item.replace(']', '')
        relCompData.append(item)
    for i in range(12):
        brt.append(100)
        dt.append(relCompData[i].split(',')[0])
        adt.append(relCompData[i].split(',')[1])

    # currUser = tblUser.objects.get(user_id = User.email)
   
    # t1 = currUser.lastTime
    # bill = currUser.bill
    # consumedUnits = currUser.consumedUnits
    # currActiveLoad = currUser.currActiveLoad
    # cost = TblUnitprice.objects.values('cost')

    # unitPrice = []
    # for item in cost:
    #     unitPrice.append(item.get('cost'))

    # fmt = "%d:%H:%M"
    # if  t1 == '01:00:00':
    #     t1 = datetime.now().strftime(fmt)
    # t2 = datetime.now().strftime(fmt)
    # tDiff = datetime.strptime(t2, fmt) - datetime.strptime(t1, fmt)
    # totalMin = math.floor(tDiff.total_seconds()/60)
    # currHr = datetime.strptime(t2, fmt).strftime("%H")
    # index = int(currHr)

    # j = totalMin%60
    # for i in range(totalMin):
    #     bill += currActiveLoad*(unitPrice[index]/60)
    #     j -= 1
    #     if j < 0:
    #         j = 59
    #         index -= 1
    #         if index < 0:
    #             index = 23

    # currUser.bill = bill
    # currUser.consumedUnits += currActiveLoad*(totalMin/60)
    # currUser.lastTime = t2

    # if request.method == 'POST':
    #     action = request.POST.get('load_action')
    #     action = int(action)
    #     load = request.POST.getlist('load')

    #     total_load = 0
    #     for unit_load in load:
    #         unit_load = int(unit_load)
    #         total_load += unit_load
        
    #     if action:
    #         currUser.currActiveLoad += total_load
    #     elif not action:
    #         if (currActiveLoad - total_load) < 0:
    #             currUser.currActiveLoad = 0
    #         else:
    #             currUser.currActiveLoad -= total_load
    #     else:
    #         pass
    # else:
    #     pass

    # currUser.save()

    # context = {
    #     'tbl_cost' : TblUnitprice.objects.values('hour', 'cost'),
    #     'tbl_user' : tblUser.objects.get(user_id = User.email)
    # }
    context = {
        'n24' : range(24),
        'n12' : range(12),
        'n3' : range(3),
        'loadCurve' : loadCurve,
        'unitPrice' : unitPrice,
        'loadType' : loadType,
        'dispatchThermal' : dispatchThermal,
        'dispatchSolar' : dispatchSolar,
        'dispatchHydel' : dispatchHydel,
        'relComp' : relComp,
        'brt' : brt,
        'dt' : dt,
        'adt' : adt
    }
    return render(request, 'userApp/home.html', context=context)
    
@login_required(login_url='/accounts/')
def profile_view(request):
    return render(request, 'userApp/profile.html')

def test_view(request):
    user = User.objects.get(username='asd')
    return render(request, 'userApp/test.html', context={'data':user})