# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Background.year_start'
        db.alter_column('about_xie_background', 'year_start', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Background.year_start'
        db.alter_column('about_xie_background', 'year_start', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        'about_xie.background': {
            'Meta': {'object_name': 'Background'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['about_xie']