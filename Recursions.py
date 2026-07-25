#Iterative 
def walk(steps):
    for step in range(1 , steps + 1):
        print(f"You take step #{steps}")

#recursive
def walk(steps):
    if steps == 0:
        return 
    walk(steps - 1)
    print(f"You take step #{steps}")

    walk(100)