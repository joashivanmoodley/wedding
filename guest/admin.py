# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from guest.models import Guest, Invite


class InviteAdmin(admin.ModelAdmin):
    list_display_links = ('invite_number', 'invite_amount', 'invite_owner')
    list_display = ('invite_number', 'invite_amount', 'invite_owner')
    list_filter = ('invite_number', 'invite_amount', 'invite_owner')
    ordering = ('invite_number', 'invite_amount', 'invite_owner')
    search_fields = ['^invite_number', '^invite_amount', '^invite_owner']


class GuestAdmin(admin.ModelAdmin):
    list_display_links = ('first_name', 'last_name', 'invite', 'attending')
    list_display = ('first_name', 'last_name', 'invite', 'attending')
    list_filter = ('first_name', 'last_name', 'invite', 'attending')
    ordering = ('first_name', 'last_name', 'invite', 'attending')
    search_fields = ['^first_name', '^last_name', '^invite', '^attending']

admin.site.register(Invite, InviteAdmin)
admin.site.register(Guest, GuestAdmin)
