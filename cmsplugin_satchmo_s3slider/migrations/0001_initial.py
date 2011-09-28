# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProductGalleryPlugin'
        db.create_table('cmsplugin_productgalleryplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('template', self.gf('django.db.models.fields.CharField')(default='cmsplugin_s3slider/gallery.html', max_length=255)),
            ('timeout', self.gf('django.db.models.fields.IntegerField')(default=3000)),
            ('alignment', self.gf('django.db.models.fields.CharField')(default='left', max_length=8)),
        ))
        db.send_create_signal('cmsplugin_satchmo_s3slider', ['ProductGalleryPlugin'])


    def backwards(self, orm):
        
        # Deleting model 'ProductGalleryPlugin'
        db.delete_table('cmsplugin_productgalleryplugin')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_satchmo_s3slider.productgalleryplugin': {
            'Meta': {'object_name': 'ProductGalleryPlugin', 'db_table': "'cmsplugin_productgalleryplugin'", '_ormbases': ['cms.CMSPlugin']},
            'alignment': ('django.db.models.fields.CharField', [], {'default': "'left'", 'max_length': '8'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_s3slider/gallery.html'", 'max_length': '255'}),
            'timeout': ('django.db.models.fields.IntegerField', [], {'default': '3000'})
        }
    }

    complete_apps = ['cmsplugin_satchmo_s3slider']
