#!/usr/bin/env bash
heroku plugins:install heroku-repo
heroku repo:purge_cache -a appname
