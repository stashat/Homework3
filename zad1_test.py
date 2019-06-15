from zad1 import Article

test1 = Article()
test1.title = 'title'
print('test 1: ', test1.title)
test1.title = 56
print('test 2: ', test1.title)
test1.title = 'te st'
print('test 3: ', test1.title)
test1.author = 'stasatadic'
print('test 4: ', test1.author)
test1.author = 'stasa tadic'
print('test 5: ', test1.author)
test1.author = 67
print('test 6: ', test1.author)
test1.description = 'orioeioejfiojiotfiojijfei'
print('test 7: ', test1.description)
test1.description = 'jfijfijijfirjfirjfirjfrijfrijfrijfrijfirjfrifjrijfrijfirjfirjfirjfirjfrijfirjfirjfrijfirjrifjrijri'
print('test 8: ', test1.description)
test1.category = 'kikikikikikikikikikikikikikikikikikikikikikikikikikikikikikik'
print('test 9: ', test1.category)
test1.category = 'kikikikikikikikikikik'
print('test 10: ', test1.category)
test1.category = 33
print('test 11: ', test1.category)
test1.views = 10
print('test 12: ', test1.views)
test1.views = ' ydgeygdye'
print('test 13: ', test1.views)
test1.insert_new_comment('titlea', 'autor','1')
test1.insert_new_comment('titleb', 'autor','2')
test1.insert_new_comment('titlec', 'autor','3')
test1.insert_new_comment('title4', 'autor3','3')
test1.insert_new_comment('title5', 'autor3','3')
test1.insert_new_comment('title6', 'autor3','3')
print('test 14: ',test1.comments)
test1.insert_new_comment('title2', 'autor2','opisssssusjusjsujsusjusjus2')
print('test 15: ',test1.comments)
test1.insert_new_comment('title2', 'autor2','opisssssusjusjsujsusjusjus2')
print('test 16: ',test1.comments)
test1.insert_new_comment('title3', '','opisssssusjusjsujsusjusjus2')
print('test 17: ',test1.comments)
# test1.comments = 'test'
print('test 18: ', test1.comments)
test1.delete_comment_by_title('title3')
print('test 19: ', test1.comments)
test1.delete_comments_by_author('autor')
print('test 20: ', test1.comments)
print('test 21: ', test1.get_comment_by_title('title2'))
print('test 21: ', test1.get_comment_by_title('title4'))
print('test 22: ', test1.get_comments_by_author('autor3'))
test1.inc_views()
print('test 23: ', test1.views)
test1.inc_views(56)
print('test 24: ', test1.views)
test1.inc_views('eudeudj')
print('test 25: ', test1.views)
print('test 26: ', test1)