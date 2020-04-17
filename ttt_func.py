#functions for tic tac toe
def print_grid(grid):
    print("".join(grid[0:11]))
    print("".join(grid[11:22]))
    print("".join(grid[22:33]))
    print("".join(grid[33:44]))
    print("".join(grid[44:55]))
    
def get_choice():
    print("Player - Make Your Choice: ", end = '')
    choice = 0
    try:
        choice = int(input())
    except ValueError:
        choice = int(input())
    while choice < 1 or choice > 9:
        print("Make a Valid Selection: ")
        choice = int(input())
    if choice == 1:
        return 1
    if choice == 2:
        return 5
    if choice == 3:
        return 9
    if choice == 4:
        return 23
    if choice == 5:
        return 27
    if choice == 6:
        return 31
    if choice == 7:
        return 45
    if choice == 8:
        return 49
    if choice == 9:
        return 53
        
def win_check(grid):
  #if X win return 1
  if grid[1] == 'X' and grid[5] == 'X' and grid[9] == 'X':
    return 1
  if grid[23] == 'X' and grid[27] == 'X' and grid[31] == 'X':
    return 1
  if grid[45] == 'X' and grid[49] == 'X' and grid[53] == 'X':
    return 1
  if grid[1] == 'X' and grid[23] == 'X' and grid[45] == 'X':
    return 1
  if grid[5] == 'X' and grid[27] == 'X' and grid[49] == 'X':
    return 1
  if grid[9] == 'X' and grid[31] == 'X' and grid[53] == 'X':
    return 1
  if grid[1] == 'X' and grid[27] == 'X' and grid[53] == 'X':
    return 1
  if grid[9] == 'X' and grid[27] == 'X' and grid[45] == 'X':
    return 1
  
  #if O win return 2
  if grid[1] == 'O' and grid[5] == 'O' and grid[9] == 'O':
    return 2
  if grid[23] == 'O' and grid[27] == 'O' and grid[31] == 'O':
    return 2
  if grid[45] == 'O' and grid[49] == 'O' and grid[53] == 'O':
    return 2
  if grid[1] == 'O' and grid[23] == 'O' and grid[45] == 'O':
    return 2
  if grid[5] == 'O' and grid[27] == 'O' and grid[49] == 'O':
    return 2
  if grid[9] == 'O' and grid[31] == 'O' and grid[53] == 'O':
    return 2
  if grid[1] == 'O' and grid[27] == 'O' and grid[53] == 'O':
    return 2
  if grid[9] == 'O' and grid[27] == 'O' and grid[45] == 'O':
    return 2
  
  return 3;