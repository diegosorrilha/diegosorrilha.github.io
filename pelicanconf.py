#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#### Base config ####
AUTHOR = 'Diego Sorrilha'
SITENAME = 'Diego Sorrilha'
SITESUBTITLE = 'Software Engineer & Consultant'
SITEURL = 'http://diegosorrilha.net'
PATH = 'content'
STATIC_PATHS = ['extras/CNAME', 'images', 'favicon.png']
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt'
DEFAULT_PAGINATION = 10
DISQUS_SITENAME = u'diegosorrilha'


#### Theme settings ####
THEME_NAME = 'pelican-clean-blog'
THEME = u'themes/'+ THEME_NAME


# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
FEED_ALL_ATOM = 'feeds.atom'
CATEGORY_FEED_ATOM = 'feeds/%s.atom'
FEED_USE_SUMMARY = True


#### Social ####
GITHUB_URL = 'http://github.com/magnunleno/'
LINKS =  (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)
SOCIAL = (
    ('envelope', 'mailto: diegopsorrilha@gmail.com'),
    ('github', 'https://github.com/diegosorrilha'),
    ('twitter', 'https://twitter.com/diegosorrilha'),
    ('facebook', 'http://facebook.com/sorrilha.diego'),
)


#### Site URL writing ####
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

#### Setup Domain ####
EXTRA_PATH_METADATA = {
    'extras/CNAME': {'path': 'CNAME'},
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
