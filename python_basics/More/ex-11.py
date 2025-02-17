class MyClass:
    num_instances = 0  

    def __init__(self):
        MyClass.num_instances += 1

    @staticmethod
    def get_num_instances():
        return MyClass.num_instances


obj1 = MyClass()
obj2 = MyClass()


print(f"Total instances: {MyClass.get_num_instances()}")