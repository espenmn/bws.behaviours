# -*- coding: utf-8 -*-

from bws.behaviours import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider

#Needed for the datagrid fields
from plone.autoform.directives import widget

#DataGridStuff
from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield import DictRow

class ITableColumns(Interface):
    """ Fields to be used with DataGridField below
    """

    label = schema.TextLine(
        title=_(u'Label'),
        description=_(u'Label Name'),
        required=False,
    )

    information = schema.TextLine(
        title=_(u'Info'),
        description=_(u'Information'),
        required=False,
    )


class ISimpleNoteTableMarker(Interface):
    pass

@provider(IFormFieldProvider)
class ISimpleNoteTable(model.Schema):
    """
    """

    widget(simple_group=DataGridFieldFactory)
    simple_group = schema.List(title=u"Table fields",
        value_type=DictRow(title=u"Note Table Fields", schema=ITableColumns),
        required=False,
    )


# Note        
# It might not be possible to use setter with all type of (datagrid) fields

@implementer(ISimpleNoteTable)
@adapter(ISimpleNoteTableMarker)
class SimpleNoteTable(object):
    def __init__(self, context):
        self.context = context

    @property
    def simple_group(self):
        if hasattr(self.context, 'simple_group'):
            return self.context.simple_group
        return None

    @simple_group.setter
    def simple_group(self, value):
        self.context.simple_group = value
        

