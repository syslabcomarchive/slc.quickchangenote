from Acquisition import aq_inner

from zope.interface import implements 
from zope.component import adapts
from zope.annotation.interfaces import IAnnotations

from Products.Archetypes.interfaces import IObjectPostValidation
from Products.Archetypes.interfaces import IBaseContent
from Products.CMFCore.utils import getToolByName

from slc.quickchangenote.utils import changenoteRequired
from slc.quickchangenote.interfaces import IQuickChangenoteLayer
from slc.quickchangenote import MessageFactory as _
from slc.quickchangenote.interfaces import IQuickChangenoteLayer

def isVersionable(ob):
    try:
        pr = getToolByName(ob, 'portal_repository')
    except AttributeError:
        return None
    return pr.isVersionable(ob)

def supportsAutoVersion(ob):
    pr = getToolByName(ob, 'portal_repository')
    return pr.supportsPolicy(ob, 'at_edit_autoversion')

class ValidateChangenote(object):
    """ Validate that the user has provided a change note. """
    implements(IObjectPostValidation)
    adapts(IBaseContent)
    field_name = 'cmfeditions_version_comment'

    def __init__(self, context):
        self.context = context

    def __call__(self, request):
        if not IQuickChangenoteLayer.providedBy(request):
            return

        # Archetypes will call us three times, and that complicates things.
        # Either the change note is there or it isn't. If its there the first
        # time, its not about to disappear during the processing of the
        # request. Therefore annotate the return value on the request.
        cache_key = "validate_changenote_result"
        _marker = object()
        cache = IAnnotations(request)
        data = cache.get(cache_key, _marker)
        if data is not _marker:
            return data

        context = aq_inner(self.context)
        if IQuickChangenoteLayer.providedBy(request) and \
            changenoteRequired(context) and isVersionable(context) and \
            supportsAutoVersion(context):
                
            value = request.form.get(self.field_name,
                request.get(self.field_name, ''))
            if len(value) == 0:
                errors = {self.field_name: _(
                    u'A change note must be provided')}
                cache[cache_key] = errors
                return errors
        cache[cache_key] = None
        return None
