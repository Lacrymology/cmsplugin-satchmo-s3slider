from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from cmsplugin_satchmo_s3slider import models


class CMSSatchmoGalleryPlugin(CMSPluginBase):
    model = models.ProductGalleryPlugin
    name = _('Product Image gallery')
    render_template = 'cmsplugin_satchmo_s3slider/gallery.html'

    def render(self, context, instance, placeholder):
        context.update({
                        'images': instance.images(),
                        'gallery': instance,
                        'slider_id': "slider%d"%instance.pk,
                       })
        self.render_template = instance.template
        return context

plugin_pool.register_plugin(CMSSatchmoGalleryPlugin)
