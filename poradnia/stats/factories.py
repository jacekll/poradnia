# coding=utf-8
import factory.fuzzy
import factory
import pytz
from django.utils.datetime_safe import datetime
from pytz import timezone


class ItemFactory(factory.django.DjangoModelFactory):
    key = factory.Sequence("item-key-{0}".format)
    name = factory.Sequence("item-name-{0}".format)
    description = factory.fuzzy.FuzzyText()
    last_updated = factory.fuzzy.FuzzyDateTime(datetime(2008, 1, 1, tzinfo=pytz.utc))
    public = factory.Sequence(lambda n: n % 2 == 0)

    class Meta:
        model = 'stats.Item'


class ValueFactory(factory.django.DjangoModelFactory):
    item = factory.SubFactory("poradnia.stats.tests.factories.ItemFactory")
    time = factory.fuzzy.FuzzyDateTime(datetime(2008, 1, 1, tzinfo=pytz.utc))
    value = factory.Sequence(lambda n: n*n)
    comment = factory.Sequence("value-comment-{0}".format)

    class Meta:
        model = 'stats.Value'
