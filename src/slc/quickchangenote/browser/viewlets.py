from json import dumps
from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from slc.quickchangenote.interfaces import IQuickChangenoteSettings
from slc.quickchangenote.utils import changenoteRequired, getSettings

class QuickChangenoteViewlet(ViewletBase):
    index = ViewPageTemplateFile('javascript.pt')

    def notes(self):
        """ Returns the possible changenotes as a tuple. """
        settings = getSettings()
        if settings is None or settings.notes is None:
            return ()
        return tuple(settings.notes)

    def json_notes(self):
        """ Returns the change notes as a json string. """
        return dumps(self.notes())

    def required(self):
        """ returns whether a change note is required on each save. """
        return changenoteRequired(self.context)
