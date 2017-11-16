# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

NAME = ['TAMSIN', 'JOASH']


class Invite(models.Model):
    invite_number = models.IntegerField(primary_key=True)
    invite_amount = models.IntegerField()
    invite_owner = models.CharField(max_length=20, choices=zip(NAME, NAME), db_index=True)

    def __unicode__(self):
        return "%s" % (unicode(self.invite_number))


class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    invite = models.ForeignKey(Invite)
    attending = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (unicode(self.first_name), unicode(self.last_name))
