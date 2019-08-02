from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Rating,Project
from django.test import TestCase


# Create your tests here.
class Projects_TestCases(TestCase):
    def setup(self):
        self.user_me = User(id=1,username='Haggray',email='haggray@test.com',password='chepngetich')
        self.user_me.save()
        self.me_profile = Profile(user=self.user_me, bio='my name is haggray',
                                  profile_pic='/media/fashion1.jpg', contact='1234567')
        self.me_profile.save()
        self.my_project = Project(id=1, user=self.user_me, profile=self.me_profile, sitename='parlor',
                                  screenshot='/media/parlor.jpg', link='https://www.wynnpalace.com/en/rooms-n-suites/parlor-suite', technologies='business')
        self.my_project.save()
        self.the_review = Review(
            id=1, project=self.my_project, user=self.user_me, text='')
        self.the_review.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()
        Review.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user_me, User))
        self.assertTrue(isinstance(self.me_profile, Profile))
        self.assertTrue(isinstance(self.my_project, Project))
        self.assertTrue(isinstance(self.the_review, Review))

    def test_delete_method(self):
        self.my_project.save_project()
        object = Project.objects.filter(id=1)
        Project.delete_project(object)
        all_objects = Project.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_get_project_by_id(self):
        self.my_project.save_project()
        project = Project.get_project_by_id(1)
        self.assertEqual(project.id, 1)

    def test_update_project(self):
        self.my_project.save_project()
        filtered_object = Project.update_project('muk', 'Greener')
        updated = Project.objects.get(name='Greener')
        self.assertEqual(updated.name, 'Greener')

    def test_search_by_name(self, search_term):
        self.project.save_project()
        got_project = Project.objects.get(sitename=search_term)
        self.assertTrue(got_project.sitename == 'pigdice')
