# # news api and request module question 
# import requests



# r = requests.get('https://www.datacareer.de/blog/accessing-the-news-api-in-python/')

# # print(response.content)
# # print(response.headers)
# # print(response.json)
# # print(response.__getattribute__)
# # print(response.__str__)
# print(r.json())

# print(r.headers)
# print(r.text)



# 1. GENERATORS
# def mygen():
#     for i in range(10):
#        yield i*2 - 4
# gen = mygen()
# print(next(gen))    
# print(next(gen))    
# print(next(gen))    
# print(next(gen))    



# 2.FUNCTION CACHING IN PY

# from functools import lru_cache
# import time

# @lru_cache(maxsize = None)
# def fx(n):
#     time.sleep(n)
#     return n*2
# print(fx(2))
# print("done for fx2")
# print(fx(4))
# print("done for fx4 after delay of 4s")
# print(fx(2))
# print("done for fx2")



# 3. REGULAR EXPRESSIONS IN PYTHON
import re 

pattern = r"[A-Z]+orn"
text = '''Born and raised in the Austrian Empire, Tesla first 
studied engineering and physics in the 1870s without receiving 
a degree. He then gained practical experience in the early 1880s 
working in telephony and at Continental Edison in the new electric
power industry. In 1884 he immigrated to the United States, where he 
became a naturalized citizen. He worked for a short time at the
Edison Machine Works in New York City before he struck out on 
his own. With the help of partners to finance and market his ideas,
Tesla set up laboratories and companies in New York to develop a 
range of electrical and mechanical devices. His AC induction motor
and related polyphase AC patents, licensed by Westinghouse Electric in 1888,
earned him a considerable amount of money and became the cornerstone 
of the polyphase system which that company eventually marketed.
'''
match = re.search(pattern,text)
print(match)

