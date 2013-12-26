# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'UserForecast.date'
        db.alter_column(u'game_userforecast', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'UserForecast.date'
        db.alter_column(u'game_userforecast', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.forecast': {
            'Meta': {'object_name': 'Forecast'},
            'detailed': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'draw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forecast_game'", 'to': u"orm['game.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'supernumerary': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'forecast_supernumerary'", 'null': 'True', 'to': u"orm['user_profile.Supernumerary']"}),
            'win_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'forecast_team'", 'null': 'True', 'to': u"orm['game.Team']"}),
            'wrong': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'game.game': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'draw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game_sport_type'", 'null': 'True', 'to': u"orm['game.SportType']"}),
            'team1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'win_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game_team'", 'null': 'True', 'to': u"orm['game.Team']"})
        },
        u'game.sporttype': {
            'Meta': {'object_name': 'SportType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'game.userforecast': {
            'Meta': {'ordering': "('date',)", 'object_name': 'UserForecast'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'forecast': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_forecast_forecast'", 'to': u"orm['game.Forecast']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supernumerary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_forecast_supernumerary'", 'to': u"orm['user_profile.Supernumerary']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_forecast_user'", 'to': u"orm['user_profile.CustomUser']"})
        },
        u'packages.package': {
            'Meta': {'object_name': 'Package'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'forecasts': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'one': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'packages.userpackage': {
            'Meta': {'object_name': 'UserPackage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_package_package'", 'null': 'True', 'to': u"orm['packages.Package']"}),
            'predictions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'supernumerary': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_package_supernumerary'", 'null': 'True', 'to': u"orm['user_profile.Supernumerary']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_package_custom_user'", 'to': u"orm['user_profile.CustomUser']"})
        },
        u'user_profile.customuser': {
            'Meta': {'object_name': 'CustomUser', '_ormbases': [u'auth.User']},
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'left': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['packages.UserPackage']", 'null': 'True', 'blank': 'True'}),
            'used': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'user_profile.supernumerary': {
            'Meta': {'object_name': 'Supernumerary', '_ormbases': [u'auth.User']},
            'about': ('django.db.models.fields.TextField', [], {}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'right': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['user_profile.CustomUser']", 'null': 'True', 'blank': 'True'}),
            'wrong': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['game']