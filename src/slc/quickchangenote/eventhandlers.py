from Acquisition import aq_inner
from zope.interface import implements 
from zope.component import adapts, queryUtility
from plone.registry.interfaces import IRegistry
from Products.Archetypes.interfaces import IObjectPostValidation
from Products.Archetypes.interfaces import IBaseContent
from Products.CMFCore.utils import getToolByName
from slc.quickchangenote.interfaces import IQuickChangenoteSettings
from slc.quickchangenote import MessageFactory as _

def isVersionable(ob):
    try:
        pr = getToolByName(ob, 'portal_repository')
    except AttributeError:
        return None
    return pr.isVersionable(ob);

class ValidateChangenote(object):
    """ Validate that the user has provided a change note. """
    implements(IObjectPostValidation)
    adapts(IBaseContent)
    field_name = 'cmfeditions_version_comment'

    def __init__(self, context):
        self.context = context

    def __call__(self, request):
        registry = queryUtility(IRegistry)
        if registry is None:
            return None
        if registry.forInterface(IQuickChangenoteSettings).required:
            context = aq_inner(self.context)
            if isVersionable(context):
                value = request.form.get(self.field_name,
                    request.get(self.field_name, ''))
                if len(value) == 0:
                    return {self.field_name: _(
                        u'A change note must be provided')}
