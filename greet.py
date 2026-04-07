name = input("Please enter your name: ").strip()
print(f"Hello, {name}!")

print("Here's a star pattern for you:")
for i in range(1, 6):
    print("*" * i)

words = ["Hello", "this", "is", "a", "test"]

sentence = ""
for word in words:
    sentence = sentence + word + " "

print(sentence)