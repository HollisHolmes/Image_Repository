from django.test import TestCase
from .models import Item
from django.contrib.auth.models import User

# Create your tests here.
good_img_url1 = 'https://images.theconversation.com/files/350865/original/file-20200803-24-50u91u.jpg?ixlib=rb-1.1.0&rect=37%2C29%2C4955%2C3293&q=45&auto=format&w=926&fit=clip'
good_img_url2 = 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=980:*'
good_img_url3 = 'https://animals.sandiegozoo.org/sites/default/files/2016-11/animals_hero_giraffe_1_0.jpg'
bad_img_url = 'blah'


class ItemTestCase(TestCase):
    def setUp(self):
        # Create Users
        jon = User.objects.create_user(username='jon', password='aSdFgH12345')
        fran = User.objects.create_user(username='fran', password='qAzXsWH09876')
        # Create Items
        cat = Item.objects.create(name='unittest cat',
                                  image_url = good_img_url1,
                                  num_reviews = 1,
                                  price = 23.99,
                                  user = jon)
        dog = Item.objects.create(name='unittest dog',
                                  image_url = good_img_url2,
                                  num_reviews = 2,
                                  price = 22.99,
                                  user = jon)
        cat = Item.objects.create(name='unittest gir',
                                  image_url = good_img_url3,
                                  num_reviews = 3,
                                  price = 21.99,
                                  user = jon)
    def test_inventory_count1(self):
        '''Check foreign key related name ralationship to count number of items a user has'''
        person = User.objects.get(username='jon')
        self.assertEqual(person.inventory.count(), 3)

    def test_inventory_count2(self):
        '''Check foreign key related name ralationship to count number of items a user has'''
        person = User.objects.get(username='fran')
        self.assertEqual(person.inventory.count(), 0)

    def test_inventory_count3(self):
        '''Invalid user - Check foreign key related name ralationship to count number of items a user has'''
        def bad_func():
            person = User.objects.get(username='steve carell')
        self.assertRaises(User.DoesNotExist, bad_func())

        # login = self.client.login(username='testuser', password='12345')
        #create items
