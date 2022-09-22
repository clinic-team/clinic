import clinic

def test(name: str, lastname: str):
    print(f"Hello {name}!")

example = clinic.CLI("example")
example.add("hello", ["name", "last_name"], test, "Says hello")
example.run()