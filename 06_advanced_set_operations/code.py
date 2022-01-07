friends = {"Bob", "Tom", "Ana"}
abroad = {"Bob", "Ana"}

local_friends = friends.difference(abroad)
print(local_friends)

friends = {"Bob", "Dylan"}
other_friends = {"Ana"}

all_friends = other_friends.union(friends)
print(all_friends)

art = {"Bob", "Jen", "Rolf", "Charlie" }
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)