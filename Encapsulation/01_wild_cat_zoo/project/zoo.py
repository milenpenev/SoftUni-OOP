from project.tiger import Tiger
from project.cheetah import Cheetah
from project.lion import Lion
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        if len(self.animals) < self.__animal_capacity and self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_for_care = sum(map(lambda animal: animal.money_for_care, self.animals))
        if total_money_for_care <= self.__budget:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        total_lions = 0
        lions_info = []
        total_tigers = 0
        tigers_info = []
        total_cheetahs = 0
        cheetahs_info = []
        for animal in self.animals:
            if type(animal) == Lion:
                total_lions += 1
                lions_info.append(repr(animal))
            elif type(animal) == Tiger:
                total_tigers += 1
                tigers_info.append(repr(animal))
            elif type(animal) == Cheetah:
                total_cheetahs += 1
                cheetahs_info.append(repr(animal))
        result += f"----- {total_lions} Lions:\n"
        lions_result = '\n'.join(lions_info)
        result += lions_result + '\n'
        result += f'----- {total_tigers} Tigers:\n'
        tigers_result = '\n'.join(tigers_info)
        result += tigers_result + '\n'
        result += f'----- {total_cheetahs} Cheetahs:\n'
        cheetahs_result = '\n'.join(cheetahs_info)
        result += cheetahs_result
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        total_keepers = 0
        keepers_info = []
        total_caretakers = 0
        caretakers_info = []
        total_vets = 0
        vets_info = []
        for worker in self.workers:
            if type(worker) == Keeper:
                total_keepers += 1
                keepers_info.append(repr(worker))
            elif type(worker) == Caretaker:
                total_caretakers += 1
                caretakers_info.append(repr(worker))
            elif type(worker) == Vet:
                total_vets += 1
                vets_info.append(repr(worker))
        result += f"----- {total_keepers} Keepers:\n"
        keepers_result = '\n'.join(keepers_info)
        result += keepers_result + '\n'
        result += f'----- {total_caretakers} Caretakers:\n'
        caretakers_result = '\n'.join(caretakers_info)
        result += caretakers_result + '\n'
        result += f'----- {total_vets} Vets:\n'
        vets_result = '\n'.join(vets_info)
        result += vets_result
        return result