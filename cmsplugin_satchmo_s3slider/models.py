import threading

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from inline_ordering.models import Orderable

import utils

localdata = threading.local()
localdata.TEMPLATE_CHOICES = utils.autodiscover_templates()
TEMPLATE_CHOICES = localdata.TEMPLATE_CHOICES

class GalleryPlugin(CMSPlugin):

    template = models.CharField(
        max_length=255,
        choices=TEMPLATE_CHOICES,
        default='cmsplugin_s3slider/gallery.html',
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


class Image(Orderable):
    def get_media_path(self, filename):
        pages = self.gallery.placeholder.page_set.all()
        return pages[0].get_media_path(filename)

    gallery = models.ForeignKey(GalleryPlugin)
    src = models.ImageField(upload_to=get_media_path,
                            height_field='src_height',
                            width_field='src_width')
    src_height = models.PositiveSmallIntegerField(editable=False, null=True)
    src_width = models.PositiveSmallIntegerField(editable=False, null=True)
    alt = models.CharField(
        max_length=127,
        blank=True,
        )

    position_options = (
        ('top', _('Top')),
        ('bottom', _('Bottom')),
        ('left', _('Left')),
        ('right', _('Right')),
        )
    textPosition = models.CharField(
        default = 'bottom',
        choices = position_options,
        max_length = max([len(v) for (k,v) in position_options]),
        )
    title = models.CharField(max_length=255, blank=True)
    text = models.CharField(max_length=2047, blank=True)

    def __unicode__(self):
        return self.title or self.alt or str(self.pk)
