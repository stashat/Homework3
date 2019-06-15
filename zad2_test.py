from zad2 import TechArticle

test2 = TechArticle()
test2.title = 'title'
print('test 1: ', test2.title)
test2.creation_date = '6/5/2019'
print('test 2: ',test2.creation_date)
test2.creation_date = '65/5/2019'
print('test 3: ',test2.creation_date)
test2.lang = 'rs'
print('test 4: ',test2.lang)
test2.lang = 'drikrok4'
print('test 5: ',test2.lang)
test2.insert_new_comment('naslova', 'autor','1')
test2.insert_new_comment('naslovb', 'autor','2')
test2.insert_new_comment('titlec', 'autor','3')
test2.insert_new_comment('title4', 'autor3','3')
test2.insert_new_comment('title5', 'autor3','3')
test2.insert_new_comment('title6', 'autor3','3')
print('test 6: ', test2.get_comments_by_term('na'))
print('test 7: ', test2)
