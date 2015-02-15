# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CurrentMember.personal_title'
        db.add_column(u'people_currentmember', 'personal_title',
                      self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True),
                      keep_default=False)


        # Changing field 'CurrentMember.work_title'
        db.alter_column(u'people_currentmember', 'work_title', self.gf('django.db.models.fields.CharField')(max_length=8))
        # Adding field 'FormerMember.personal_title'
        db.add_column(u'people_formermember', 'personal_title',
                      self.gf('django.db.models.fields.CharField')(max_length=8, null=True, blank=True),
                      keep_default=False)


        # Changing field 'FormerMember.work_title'
        db.alter_column(u'people_formermember', 'work_title', self.gf('django.db.models.fields.CharField')(max_length=8))

    def backwards(self, orm):
        # Deleting field 'CurrentMember.personal_title'
        db.delete_column(u'people_currentmember', 'personal_title')


        # Changing field 'CurrentMember.work_title'
        db.alter_column(u'people_currentmember', 'work_title', self.gf('django.db.models.fields.CharField')(max_length=32))
        # Deleting field 'FormerMember.personal_title'
        db.delete_column(u'people_formermember', 'personal_title')


        # Changing field 'FormerMember.work_title'
        db.alter_column(u'people_formermember', 'work_title', self.gf('django.db.models.fields.CharField')(max_length=32))

    models = {
        u'people.currentmember': {
            'Meta': {'object_name': 'CurrentMember'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100'}),
            'img_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '80'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'personal_title': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'work_number': ('django.db.models.fields.CharField', [], {'default': "'617-496-8654'", 'max_length': '16'}),
            'work_title': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        u'people.formermember': {
            'Meta': {'object_name': 'FormerMember'},
            'current_association': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'current_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lab_period': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'personal_title': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'work_title': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['people']