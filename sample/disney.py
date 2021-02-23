pnoun=input("Enter a proper noun: ")
number = input("Enter a number: ")
transport = input("Enter a means of transport: ")
adj = input("Enter an adjective: ")
adj1 = input("Enter an adjective: ")
iverb = input("Enter a -ing verb: ")
animal = input("Enter a name of an animal: ")

madlib = f'Last month, I went to Disney World with {pnoun} . We traveled for {number} of hours by {transport}.\ ' \
          f'Finally, we arrived and it was very {adj}. There were{adj1} people{iverb} everywhere.\
           There were also people dressed up in{animal} costumes.'

print(madlib)