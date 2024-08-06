with open("Store.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("Store.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)


