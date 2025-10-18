from singleton import Singleton
def main():
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)
    s1.setMessage("Hello Singleton s1")
    s1.showMessage()
    s2.showMessage()
    s2.setMessage("Hello Singleton s2")
    s1.showMessage()
    s2.showMessage()

if __name__ == "__main__":
    main()