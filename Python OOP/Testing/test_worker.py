from unittest import TestCase

from Testing.worker import Worker


class TestWorker(TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 1

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when__valid_props_expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(Worker.INITIAL_MONEY, self.worker.money)


    def test__rest__expect__energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)


    def test__work__when_energy_is_0__expect_to_raise(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertIsNotNone(ex)

    def test__work_when_enough_energy__expect_salary_to_be_increased(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2 * self.SALARY, self.worker.salary)


    def test__work__when__enough_energy_to_decrement(self):
        self.worker.work()

        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__get__info__expect_correct__result(self):
        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {0} money.'

