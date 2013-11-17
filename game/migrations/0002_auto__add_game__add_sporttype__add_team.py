# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table(u'game_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('team2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('score', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('draw', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('win_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_team', to=orm['game.Team'])),
            ('sport', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_sport_type', to=orm['game.SportType'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'game', ['Game'])

        # Adding model 'SportType'
        db.create_table(u'game_sporttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'game', ['SportType'])

        # Adding model 'Team'
        db.create_table(u'game_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'game', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table(u'game_game')

        # Deleting model 'SportType'
        db.delete_table(u'game_sporttype')

        # Deleting model 'Team'
        db.delete_table(u'game_team')


    models = {
        u'game.game': {
            'Meta': {'object_name': 'Game'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'draw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sport': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_sport_type'", 'to': u"orm['game.SportType']"}),
            'team1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'team2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'win_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_team'", 'to': u"orm['game.Team']"})
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
        }
    }

    complete_apps = ['game']