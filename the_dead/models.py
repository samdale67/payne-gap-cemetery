from django.db import models


class theDead(models.Model):
    last_name = models.CharField('Last Name', max_length=255, blank=False)
    maiden_name = models.CharField('Maiden Name', max_length=255, blank=True)
    first_name = models.CharField('First Name', max_length=255, blank=True)
    nick_name = models.CharField('Nick Name', max_length=255, blank=True)
    birth_date = models.DateField('Birth Date', blank=True)
    death_date = models.DateField('Death Date', blank=True)
    website = models.URLField('Website',
                              max_length=255,
                              blank=True,
                              help_text='Add website describing or providing more information about the '
                                        'person.')
    description = models.TextField('Description', max_length=3000, blank=True)
    # grave_image = models.ForeignKey('GraveImage',
    #                           related_name='collections',
    #                           verbose_name=u'Grave Images',
    #                           on_delete=models.CASCADE,
    #                           blank=True,
    #                           null=True,
    #                           help_text='Upload images showing details of grave or tombstone.')
    grave_location = models.CharField('Grave Coordinate', max_length=255, default='', blank=False)
    monument = models.BooleanField('Monument?', blank=False, help_text="Does the grave include a monument "
                                                                       "or tombstone?")
    date_created = models.DateField(auto_now_add=True)
    date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'The Dead'
        verbose_name_plural = 'The Dead'
        ordering = ['last_name']
