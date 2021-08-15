class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_worker_is_init_correctly(self):
        # Assert
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy, msg= "Energy should be equal to the energy on init")
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_increased_after_rest(self):
        self.assertEqual(10, self.worker.energy)
        # Act
        self.worker.rest()
        # Assert
        self.assertEqual(11, self.worker.energy)

    def test_worker_works_with_negative_energy_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)
        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()
        # Assert
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_worker_money_is_increased_after_work(self):

        self.assertEqual(0, self.worker.money)
        # Act
        self.worker.work()

        # Assert
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_is_decreased_after_work(self):
        self.assertEqual(0, self.worker.money)
        # Act
        self.worker.work()
        # Assert
        self.assertEqual(9, self.worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 100, 10)
        actual_result = worker.get_info()
        expected_result = "Test has saved 0 money."
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()