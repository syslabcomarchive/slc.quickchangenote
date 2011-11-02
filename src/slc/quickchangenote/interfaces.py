from zope.schema import List
from zope.interface import Interface
from slc.quickchangenote import MessageFactory as _

class IQuickChangenoteLayer(Interface):
    """Marker Interface used by as BrowserLayer
    """

class IQuickChangenoteSettings(Interface):
    """ Interface class that describes settings for plone.app.registry. """
    notes = schema.List(
            title=_(u"Changenotes"),
            description=_(u"Define commonly used changenote text here, one "
                    "per line."),
            required=False,
            value_type=schema.TextLine(title=_(u"Changenote")))
