#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin-satchmo-s3slider',
    version='0.0.1',
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = 'DjangoCMS image gallery plugin for satchmo '
                  'product category. Special support for '
                  'thumbnails and s3Slider '
                  'http://www.serie3.info/s3slider/demonstration.html ',
    packages=find_packages(),
    provides=['cmsplugin_satchmo_s3slider', ],
    include_package_data=True,
    install_requires = [
        'easy-thumbnails',
        'django-sekizai',
        ],
    package_data={
        'cmsplugin-satchmo-s3slider': [
            'templates/cmsplugin_s3slider/*.html',
            'media/js/*.js'
        ]
    },
)
