"""
The if __name__ == "__main__":  exists in Python so that our Python files can act as either reusable modules, or as standalone programs.
"""
x = [5,7,14]

def test_list():
     print("from function test list",x)

if __name__ == "__main__":
    print("from f ")

    test_list()
