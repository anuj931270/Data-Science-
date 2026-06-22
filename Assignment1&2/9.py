# Task: Cricket Stats Analyzer
player1 = int(input("Enter runs scored by Player 1: "))
player2 = int(input("Enter runs scored by Player 2: "))
player3 = int(input("Enter runs scored by Player 3: "))
player4 = int(input("Enter runs scored by Player 4: "))
player5 = int(input("Enter runs scored by Player 5: "))
total_runs = player1 + player2 + player3 + player4 + player5
average_runs = total_runs / 5
# print("Total Runs Scored:", total_runs)
# print("Average Runs:", average_runs)
print(f"Total Runs Scored: {total_runs} Average Runs: {average_runs}")