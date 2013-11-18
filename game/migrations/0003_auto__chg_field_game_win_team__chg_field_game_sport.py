# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Game.win_team'
        db.alter_column(u'game_game', 'win_team_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['game.Team']))

        # Changing field 'Game.sport'
        db.alter_column(u'game_game', 'sport_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['game.SportType']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Game.win_team'
        raise RuntimeError("Cannot reverse this migration. 'Game.win_team' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Game.win_team'
        db.alter_column(u'game_game', 'win_team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Team']))

        # User chose to not deal with backwards NULL issues for 'Game.sport'
        raise RuntimeError("Cannot reverse this migration. 'Game.sport' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Game.sport'
        db.alter_column(u'game_game', 'sport_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.SportType']))

    models = {
        u'game.game': {
            'Meta': {'object_name': 'Game'},
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
        }
    }

    complete_apps = ['game']