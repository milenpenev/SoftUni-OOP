class PhotoAlbum:
    def __init__(self, pages):
        self.pages = int(pages)
        self.photos = [[] for _ in range(pages)]
        self.page_capacity = 4
        self.page_index = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = int(photos_count) // 4
        return cls(pages)

    def is_there_place(self):
        return self.page_index < self.pages and len(self.photos[self.page_index]) < 4

    def new_page(self):
        if len(self.photos[self.page_index]) == 4:
            self.page_index += 1
        return self.page_index

    def add_photo(self, label):
        if not self.is_there_place():
            return f"No more free slots"
        self.photos[self.page_index].append(label)
        page_added = f"{label} photo added successfully on page {self.page_index + 1} slot {len(self.photos[self.page_index])}"
        self.new_page()
        return page_added

    def display(self):
        display = f"-----------"
        for _ in self.photos:
            display += "\n"
            if _:

                display += ''.join('[] ' for p in range(len(_))).strip()
            display += "\n"
            display += f"-----------"
        return display


