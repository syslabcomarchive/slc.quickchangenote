from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from slc.quickchangenote.interfaces import IQuickChangenoteSettings
from slc.quickchangenote import MessageFactory as _

class QuickChangenoteSettings(RegistryEditForm):
    schema = IQuickChangenoteSettings
    label = _(u"Quick Changenote Settings")
    description = _(u"Use the settings below to configure "
                    u"slc.quickchangenote for this site")

class QuickChangenoteControlPanel(ControlPanelFormWrapper):
    form = QuickChangenoteSettings
