=========================================
DjangoCMS Satchmo s3Slider Gallery plugin
=========================================

Features
--------

1. Unlimited, auto-discovered custom templates - you can change template 
   of given gallery at anytime, use javascript galleries etc. 

2. Native support for http://www.serie3.info/s3slider/demonstration.html

Requirements
------------

- easy-thumbnails http://pypi.python.org/pypi/easy-thumbnails/
- sekizai http://pypi.python.org/pypi/django-sekizai
- django-cms
- satchmo

Installation
------------

1. Install requirements and put ``cmsplugin_satchmo_s3slider`` on your python path 
   (requirements will be installed automatically if you use ``pip`` 
   with ``-e https://Lacrymology@github.com/Lacrymology/cmsplugin-satchmo-s3slider.git``

2. Add ``cmsplugin_satchmo_s3slider``, ``easy_thumbnails`` and ``sekizai`` to your installed apps

3. Run ``syncdb`` or ``migrate cmsplugin_satchmo_s3slider`` (if you use South). 

4. Very simple template is included with the project. It comes with the
   s3Slider gallery plugin javascript packed, and ready to work.
   It also expects you to have a "css" and a "js" sekizai blocks
   rendered in your template.
   You can modify the template to fix the css to suit your needs.

Usage
-----

The easiest approach is to use a nice feature of cmsplugin-satchmo-s3slider -
the template autodiscovery. In order to take advantage of it, add your custom 
templates in the cmsplugin_satchmo_s3slider subdirectory of any of template dirs scanned
by Django.

If you don't want to use the autodiscovery, you can hardcode available templates
in settings.py using following setting:

::

    CMSPLUGIN_SATCHMO_S3SLIDER_TEMPLATES = (
        ('app/template.html', 'Template #1', ),
        ('app/other_template.html', 'Template #2', ),
    )

Embed as a typical plugin.
