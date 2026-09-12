# This is a dictionary in python

my_dict = {"name": "John", "age": 30, "city": "New York"}
my_list_of_dict = [{"name": "John", "age": 30, "city": "New York"}, {"name": "Jane", "age": 25, "city": "Los Angeles"}]

def my_function1(data):
    my_list_of_dict.append(data)
    return my_list_of_dict
def my_function2(data):
      for elements in my_list_of_dict:
            print("*"* 30)
            print( f"Type of elements {elements}: {type(elements)}" )
            print("*"* 30)
            if elements["name"] == data:
                  elements["age"] = "39"
      return my_list_of_dict

if __name__ == "__main__":
    print("="* 160)  
    print(my_dict)
    print(my_function1({"name": "Mike", "age": 35, "city": "Chicago"}))
    print(my_function2("John"))
    print("="* 160)