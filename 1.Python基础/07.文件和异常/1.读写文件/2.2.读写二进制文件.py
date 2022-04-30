import pickle

# 写
my_list = [123, 3.14, '柯小乐', ['another list']]
f = open(r"C:\Users\Administrator\Desktop\Python_all_file\my_list.pkl", "wb")

pickle.dump(my_list, f)
f.close()

# 读
f = open(r"C:\Users\Administrator\Desktop\Python_all_file\my_list.pkl", "rb")
your_list = pickle.load(f)
print(your_list)
