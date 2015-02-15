# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Background'
        db.create_table('about_xie_background', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year_start', self.gf('django.db.models.fields.IntegerField')()),
            ('year_end', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal('about_xie', ['Background'])


    def backwards(self, orm):
        # Deleting model 'Background'
        db.delete_table('about_xie_background')


    models = {
        'about_xie.background': {
            'Meta': {'object_name': 'Background'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year_end': ('django.db.models.fields.IntegerField', [], {}),
            'year_start': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['about_xie']