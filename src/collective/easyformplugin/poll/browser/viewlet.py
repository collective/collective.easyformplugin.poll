from plone import api
from plone.app.layout.viewlets import common as base
from zope.annotation.interfaces import IAnnotations

from collective.easyformplugin.poll import _
from collective.easyformplugin.poll import CEFPSS,  CEFPSV


class PollEasyFormViewlet(base.ViewletBase):
    
    
    def allowSingleSubmission(self):
        try:
            if not api.user.is_anonymous():
                if self.context.Type() == 'EasyForm':
                    annotations = IAnnotations(self.context)
                    singleSubmission = annotations.get(CEFPSS, False)
                    
                    voters = annotations.get(CEFPSV, [])
                    auth_user = api.user.get_current()
                    if singleSubmission and auth_user.id in voters:
                        return True
                    
        except:
            return False
        return False
    