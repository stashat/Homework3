from zad1 import Article
from datetime import datetime

class TechArticle(Article):
    def __init__(self):
        super().__init__()
        self.__creation_date = None
        self.__lang = None
        self.category = 'tech'
    
    # creation date
    @property
    def creation_date(self):  
        return self.__creation_date.strftime('%d/%m/%Y')

    @creation_date.setter
    def creation_date(self, value):
        try:
            date = datetime.strptime(value, '%d/%m/%Y').date()
            self.__creation_date = date
        except ValueError as err:
            print('creation date greska: string treba da bude oblika d/m/y; ', err)

    # lang
    @property
    def lang(self):  
        return self.__lang

    @lang.setter
    def lang(self, value):
        if str(value) == 'en' or str(value) == 'rs':
            self.__lang = value
        else:
            print('language greska: dozvoljene vrijednosti su en i rs')
    
    def get_comments_by_term(self, term):
        comments_term = []
        for comment in self.comments:
            if term == comment[0][:len(term)]:
                comments_term.append(comment)
        return comments_term

    def __str__(self):
        return "title: " + str(self.title) + \
            ", author: " + str(self.author) + \
            ", description: " + str(self.description) + \
            ", category: " + str(self.category) + \
            ", views: " + str(self.views) + \
            ", number_of_comments: " + str(len(self.comments)) + \
            ", creation_date: " + str(self.creation_date) + \
            ", language: " + str(self.lang)



