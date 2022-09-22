import clinic

def test(name: str):
    print(f"Hello {name}!")

example = clinic.CLI("example")
example.add("hello", ["name"], test)
example.run()