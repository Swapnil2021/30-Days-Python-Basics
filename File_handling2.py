#operation in os module
import os
folder = os.listdir("data")
print(folder)
# for i in folder:
#     print(i)
for i in folder:
    print(os.listdir(f"data/{folder}"))
    