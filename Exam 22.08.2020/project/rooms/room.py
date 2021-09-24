class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum(el.cost for seq in args for el in seq)


    @property
    def cost(self):
     return self.expenses * 30 + self.room_cost

    def __str__(self):
        return "\n".join([
            f"{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.cost:.2f}$"
        ]+[
           f"--- Child {n+1} monthly cost: {c.get_montly_expense():.2f}" for n, c in enumerate(self.children)
        ]+[
            f"--- Appliances monthly cost: {sum(app.get_monthly_expense() for app in self.appliances):.2f}"
        ])