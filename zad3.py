from zad1 import Article
from zad2 import TechArticle

article_list = []
# new_techarticle = TechArticle()
# article_list.append(new_article)
# article_list.append(new_techarticle)
# article_list[0].title = 'titleA'
# print(article_list[0])
# print(new_article)

# new_article.title = input('Unesi title: ')
# new_article.author = input('Unesi autora: ')
# new_article.description = input('Unesi opis: ')
# new_article.category = input('Unesi kategoriju: ')
# new_article.views = int(input('Unesi preglede: '))
# new_article.insert_new_comment(input('Unesi title komentara: '), 
#                                input('Unesi autora komentara: '),
#                                input('Unesi opis komentara: ') )
# print(new_article)
def input_articles():
    new_article = Article()
    while True:
        try:
            new_article.title = input('unesi article title: ')
            break
        except ValueError as err:
            print(err)
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
            new_article.category = input('unesi article category: ')
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
            new_article.insert_new_comment(input('comment title: '),
                                        input('comment author: '),
                                        input('comment description: '))
            break
        except ValueError as err:
            print(err)
    return new_article

# vraceni_article = input_articles()
# print(vraceni_article)
# article_list.append(vraceni_article)
# print(article_list)

# vraceni_article = input_articles()
# print(vraceni_article)
# article_list.append(vraceni_article)
# print(article_list)

while True:
    izbor = input('-------------------------------------------------------- \n'
                  'izaberi: \n'
                  '1 - za unos atricle \n'
                  '2 - za kraj \n')
    if izbor == '1':
        vraceni_article = input_articles()
        article_list.append(vraceni_article)
    if izbor == '2':
        break
print(article_list)
