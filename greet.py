name = input("Please enter your name: ").strip()
print(f"Hello, {name}!")

print("Here's a star pattern for you:")
for i in range(1, 6):
    print("*" * i)

words = ["Hello", "this", "is", "a", "test"]

# Build the sentence without adding a trailing space.
sentence = " ".join(words)

print(sentence)
