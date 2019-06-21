from zad1 import Article
from zad2 import TechArticle


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

categories = ['mystery', 'drama', 'action', 'crime', 'adventure', 'tech']
article_list = []
###############################################################################
article = Article()
article.title = 'titleA'
article.author = 'author A'
article.description = 'description 1'
article.views = 1
article.category = 'action'
article_list.append(article)

article = Article()
article.title = 'titleB'
article.author = 'author B'
article.description = 'description 2'
article.views = 2
article.category = 'mystery'
article_list.append(article)

article = Article()
article.title = 'titleC'
article.author = 'author C'
article.description = 'description 3'
article.views = 3
article.category = 'mystery'
article_list.append(article)

article = Article()
article.title = 'titleD'
article.author = 'author D'
article.description = 'description 4'
article.views = 4
article.category = 'action'
article_list.append(article)

article = TechArticle()
article.title = 'titleE'
article.author = 'author E'
article.description = 'description 5'
article.views = 5
article.creation_date = '2/4/2013'
article.lang = 'en'
article_list.append(article)

article = TechArticle()
article.title = 'titleF'
article.author = 'author F'
article.description = 'description 6'
article.views = 6
article.creation_date = '4/5/1999'
article.lang = 'rs'
article_list.append(article)


##############################################################################

while True:
    izbor = input('-------------------------------------------------------- \n'
                  'izaberi: \n'
                  '1 - unos atricle \n'
                  '2 - unos tech atricle \n'
                  '3 - dodavanje komentara \n'
                  '4 - filterisanje po kategoriji \n'
                  '10 - kraj \n')
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
                article.insert_new_comment(input('unesite naslov: '), input('unosite autora: '), input('unesite opis: '))
                print(article.comments)
    if izbor == '4':
        filtered_articles = []
        category_filter = str(input('Unesite jednu od kategorija ' + str(categories) + ' : '))
        for article in article_list:
            if article.category == category_filter:
                filtered_articles.append(article)
                print(article)
    if izbor == '10':
        break

for article in article_list:
    print(article)
