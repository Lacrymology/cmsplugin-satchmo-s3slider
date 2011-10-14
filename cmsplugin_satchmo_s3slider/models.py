import threading
from product.models import Category
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

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
    product_category = models.ForeignKey(Category,
                                         verbose_name = _('Product Category'),
                                         help_text = _('Category that should '
                                                       'be used to create this '
                                                       'gallery'))
    
    POSITIONS = (
        ('left', _('Left')),
        ('right', _('Right')),
        ('center', _('Center')),
        )
    alignment = models.CharField(max_length=8,
                                 choices=POSITIONS,
                                 default='left')

    def images(self):
        class Image:
            def __init__(self, image, title=None, text=""):
                self.image = image
                self.title = title
                self.text = text

            def __getattr__(self, attr):
                return getattr(self.image, attr)

        category = self.product_category
        images = []
        for p in category.product_set.all():
            if p.productimage_set.count():
                image = Image(p.productimage_set.all()[0].picture,
                              title=p.name, text=mark_safe(p.description))
                images.append(image)
        
        return images

    def width(self):
        images = self.images()
        if images:
            return max([i.width for i in images])
        else:
            return 0

    def height(self):
        images = self.images()
        if images:
            return max([i.height for i in images])
        else:
            return 0

    def span_height(self):
        return self.height() - 13

    def span_width(self):
        return self.width() - 10
    
    def __unicode__(self):
        return _('Category Gallery: %(category)s') % {
            'category': unicode(self.product_category)
            }
