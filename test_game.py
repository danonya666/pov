from unittest import TestCase

from one import Game, Person, POWER, Choice


class TestPerson(TestCase):
    def setUp(self):
        self.person = Person('test')


class TestInit(TestPerson):
    def test_initial_hp(self):
        self.assertEqual(self.person.hp, 100)

    def test_initial_power(self):
        self.assertEqual(self.person.power, POWER)

    def test_initial_name(self):
        self.assertEqual(self.person.name, 'test')


class TestFighting(TestPerson):
    other_person = Person('test2')

    def test_hit(self):
        other_person_hp = self.other_person.hp
        self.person.hit(self.other_person)
        self.assertEqual(other_person_hp - POWER, self.other_person.hp)

    def test_rps(self):
        result = self.person.rps('r')
        self.assertEqual(result, Choice.rock)
