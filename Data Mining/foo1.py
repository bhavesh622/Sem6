import foo2
def test():
    for _ in range(5):
        print('*' *5)
    print('Exiting foo1')
if __name__=="__main__":
    test()
    foo2.test()
    
    