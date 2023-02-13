AUTHOR = 'Pawel Cwiek'
SITENAME = 'Mennova'
SITEDESCRIPTION = 'this is just an example page for the pelican-fh5co-marble theme.'
SITEURL = ''

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en','pages/pl']
ARTICLE_PATHS = ['blog/en','pages/pl']

TIMEZONE = 'Europe/Warsaw'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = r"themes/fh5co-marble"

# logo path, needs to be stored in PATH Setting
LOGO = 'images/logo.svg'

# plugins
PLUGIN_PATHS = ['./plugins/cloned/pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_SUBSITES = {
  'pl': {
    'PAGE_PATHS': ['pages/pl'],
    'ARTICLE_PATHS': ['blog/pl'],
    'LOCALE': 'pl_PL'
  }
}
I18N_GETTEXT_LOCALEDIR = THEME + '/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'pl_PL'