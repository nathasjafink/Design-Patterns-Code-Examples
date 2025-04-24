# singleton.py

class Singleton:
    _instance = None  # Holds the single instance of the class

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = 0  # Example attribute
        return cls._instance

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value
