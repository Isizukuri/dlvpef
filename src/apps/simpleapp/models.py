from __future__ import unicode_literals

from django.db import models


class Feedback(models.Model):

    """Feedback Model"""

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=(u"Full Name"))

    category = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=(u"Category"))

    subject = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=(u"Subject"))

    text = models.TextField(
        blank=False,
        verbose_name=(u"Text"))

    class Meta(object):
        verbose_name = (u"Feedback")
        verbose_name_plural = (u"Feedbacks")

    def __unicode__(self):
        return u"From:%s Category:%s Subject:%s" % (self.name,
                                                    self.category,
                                                    self.subject)
