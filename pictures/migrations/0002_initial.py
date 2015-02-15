# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GroupPhoto'
        db.create_table(u'pictures_groupphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('list_order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('full_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'pictures', ['GroupPhoto'])

        # Adding model 'Poster'
        db.create_table(u'pictures_poster', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('list_order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('full_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'pictures', ['Poster'])


    def backwards(self, orm):
        # Deleting model 'GroupPhoto'
        db.delete_table(u'pictures_groupphoto')

        # Deleting model 'Poster'
        db.delete_table(u'pictures_poster')


    models = {
        u'pictures.groupphoto': {
            'Meta': {'object_name': 'GroupPhoto'},
            'full_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'pictures.poster': {
            'Meta': {'object_name': 'Poster'},
            'full_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['pictures']