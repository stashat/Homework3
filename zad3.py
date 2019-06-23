from zad1 import Article
from zad2 import TechArticle
import os

###############################################################################
# funkcija za unosenje artikala
def input_articles():
    new_article = Article()
    while True:
        title = input('unesi article title: ')
        if title not in article_titles(article_list):
            try:
                new_article.title = title
                break
            except ValueError as err:
                print(err)
        else: 
            print('Title "' + title +'" vec postoji, unijeti opet!')
    while True:
        try:
            new_article.author = input('unesi article author: ')
            break
        except ValueError as err:
            print(err)
    while True:
        try:
            new_article.description = input('unesi article description: ')
            break
        except ValueError as err:
            print(err)
    while True:
        category = input('unesi neku od kategorija, ' + str(categories) + ' :')
        if category in categories:
            try:
                new_article.category = category
                break
            except ValueError as err:
                print(err)
        else:
            print('nepostojeca kategorija')
    while True:
        try:
            new_article.views = int(input('unesi article views: '))
            break
        except ValueError as err:
            print(err)
    return new_article

###############################################################################
# funkcija za unosenje techarticle
def input_tech_articles():
    new_article = TechArticle()
    while True:
        title = input('unesi tech article title: ')
        if title not in article_titles(article_list):
            try:
                new_article.title = title
                break
            except ValueError as err:
                print(err)
        else: 
            print('Title "' + title +'" vec postoji, unijeti opet!')
    while True:
        try:
            new_article.author = input('unesi article author: ')
            break
        except ValueError as err:
            print(err)
    while True:
        try:
            new_article.description = input('unesi article description: ')
            break
        except ValueError as err:
            print(err)
    while True:
        try:
            new_article.views = int(input('unesi article views: '))
            break
        except ValueError as err:
            print(err)
    while True:
        try:
            new_article.creation_date = input('unesi creation date u obliku d/m/y: ')
            break
        except ValueError as err:
            print(err)
    while True:
        try:
            new_article.lang = input('unesi language en ili rs: ')
            break
        except ValueError as err:
            print(err)
    
    return new_article

def article_titles(article_list_p):
    list_titles = []
    for article in article_list_p:
        list_titles.append(article.title)
    return list_titles

###############################################################################
# definisanje konstanti i promjenljivih
categories = ['mystery', 'drama', 'action', 'crime', 'adventure', 'tech']
article_list = []
category_filter = ""

###############################################################################
# unosenje atricles za testiranje
article = Article()
article.title = 'titleA'
article.author = 'author A'
article.description = 'description 1'
article.views = 378
article.category = 'action'
article.insert_new_comment('titlea', 'autor','1')
article.insert_new_comment('titleb', 'autor','2')
article.insert_new_comment('titlec', 'autor','3')
article.insert_new_comment('titled', 'autor3','3')
article.insert_new_comment('titlee', 'autor','1')
article.insert_new_comment('titlef', 'autor','2')
article.insert_new_comment('titleg', 'autor','3')
article.insert_new_comment('titleh', 'autor3','3')
article.insert_new_comment('titlei', 'autor3','3')
article.insert_new_comment('titlej', 'autor','1')
article_list.append(article)

article = Article()
article.title = 'titleB'
article.author = 'author B'
article.description = 'description 2'
article.views = 237
article.category = 'mystery'
article.insert_new_comment('titlea', 'autor','1')
article.insert_new_comment('titleb', 'autor','2')
article.insert_new_comment('titlec', 'autor','3')
article.insert_new_comment('titled', 'autor3','3')
article_list.append(article)

article = Article()
article.title = 'titleC'
article.author = 'author C'
article.description = 'description 3'
article.views = 878
article.category = 'mystery'
article.insert_new_comment('titlea', 'autor','1')
article.insert_new_comment('titleb', 'autor','2')
article.insert_new_comment('titlec', 'autor','3')
article.insert_new_comment('titled', 'autor3','3')
article.insert_new_comment('titlee', 'autor3','3')
article.insert_new_comment('titlef', 'autor','1')
article.insert_new_comment('titleg', 'autor','1')
article.insert_new_comment('titleh', 'autor','2')
article.insert_new_comment('titlei', 'autor','3')
article.insert_new_comment('titlej', 'autor3','3')
article.insert_new_comment('titlek', 'autor3','3')
article.insert_new_comment('titlel', 'autor','1')
article_list.append(article)

article = Article()
article.title = 'titleD'
article.author = 'author D'
article.description = 'description 4'
article.views = 764
article.category = 'action'
article.insert_new_comment('titlea', 'autor','1')
article.insert_new_comment('titleb', 'autor','2')
article_list.append(article)

article = TechArticle()
article.title = 'titleE'
article.author = 'author E'
article.description = 'description 5'
article.views = 333
article.creation_date = '2/4/2013'
article.lang = 'en'
article.insert_new_comment('titlea', 'autor','1')
article.insert_new_comment('titleb', 'autor','2')
article.insert_new_comment('titlec', 'autor','3')
article.insert_new_comment('titled', 'autor3','3')
article.insert_new_comment('titlee', 'autor3','3')
article.insert_new_comment('titlef', 'autor','1')
article.insert_new_comment('titleg', 'autor','2')
article.insert_new_comment('titleh', 'autor','3')
article.insert_new_comment('titlei', 'autor3','3')
article.insert_new_comment('titlej', 'autor3','3')
article_list.append(article)

article = TechArticle()
article.title = 'titleF'
article.author = 'author F'
article.description = 'description 6'
article.views = 6
article.creation_date = '4/5/1999'
article.lang = 'rs'
article.insert_new_comment('titlea', 'autor','1')
article.insert_new_comment('titleb', 'autor','2')
article.insert_new_comment('titlec', 'autor','3')
article.insert_new_comment('titled', 'autor3','3')
article.insert_new_comment('titlee', 'autor3','3')
article.insert_new_comment('titlef', 'autor3','3')
article_list.append(article)


##############################################################################
# UI
while True:
    izbor = input('-------------------------------------------------------- \n'
                  'izaberi: \n'
                  '1 - unos atricle \n'
                  '2 - unos tech atricle \n'
                  '3 - dodavanje komentara \n'
                  '4 - filterisanje po kategoriji \n'
                  '5 - kraj \n')
    if izbor == '1':
        new_article = input_articles()
        article_list.append(new_article)
    if izbor == '2':
        new_article = input_tech_articles()                       
        article_list.append(new_article)
    if izbor == '3':
        print('postojeci titlovi: ', article_titles(article_list))
        insert_comment_by_title = input('unesite title artikla: ')
        for article in article_list:
            if article.title == insert_comment_by_title:
                article.insert_new_comment(input('unesite naslov: '),
                                           input('unosite autora: '),
                                           input('unesite opis: '))
                print(article.comments)
    if izbor == '4':
        categories_sorted_by_views = []
        categories_sorted_by_num_com = []
        filtered_articles = []
        category_filter = str(input('Unesite jednu od kategorija ' +\
                              str(categories) + ' : '))
        for article in article_list:
            if article.category == category_filter:
                filtered_articles.append(article)
                print(article)
        categories_sorted_by_views = sorted(filtered_articles, 
                                            key = lambda article: article.views,
                                            reverse = True)
        categories_sorted_by_num_com = sorted(filtered_articles,
                                              key = lambda article: len(article.comments),
                                              reverse = True)
        # write in file
        file_n = category_filter + "_sorted_by_views.txt"
        file = open(file_n, "w+")
        for article in categories_sorted_by_views:
            articles = "|".join(str(comm) for comm in article.comments)
            file.write(str(article.title) + ';' +\
                       str(article.author) + ';' +\
                       str(article.description) + ';' +\
                       articles + ';' +\
                       str(len(article.comments)) + ';' +\
                       str(article.views) +\
                       '\n')
        file.close()

        # write in file
        file_n = category_filter + "_sorted_by_num_com.txt"
        file = open(file_n, "w+")
        for article in categories_sorted_by_num_com:
            articles = "|".join(str(comm) for comm in article.comments)
            file.write(str(article.title) + ';' +\
                       str(article.author) + ';' +\
                       str(article.description) + ';' +\
                       articles + ';' +\
                       str(len(article.comments)) + ';' +\
                       str(article.views) +\
                       '\n')
        file.close()
    if izbor == '5':
        # if category_filter != "":
            # os.remove(category_filter + "_sorted_by_views.txt")
            # os.remove(category_filter + "_sorted_by_num_com.txt")
        break
