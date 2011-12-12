# -*- coding: utf-8 -*-
from persistent import Persistent
from plone.app.controlpanel.form import ControlPanelForm
from plone.fieldsets.fieldsets import FormFieldsets
from slc.quickchangenote.interfaces import IQuickChangenoteSettings
from slc.quickchangenote import MessageFactory as _
from zope.annotation.interfaces import IAnnotations
from zope.component import getUtility
from zope.interface import implements


SETTING_KEY="slc.quickchangenote.settings"


def quick_changenote_settings(context):
    return getUtility(IQuickChangenoteSettings)

class Settings(Persistent):
    """Settings for a site/subsite
    """
    notes = list()
    required = ''
    required_on_new = ''


class QuickChangenoteSettings(Persistent):
    implements(IQuickChangenoteSettings)

    @apply
    def notes():
        def get(self):
            return [x for x in self.settings.notes]
        def set(self, value):
            self.settings.notes = value   
        return property(get, set)
   

    def get_required(self):
        return self.settings.required
    def set_required(self, value):
        self.settings.required = value
    required = property(get_required, set_required)

    def get_required_on_new(self):
        return self.settings.required_on_new
    def set_required_on_new(self, value):
        self.settings.required_on_new = value
    required = property(get_required_on_new, set_required_on_new)

    @property
    def settings(self):
        site = getSite()
        ann = IAnnotations(site)
        return ann.setdefault(SETTING_KEY, Settings())

default_set = FormFieldsets(IQuickChangenoteSettings)
default_set.id ='default'
default_set.label = _(u"Default")

class QuickChangenoteControlPanel(ControlPanelForm):
    form_fields = FormFieldsets(default_set)
    form_name = _(u"do I need a form name?")
    label = _(u"Quick Changenote Settings")
    description = _(u"Use the settings below to configure "
                    u"slc.quickchangenote for this site")
