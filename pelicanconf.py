#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = 'Nicolas Reigl'
SITEURL = u'http://localhost:8000'
SITENAME = "nreigl.github.io"
DELETE_OUTPUT_DIRECTORY = False
RELATIVE_URLS = True

PATH = 'content'
TIMEZONE = 'Europe/Tallinn'
DEFAULT_LANG = 'en'

# Subtitles
# SITESUBTITLE = u'Nicolas Reigl'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
FAVICON = '/Users/nicolasreigl/nreigl/content/images/'
SOCIAL = (
        # ('email', 'mailto: nicolas.reigl@gmail.com','envelope'),
        ('mail',"http://www.google.com/recaptcha/mailhide/d?k=01BviSVWzNrekEzqzsin07RQ==&c=nzcwNtW28F8q_ue1ltZNKO96TpMM2YmEHrNrpQEXI1s=" ,'envelope'),
        ('github', 'https://github.com/nreigl'),
        ('twitter', 'https://twitter.com/NicolasReigl')
        )
MARKUP = ('md', 'ipynb')
DEFAULT_PAGINATION = 1000
DISPLAY_CATEGORIES_ON_MENU = False
ARTICLE_ORDER_BY = 'reversed-date'
PAGE_ORDER_BY = 'order'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'index.html'
SHOW_ABOUTME = 'FALSE'
PATH = 'pages'
STATIC_PATHS = ['images', 'static', 'files']
AUTHOR_SAVE_AS = ''
#TYPOGRIFY = False
#TYPOGRIFY_IGNORE_TAGS = ['a']
FEED_USE_SUMMARY = True
CC_LICENSE = 'CC-BY-SA'
AVATAR = 'images/nicolas_sundown.jpg'

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
            },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
            }
        }


# Plugin-related settings
PLUGIN_PATHS = ["plugins", '/Users/nicolasreigl/nreigl/pelican-plugins']
PLUGINS = ['i18n_subsites',
        "render_math",
        # 'feed_summary',
        # # 'ipynb',
        'share_post',
        'render_math',
        'share_post',
        'sitemap',
        # 'pandoc_reader',
        # 'rmd_pandoc_reader',
        'rmd_reader',
        #'pelican-btex',
        # 'disqus_static',
        'better_figures_and_images',
        "latex"]
JINJA_ENVIRONMENT = {
        'extensions': ['jinja2.ext.i18n',
            ],
        }

PYGMENTS_STYLE = 'friendly'

FEED_USE_SUMMARY = True

# Theme-related settings
THEME = '/Users/nicolasreigl/nreigl/pelican-bootstrap3'

