# AS53
candidates = ["alice", "bob", "charlie"]

voters = int(input("How many voters are there?"))

vote = []
for i in range(voters):
    vote.append(i)
    vote[i] = ["a", "b", "c"]

for x in range(voters):
    a = 0
    b = 0
    c = 0
    while a not in candidates:
        a = input(f"Voter {x + 1}, choice 1").lower()
    vote[x][0] = a
    while b not in candidates:
        b = input(f"Voter {x + 1}, choice 2").lower()
    vote[x][1] = b
    while c not in candidates:
        c = input(f"Voter {x + 1}, choice 3").lower()
    vote[x][2] = c

while True:
    alice = 0
    bob = 0
    charlie = 0
    # take the first choice of each voter
    for e in range(voters):
        if vote[e][0] == "alice":
            alice = alice + 1
        elif vote[e][0] == "bob":
            bob = bob + 1
        elif vote[e][0] == "charlie":
            charlie = charlie + 1
    tally = [alice, bob, charlie]
    # if the was a majority vote, they win
    if alice / voters > 1 / 2:
        print("Alice is the winner!")
        break
    elif bob / voters > 1 / 2:
        print("Bob is the winner!")
        break
    elif charlie / voters > 1 / 2:
        print("Charlie is the winner!")
        break
    # else compare the results
    l = tally.index(min(tally))
    if l == 0:
        lowest = "alice"
    elif l == 1:
        lowest = "bob"
    elif l == 2:
        lowest = "charlie"
    # else eliminate the lowest voted
    for o in range(voters):
        if vote[o][0] == lowest:
            # the second choice for the eliminated party is used
            vote[o].remove(vote[o][0])
    # repeat the process
