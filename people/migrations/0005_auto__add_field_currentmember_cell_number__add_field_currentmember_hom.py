# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CurrentMember.cell_number'
        db.add_column('people_currentmember', 'cell_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'CurrentMember.home_number'
        db.add_column('people_currentmember', 'home_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=16, blank=True),
                      keep_default=False)

        # Adding field 'CurrentMember.address'
        db.add_column('people_currentmember', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CurrentMember.cell_number'
        db.delete_column('people_currentmember', 'cell_number')

        # Deleting field 'CurrentMember.home_number'
        db.delete_column('people_currentmember', 'home_number')

        # Deleting field 'CurrentMember.address'
        db.delete_column('people_currentmember', 'address')


    models = {
        'people.currentmember': {
            'Meta': {'object_name': 'CurrentMember'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'cell_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'home_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100'}),
            'img_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '80'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'personal_title': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'work_number': ('django.db.models.fields.CharField', [], {'default': "'617-496-8654'", 'max_length': '16'}),
            'work_title': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'people.formermember': {
            'Meta': {'object_name': 'FormerMember'},
            'current_association': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'current_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_period': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'personal_title': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'work_title': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['people']