# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from cStringIO import StringIO
# Create your views here.


def rsvp(request, id):
    template_data = {
        'id': id
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