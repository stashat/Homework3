class Article():
    def __init__(self):
        self.__title = None
        self.__author = None
        self.__description = None
        self.__category = None
        self.__views = 0
        self.__comments = []

# title
    @property
    def title(self):  
        return self.__title

    @title.setter
    def title(self, value):
        if all(letter.isalpha() or letter.isspace() for letter in str(value)) and len(str(value))<50:
            self.__title = value
        else:
            print('title greska: samo alfabetski karakteri, unique, do 50')

    # author
    @property
    def author(self):  
        return self.__author

    @author.setter
    def author(self, value):
        if all(letter.isalpha() or letter.isspace() for letter in str(value)) and len(str(value))<100 and ' ' in str(value):
            self.__author = value
        else:
            print('author greska: samo alfabetski karakteri, ime i prezime autora, ne duže od 100 karaktera ukupno')

    #description
    @property
    def description(self):  
        return self.__description

    @description.setter
    def description(self, value):
        if len(value)<300:
            self.__description = value
        else:
            print('descripton greska: opis, do 300 karaktera')

    # category
    @property
    def category(self):  
        return self.__category

    @category.setter
    def category(self, value):
        if len(str(value))<20:
            self.__category = value
        else:
            print('kategorija, ne više od 20 karaktera')
        
    # views 
    @property
    def views(self):  
        return self.__views

    @views.setter
    def views(self, value):
        if type(value) == int:
            self.__views = value
        else:
            print('views greska: broj pregleda, default = 0')

    # comments
    @property
    def comments(self):  
        return self.__comments

    def insert_new_comment(self, title, author, description):
        if len(str(title)) < 50:
            valid = True
        else:
            valid = False
            print('title greska: dužina stringa ne veća od 50 karaktera')
        if len(str(author)) < 50:
            valid = True
        else:
            valid = False
            print('author greska: dužina stringa ne veća od 50 karaktera')
        if str(author) == '':
            author = 'anonim'
        if len(str(description)) < 120:
            valid = True
        else:
            valid = False
            print('description greska: dužina stringa ne veća od 120 karaktera')
        comment_titles = []
        for comment in self.__comments:
            comment_titles.append(comment[0])
        if title in comment_titles:
            print('title nije unique')
            valid = False
        else:
            valid = True
        if valid:
            self.__comments.append((title,author,description))
        
    def delete_comment_by_title(self, title):
        new_comments = []
        for comment in self.__comments:
            if title != comment[0]:
                new_comments.append(comment)
        self.__comments = new_comments
    
    def delete_comments_by_author(self, author):
        new_comments = []
        for comment in self.__comments:
            if author != comment[1]:
                new_comments.append(comment)
        self.__comments = new_comments

    def get_comment_by_title(self, title):
        for comment in self.__comments:
            if title == comment[0]:
                # return { title : [comment[1], comment[2]] }
                return '{ ' + title + ' : [' + comment[1] + ', ' + comment[2] + '] }'

    def get_comments_by_author(self, author):
        new_comments = []
        for comment in self.__comments:
            if author == comment[1]:
                new_comments.append(comment)
        return new_comments
    
    def inc_views(self, num=1):
        if type(num) == str:
            print('views mora da bude int')
        else:
            self.__views += num

    def __str__(self):
        return "title: " + str(self.__title) + \
            ", author: " + str(self.__author) + \
            ", description: " + str(self.__description) + \
            ", category: " + str(self.__category) + \
            ", views: " + str(self.__views) + \
            ", number_of_comments: " + str(len(self.__comments))