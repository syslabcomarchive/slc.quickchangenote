# -*- coding: utf-8 -*-
from zope.component import getUtility
from slc.quickchangenote.interfaces import IQuickChangenoteSettings

def getSettings():
    registry = getUtility(IQuickChangenoteSettings)
    if registry is None:
        return None
    return registry

def changenoteRequired(context):
    """ returns whether a change note is required on each save. """
    settings = getSettings()
    if settings is None:
        # Default behaviour is also plone default, it is not required
        return False
    if getattr(context, 'isTemporary', lambda: False)():
        return settings.required and settings.required_on_new
    return settings.required
