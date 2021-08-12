from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        for cat in self.categories:
            if cat.id == category_id:
                cat.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for top in self.topics:
            if top.id == topic_id:
                top.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for doc in self.documents:
            if doc.id == document_id:
                doc.edit(new_file_name)

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                self.categories.remove(cat)

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                self.topics.remove(top)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += repr(doc)
            result += "\n"

        return result