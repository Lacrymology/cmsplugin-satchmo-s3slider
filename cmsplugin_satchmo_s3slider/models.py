import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

import utils

localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES

class ProductGalleryPlugin(CMSPlugin):

    template = models.CharField(
        max_length=255,
        choices=TEMPLATE_CHOICES,
        default='cmsplugin_satchmo_s3slider/gallery.html',
        editable=len(TEMPLATE_CHOICES) > 1)

    timeout = models.IntegerField(default=3000)
    
    POSITIONS = (
        ('left', _('Left')),
        ('right', _('Right')),
        ('center', _('Center')),
        )
    alignment = models.CharField(max_length=8,
                                 choices=POSITIONS,
                                 default='left')
    
    def width(self):
        return max([i.src_width for i in self.image_set.all()])
    def height(self):
        return max([i.src_height for i in self.image_set.all()])
    
    def __unicode__(self):
        return _(u'%(count)d image(s) in gallery') % {
            'count': self.image_set.count()
            }
