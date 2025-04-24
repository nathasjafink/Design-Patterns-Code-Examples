# example.py

from singleton import Singleton

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.increment()
    s1.increment()
    print("s1 value:", s1.get_value())  # Outputs: 2

    print("s2 value:", s2.get_value())  # Outputs: 2 (same instance as s1)

    print("s1 is s2:", s1 is s2)        # Outputs: True
