from django.test import TestCase
from hyperlinked_relational_serializer.serializers import HyperLinkedRelationalSerializer
from rest_framework.serializers import Serializer, CharField, HyperlinkedModelSerializer, ModelSerializer
from hyperlinked_relational_serializer.hl_relational_serializer_tests.models import Vegetable, Meal
from rest_framework.compat import patterns, url
from django.test.client import RequestFactory
from rest_framework import serializers


factory = RequestFactory()
request = factory.get('/') 


def fake_view(request):
    pass


urlpatterns = patterns('',
    url(r'^vegetable/$', fake_view, name = 'vegetable-list'),
    url(r'^vegetable/(?P<pk>[0-9]+)/$', fake_view, name = 'vegetable-detail'),
    url(r'^meal/$', fake_view, name = 'meal-list'),
    url(r'^meal/(?P<pk>[0-9]+)/$', fake_view, name = 'meal-detail'),
)


class VegetableSerializer(HyperLinkedRelationalSerializer):

    class Meta:
        view_name = "vegetable-detail"
        queryset = Vegetable.objects.all()


class MealSerializer(serializers.HyperlinkedModelSerializer):
    vegetable_set = VegetableSerializer(many=True, required=False)

    class Meta:
        model = Meal
        view_name = "meal-detail"
        queryset = Meal.objects.all()


class TestStuff(TestCase):
    ''' 
        create a fake end point resource that we can link to all it
        needs are the end points
    '''
    urls = "hyperlinked_relational_serializer.hl_relational_serializer_tests.tests"

    def tearDown(self):
        Meal.objects.all().delete()
        Vegetable.objects.all().delete()


    def test_write_to_serializer(self):
        """
            test that we can write to the serializer in the normal manner
        """

        data = {'meal_name': 'hamburger'}
        meal_serializer = MealSerializer(data=data)
        self.assertTrue(meal_serializer.is_valid())
        meal_serializer.save()
        self.assertTrue(Meal.objects.all().count(), 1)
        self.assertEqual(Meal.objects.all()[0].meal_name, 'hamburger')


    def test_read_from_serializer(self):
        """
            tests that we an do a straight read from the serializer
        """
        Meal.objects.create(meal_name="cheese burger")
        object_list = Meal.objects.all()
        o_list = [{"meal_name": "cheese burger", 'url': '/meal/1/', 'vegetable_set': []}]
        serializer = MealSerializer(object_list, many=True)
        data = serializer.data
        self.assertListEqual(data, o_list)


    def test_update_from_serializer(self):
        Meal.objects.create(meal_name="vege burger")
        data = {"meal_name": "mushroom burger"}
        serializer = MealSerializer(Meal.objects.all()[0], data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        obj = serializer.save()
        self.assertEqual(len(Meal.objects.all()), 1)
        self.assertEqual(obj.meal_name, "mushroom burger")
        self.assertEqual(Meal.objects.all()[0].meal_name, "mushroom burger")


    def test_read_as_foreign_key(self):
        quiche = Meal.objects.create(meal_name = "spinach quiche")
        salad = Meal.objects.create(meal_name = "salad")
        spinach = Vegetable.objects.create(vegetable_name="spinach", meal=quiche)
        lettuce = Vegetable.objects.create(vegetable_name="lettuce", meal=salad)
        read_serializer = MealSerializer(Meal.objects.all())
        aimed_data = [
            {
            'vegetable_set': 
                [
                    {u'url': '/vegetable/1/', 'meal': '/meal/1/', 'vegetable_name': u'spinach'}
                ], 
            u'url': '/meal/1/', 
            'meal_name': u'spinach quiche'
            }, 
            {
            'vegetable_set': 
                [
                    {u'url': '/vegetable/2/', 'meal': '/meal/2/', 'vegetable_name': u'lettuce'}
                ], 
            u'url': '/meal/2/', 'meal_name': u'salad'
            }
        ]

        self.assertListEqual(read_serializer.data, aimed_data)


    def test_write_as_link(self):
        quiche = Meal.objects.create(meal_name = "quiche")
        salad = Meal.objects.create(meal_name = "salad")
        spinach = Vegetable.objects.create(vegetable_name="spinach", meal=quiche)
        lettuce = Vegetable.objects.create(vegetable_name="lettuce", meal=salad)

        #move the lettuce into the quiche
        quiche_data = {
                "meal_name": "quiche",
                "vegetable_set": ['/vegetable/2/'],
                "partial": True
        }

        write_serializer = MealSerializer(Meal.objects.get(meal_name="quiche"), data=quiche_data)
        self.assertTrue(write_serializer.is_valid())
        write_serializer.save()
        self.assertTrue(Vegetable.objects.all().count(), 2)
        self.assertTrue(Meal.objects.all().count(), 2)
        spinach = Vegetable.objects.get(vegetable_name="spinach")
        self.assertEqual(spinach.meal.id, 1)
        lettuce = Vegetable.objects.get(vegetable_name="lettuce")
        self.assertEqual(lettuce.meal.id, 1)




























