class Person:

  def __init__(self, name):
    self.name = name

  def talk(self):
    message = input(f'What is your message {self.name}?')
    print(message)       

hamza = Person('hamza')
hamza.talk()    