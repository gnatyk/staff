from django.db import models
from model_utils.choices import Choices

from ssm.users.models import User


STATUS = Choices(('new', 'New'), ('approving', 'Approving'), ('approved', 'Approved'))
REASON = Choices(('vacation', 'Vacation'), ('illness', 'Illness'), ('holiday', 'Holiday'), ('other', 'Other'))


class Absence(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    reason = models.CharField('Reason', max_length=32, choices=REASON, default=REASON.other)
    status = models.CharField('Status', max_length=32, choices=STATUS, default=STATUS.new)
    approved_by = models.ForeignKey(User, related_name='approved_by', null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
    notes = models.TextField('Notes', null=True, blank=True)

    def __str__(self):
        return '%s (absences %s)' % (self.id, self.user.id if self.user else 'unknown')

    class Meta:
        app_label = 'absences'
        verbose_name_plural = 'Absences'
        ordering = ['-id']
