from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Status of a news item, draft or published
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class News(models.Model):
    """
    This model is for a news item
    """
    class Meta:
        ordering = ['-create_date']
        verbose_name = _('News')
        verbose_name_plural = _('News')

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=250,
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news_items'
    )
    news_item_text = models.TextField(
        max_length=500,
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    create_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )

    def __str__(self):
        """
        Return new title string
        """
        return self.title
