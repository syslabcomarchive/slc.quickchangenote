from zope.schema import List, TextLine, Bool
from zope.interface import Interface
from slc.quickchangenote import MessageFactory as _

class IQuickChangenoteLayer(Interface):
    """Marker Interface used by as BrowserLayer
    """

class IQuickChangenoteSettings(Interface):
    """ Interface class that describes settings for plone.app.registry. """
    notes = List(
            title=_(u"Change notes"),
            description=_(u"Define commonly used changenote text here, one "
                    "per line."),
            required=False,
            value_type=TextLine(title=_(u"Changenote")))
    required = Bool(
            title=_(u"Change note is required"),
            description=_(u"Select this if you want to make change notes "
                u"required."),
            required=True, default=False)
    required_on_new = Bool(
            title=_(u"Change note is required for new content"),
            description=_(u"Select this if change notes are required "
            "when creating new content. This has no effect if the above "
            "setting is disabled."),
            required=True, default=False)
