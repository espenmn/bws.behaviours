# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bws.behaviours


class BwsBehavioursLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=bws.behaviours)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bws.behaviours:default')


BWS_BEHAVIOURS_FIXTURE = BwsBehavioursLayer()


BWS_BEHAVIOURS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BWS_BEHAVIOURS_FIXTURE,),
    name='BwsBehavioursLayer:IntegrationTesting',
)


BWS_BEHAVIOURS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BWS_BEHAVIOURS_FIXTURE,),
    name='BwsBehavioursLayer:FunctionalTesting',
)


BWS_BEHAVIOURS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BWS_BEHAVIOURS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='BwsBehavioursLayer:AcceptanceTesting',
)
