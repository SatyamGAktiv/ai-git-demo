name = input("Please enter your name: ").strip()
print(f"Hello, {name}!")

words = ["Hello", "this", "is", "a", "test"]

# Build the sentence without adding a trailing space.
sentence = " ".join(words)

print(sentence)
