# print("day 9 of python coding...")
# # 1. multiprocessing

# import multiprocessing
# import multiprocessing.process
# import requests

# def download(url,name):
#     response = requests.get(url)
#     x = open(f"File_{name}.jpg","wb")
#     x.write(response.content)
#     print(f"finished download {name}. ")

# url = "https://picsum.photos/2000/3000"
# pros = []

# for i in range(8):
#     # download(url,i)
#     p = multiprocessing.Process(target=download, args=[url,i])
#     p.start()
#     pros.append(p)

# for p in pros:
#     p.join()

# print("download done")
# # print(pros)


# Q: NOTIFICATION FOR DRINKING WATEER EVERY HR

