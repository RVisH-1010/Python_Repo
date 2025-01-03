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



# 

