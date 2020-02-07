def test():
    for _ in range(5):
        print('+'*5)
    print('Exiting foo2')
    print("foo2main", __name__)

if __name__=="__main__":
    test()