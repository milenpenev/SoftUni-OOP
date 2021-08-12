import datetime

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def int2month(self, month):
        month_as_string = datetime.date(1900, int(month), 1).strftime("%B")
        return month_as_string

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date = date.split(".")
        return cls(id, name, date[2], date[1], age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {status}"
