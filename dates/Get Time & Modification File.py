import os.path , time
print("Last Modified: ", time.ctime(os.path.getmtime("Get USER.py")))
print("Time Created: ", time.ctime(os.path.getctime("Get USER.py")))