# -*- coding: utf-8 -*-
from bws.behaviours.behaviors.simple_note_table import ISimpleNoteTableMarker
from bws.behaviours.testing import BWS_BEHAVIOURS_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class SimpleNoteTableIntegrationTest(unittest.TestCase):

    layer = BWS_BEHAVIOURS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_simple_note_table(self):
        behavior = getUtility(IBehavior, 'bws.behaviours.simple_note_table')
        self.assertEqual(
            behavior.marker,
            ISimpleNoteTableMarker,
        )
