from __future__ import absolute_import, unicode_literals

from wagtailmedia.widgets import AdminMediaChooser

try:
    from wagtail.admin.edit_handlers import BaseChooserPanel
except ImportError:  # fallback for wagtail <2.0
    from wagtail.wagtailadmin.edit_handlers import BaseChooserPanel


class MediaChooserPanel(BaseChooserPanel):
    object_type_name = 'media'

    def widget_overrides(self):
        return {self.field_name: AdminMediaChooser}
