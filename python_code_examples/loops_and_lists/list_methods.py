colors_list = ['purple', 'brown', 'orange', 'blue', 'pink', 'fuchsia']
print(colors_list)

colors_list.remove('brown')
print(colors_list)

colors_list.append('yellow')
print(colors_list)

print(colors_list[1] + " and " + colors_list[2])

colors_list.insert(1, 'red')

print("NOTE: Inserting a new item will change the indexes.")
# this is the same command but the output has changed
print(colors_list[1] + " and " + colors_list[2])

print("NOTE: sort() alters the list.")
colors_list.sort()
print(colors_list)

colors_list.reverse()
print(colors_list)
