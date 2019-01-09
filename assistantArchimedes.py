from wit import Wit
wit.init()

resp = wit.text_query('hi', 'MY_WIT_TOKEN')
print('Response: {}'.format(resp))

wit.close()
