from django.test import TestCase

# Create your tests here.
from apps.ad.models import Ad
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

class AdTest(TestCase):

    def get_user(self):
        user = User.objects.all().first()
        return user

    def create_user(self, username="usert1"):
        new_user = User.objects.create_user(username=username, password="123456")
        return new_user

    def create_ad(self, author, title="test ad ", body="test ad"):
        return Ad.objects.create(title=title,
                                 body=body,
                                 pub_date=timezone.now(),
                                 author=author
                                 )

    def test_ad_creation(self):
        user = self.create_user()
        ad = self.create_ad(author=user)
        self.assertTrue(isinstance(ad, Ad))
        self.assertEqual(ad.__str__(), ad.title)

    def test_ad_detail_view(self):
        # TODO: How can I be sure the user exits
        user = self.create_user()
        ad = self.create_ad(author=user)
        url = reverse('ad:detail', kwargs={'slug':ad.slug})
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
