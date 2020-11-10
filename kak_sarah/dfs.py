N = 8

def is_valid(i, j, sol):
  if (i >=1 and i<=N and j>=1 and j<=N):
    if (sol[i][j]==-1):
      return True
  return False

def knight_tour(sol, i, j, step_count, x_move, y_move):
  if (step_count == N*N):
    return True

  for k in range(0, 8):
    next_i = i+x_move[k]
    next_j = j+y_move[k]

    if(is_valid(next_i, next_j, sol)):
      sol[next_i][next_j] = step_count
      if (knight_tour(sol, next_i, next_j, step_count+1, x_move, y_move)):
        return True
      sol[next_i][next_j] = -1; # backtracking

  return False

def start_knight_tour():
    
  sol = []

  for i in range(0, N+1):
    a = [0]+([-1]*N)
    sol.append(a)

  x_move = [2, 1, -1, -2, -2, -1, 1, 2]
  y_move = [1, 2, 2, 1, -1, -2, -2, -1]

  sol[1][1] = 0 
  
  print("Sedang memproses ...")
  
  if (knight_tour(sol, 1, 1, 1, x_move, y_move)):
    
    for i in range(1, N+1):
      print(sol[i][1:])
    return True
  return False

if __name__ == '__main__':
  print(start_knight_tour())
