print("day 8 of py")
# 1. ASYNCIO
# import time
# import asyncio

# async def func1():
#     await asyncio.sleep(1)
#     print("after 1 secs func1 ")
# async def func2():
#     await asyncio.sleep(1)
#     print("after 1 secs func2")
# async def func3():
#     await asyncio.sleep(4)
#     print("after 4s") 
# l = ()
# async def main():
#     l = await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )
#     # gather syntax is used for maintaining priority

#     # task = asyncio.create_task(func1())
#     # await func2()
#     # await func3()

    
# print(l)

# asyncio.run(main())

#application :dowmloading images
# import requests
# import asyncio

# async def func1():
#     url = "https://instagram.com/favicon.ico"
#     resp = requests.get(url)
#     open("insta1.ico", 'wb').write(resp.content)
#     await asyncio.sleep(1)
#     print("func1")
#     return "compl1"
# async def func2():
#     url ="https://www.flaticon.com/free-icon/instagram_1384031"
#     resp = requests.get(url)
#     open("downldfile2", 'wb').write(resp.content)
#     await asyncio.sleep(1)
#     print("func2")

# async def func3():
#     url = "https://unsplash.com/photos/a-mountain-is-reflected-in-the-still-water-of-a-lake-pT_ZiMWFUy4"
#     resp = requests.get(url)
#     open("downldfile3.jpg", 'wb').write(resp.content)
#     await asyncio.sleep(1)
#     print("func3")

# async def main():
#     l = await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )
#     print(l) #download te image instantly
#     # await func1()
#     # await func2()
#     # await func3() #serial wise download of images

# asyncio.run(main())    



# 2. MULTITHREADING
