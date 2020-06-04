
from collective.easyform.browser.actions import get_actions
from collective.easyform.browser.actions import getFieldsInOrder
from collective.easyform.browser.actions import EasyFormActionsView
from collective.easyform.browser.actions import ISavedDataFormWrapper
from collective.easyform.browser.actions import SavedDataView
from collective.easyform.browser.actions import SavedDataForm
from collective.easyform.browser.actions import ViewPageTemplateFile
from plone import api
from plone.z3cform import layout
from zope.interface import implementer
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five import BrowserView

# from collective.easyformplugin.poll.interfaces import IPoll
# from collective.easyformplugin.poll.interfaces import IPollSaveData


class PollSavedDataView(SavedDataView):
    """View for Saved Polls"""
    # def items(self):
    #     actionlist = [
    #         (name, action.__doc__)
    #         for name, action in getFieldsInOrder(get_actions(self.context))
    #         if IPollSaveData.providedBy(action)
    #     ]
    #     return actionlist


# class PollDataForm(SavedDataForm):
#     """View for Saved Poll Form"""
#     template = ViewPageTemplateFile("saveddata_form.pt")


# @implementer(ISavedDataFormWrapper)
# class PollDataFormWrapper(layout.FormWrapper):
#     def __call__(self):
#         if hasattr(self.request, "form.buttons.download"):
#             self.context.field.download(self.request.response)
#             return u""
#         else:
#             return super(PollDataFormWrapper, self).__call__()


# ActionPollDataView = layout.wrap_form(
#     PollDataForm, __wrapper_class=PollDataFormWrapper
# )
class ActionPollDataView(BrowserView):
    template = ViewPageTemplateFile("poll.pt")

    def render(self):
        return self.template()

    def __call__(self):
        self.form_url = self.context.aq_parent.aq_parent.absolute_url()
        if not self.context.field.showToAnonymousUsers:
            if api.user.is_anonymous():
                return self.request.RESPONSE.redirect(self.form_url)
        elif not self.context.field.showToAuthUsers:
            if not api.user.has_permission('cmf.ModifyPortalContent'):
                return self.request.RESPONSE.redirect(self.form_url)
        return self.render()


class PollEasyFormActionsView(EasyFormActionsView):
    """View for Saved Poll"""