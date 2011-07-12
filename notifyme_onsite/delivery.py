#-*- coding: utf-8 -*-
from notifyme.delivery.base import BaseDeliveryBackend
from django.template.loader import render_to_string
from notifyme_onsite.models import OnsiteNotice

class OnsiteStickyBackend(BaseDeliveryBackend):
    identifier = 'onsite_sticky'

    def deliver_to(self, user, context, notice, language):
        from pprint import pprint
        pprint(context)
        expires_at = notice.options.get('expires_at', None)
        body_html = render_to_string(
            (
                "notifyme/notices/%s/onsite/sticky.html" % notice.identifier,
                "notifyme/notices/generic/onsite/sticky.html",
            ),
            context_instance=context
        )
        OnsiteNotice(
            user=user,
            expires_at=expires_at,
            notice_type=notice.identifier,
            sticky_body_html=body_html,
        ).save()
