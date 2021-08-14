from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return False
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return False
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return False
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return False
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return False
        self.subscriptions.append(subscription)

    @staticmethod
    def get_object(oid, cl_iterable):
        return list(filter(lambda _: _.id == oid, cl_iterable))[0]

    def subscription_info(self, subscription_id):
        current_subscription = self.get_object(subscription_id, self.subscriptions)
        customer_id = current_subscription.customer_id
        trainer_id = current_subscription.trainer_id
        current_customer = self.get_object(customer_id, self.customers)
        current_trainer = self.get_object(trainer_id, self.trainers)
        current_plan = self.get_object(trainer_id, self.plans)
        current_equipment = self.get_object(current_plan.equipment_id, self.equipment)
        return f"{current_subscription}\n{current_customer}\n{current_trainer}\n{current_equipment}\n{current_plan}"