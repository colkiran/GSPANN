
def fun(stud):
    print(f"stud inside fun :{stud}")
    stud.extend(['john', 'peter', 'richard'])
    print(f"stud inside fun :{stud}")

friends = ['Keneth', 'Kevin', 'Micheal', 'David']

print(f"friends before  :{friends}")

fun(friends)

print(f"friends after :{friends}")
