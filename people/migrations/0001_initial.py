# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CurrentMember'
        db.create_table(u'people_currentmember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('img_height', self.gf('django.db.models.fields.PositiveIntegerField')(default=100)),
            ('img_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=80)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('work_title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('work_number', self.gf('django.db.models.fields.CharField')(default='617-496-8654', max_length=16)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal(u'people', ['CurrentMember'])


    def backwards(self, orm):
        # Deleting model 'CurrentMember'
        db.delete_table(u'people_currentmember')


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
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'work_number': ('django.db.models.fields.CharField', [], {'default': "'617-496-8654'", 'max_length': '16'}),
            'work_title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['people']