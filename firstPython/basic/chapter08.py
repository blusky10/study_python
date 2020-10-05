def greet_users(names):
    """리스트의 출력"""
    for name in names:
        msg = f"hello {name.title()}"
        print(msg)

usernames = ['haha', 'hoho']
greet_users(usernames)


unprinted_designs=['phone', 'robot', 'gggg']
complted_modes=[]

def print_model(unprinted_designs, complted_modes):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(f"Printing model : {current_design}")
        complted_modes.append(current_design)

print_model(unprinted_designs[:], complted_modes)
print("\n complete")

print("\n complted_modes")
for model in complted_modes:
    print(f"complted_modes: {model}")

print("\n unprinted_designs")
for model in unprinted_designs:
    print(f"unprinted_designs: {model}")    