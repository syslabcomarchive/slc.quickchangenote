from json import dumps
from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from slc.quickchangenote.interfaces import IQuickChangenoteSettings

class QuickChangenoteViewlet(ViewletBase):
    index = ViewPageTemplateFile('javascript.pt')

    def settings(self):
        registry = queryUtility(IRegistry)
        if registry is None:
            return None
        return registry.forInterface(IQuickChangenoteSettings)
        

    def notes(self):
        """ Returns the possible changenotes as a tuple. """
        settings = self.settings()
        if settings is None:
            return ()
        return tuple(settings.notes)

    def json_notes(self):
        """ Returns the change notes as a json string. """
        return dumps(self.notes())

    def required(self):
        """ returns whether a change note is required on each save. """
        settings = self.settings()
        if settings is None:
            # Default behaviour is also plone default, it is not required
            return False
        return settings.required
