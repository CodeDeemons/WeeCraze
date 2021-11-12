from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
booking_details = {}

def select_dest(request, dest_name):
    booking_details["destiny"] = dest_name
    return HttpResponseRedirect('/vehicle/', {'vehicle' : 'active'})

def select_vehicle(request, vehicle_name):
    booking_details["vehicle"] = vehicle_name
    return HttpResponseRedirect('/thank_you/')

def thank_you(request):
    if booking_details and request.user.is_authenticated:
        return render(request, 'booking/thank_you.html', booking_details)
    else:
        return HttpResponseRedirect('/')