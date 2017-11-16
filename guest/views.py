# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import qrcode
from cStringIO import StringIO
from guest.models import Guest
# Create your views here.


def confirmation(request):
    template_data = {}
    template = 'confirmation.html'
    return render(request, template, template_data,)


def rsvp(request, id):
    guests = Guest.objects.filter(invite__invite_number=id)
    template_data = {
        'id': id,
        'guests': guests
    }
    template = 'qr-scan.html'
    if request.POST:
        for guest in guests:
            if 'attending_%s_%s' % (guest.first_name, guest.last_name) in request.POST:
                guest.attending = True
                guest.save()
                return HttpResponseRedirect('/confirmation/')

    return render(request, template, template_data,)


def index(request, ):

    template_data = {
    }
    template = 'index.html'

    return render(request, template, template_data)


def create_qr_code(request):
    url = 'http://www.jowedstam.co.za/rsvp/'
    for id in range(1, 101):
        rsvp_url = "%s%s/" % (url, id)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=0,
        )
        qr.add_data(rsvp_url)

        # Generate image
        qr_code = qr.make_image(fit=True)

        # Write to StringIO()
        io = StringIO()
        qr_code.save(io)
        f = open('%s.png' % id, 'wb')
        f.write(io.getvalue())
        f.close()
        io.close()


    return HttpResponse('done')