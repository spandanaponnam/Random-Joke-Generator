import pyjokes
import random
category = input("Choose joke category (all, neutral, chuck, twister): ").strip()
joke=pyjokes.get_jokes("en",category =category)
random_j=random.choices(joke)
print("Here is a joke for you: \n",random_j)