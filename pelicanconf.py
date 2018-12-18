#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'envoter'
SITENAME = 'Mitos Electorales'
SITEURL = ''
SITESUBTITLE = 'El mítico voto útil y otros cuentos'
SITEDESCRIPTION = (
	"Contraste de los mitos sobre el efecto "
	"de las distintas opciones de voto y de no voto "
	"y su aplicación a las distintas convocatorias "
	"electorales."
)
GITHUB_URL = 'http://github.com/vokimon/envote'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU=False
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Otros"
SUMMARY_USE_FIRST_PARAGRAPH = True

MENUITEMS=(
	('Simulador', 'pages/envote-simulador-de-flujos-electorales.html'),
	#('Mitos', 'mitos.md'),
	#('Memes', 'memes.md'),
)

# Blogroll
_LINKS = (
	('Can Voki', 'http://canvoki.net/'),
)

# Social widget
SOCIAL = (
	('Twitter', '@mitosElectorales'),
)
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
ARTICLE_URL='posts/{date:%Y-%m-%d}-{slug}.html'
ARTICLE_SAVE_AS='posts/{date:%Y-%m-%d}-{slug}.html'

DEFAULT_PAGINATION = None

LICENSE= "by-sa"

JINJA_ENVIRONMENT = {
  'extensions': [
    'jinja2.ext.i18n',
  ],
}
PLUGIN_PATHS = [
	'repos/pelican-plugins',
]
PLUGINS = [
	#'pelican_albums',
	'summary',
	'i18n_subsites',
	'render_math',
]

I18N_TEMPLATES_LANG = 'en'


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

BLOG_AUTHORS={}


#THEME = 'themes/aboutwilson'
#THEME = 'themes/backdrop'
#THEME = 'themes/basic'
#THEME = 'themes/bootlex' # vale
#THEME = 'themes/bootstrap' # vale
#THEME = 'themes/bootstrap2'
#THEME = 'themes/bootstrap2-dark'
#THEME = 'themes/new-bootstrap2'
#THEME = 'themes/simple-bootstrap'
#THEME = 'themes/pelican-bootstrap3'

#THEME = 'themes/bricabrac' # no furula
#THEME = 'themes/bricks' # plus plus
#THEME = 'themes/brownstone' # cool
#THEME = 'themes/built-texts'
#THEME = 'themes/cebong'
#THEME = 'themes/dev-random'
#THEME = 'themes/dev-random2'
#THEME = 'themes/foundation-default-colours'
#THEME = 'themes/franticworld' # layout guai no para envote
#THEME = 'themes/graymill'
#THEME = 'themes/gum'
#THEME = 'themes/Just-Read'
#THEME = 'themes/lightweight'
#THEME = 'themes/martyalchin'
#THEME = 'themes/medio'
#THEME = 'themes/mnmlist'
#THEME = 'themes/monospace'
#THEME = 'themes/nmnlist'
#THEME = 'themes/notebook'
#THEME = 'themes/notmyidea-cms'
#THEME = 'themes/notmyidea-cms-fr'
#THEME = 'themes/ops'
#THEME = 'themes/pelican-striped-html5up'
#THEME = 'themes/photowall'
#THEME = 'themes/sneakyidea'
#THEME = 'themes/SOB'
#THEME = 'themes/SoMA'
#THEME = 'themes/SoMA2'
#THEME = 'themes/subtle'
#THEME = 'themes/syte'
#THEME = 'themes/tuxlite_tbs'
#THEME = 'themes/tuxlite_zf'
#THEME = 'themes/uikit'
#THEME = 'themes/waterspill'
#THEME = 'themes/waterspill-en'
#THEME = 'themes/zurb-F5-basic'
THEME = 'pelican-theme-votingmyths'
