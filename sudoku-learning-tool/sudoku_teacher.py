class SudokuTeacher:
    def __init__(self):
        # Sample puzzle (0 represents empty cells)
        self.puzzle = [
            [5,3,0, 0,7,0, 0,0,0],
            [6,0,0, 1,9,5, 0,0,0],
            [0,9,8, 0,0,0, 0,6,0],
            
            [8,0,0, 0,6,0, 0,0,3],
            [4,0,0, 8,0,3, 0,0,1],
            [7,0,0, 0,2,0, 0,0,6],
            
            [0,6,0, 0,0,0, 2,8,0],
            [0,0,0, 4,1,9, 0,0,5],
            [0,0,0, 0,8,0, 0,7,9]
        ]

    def print_board(self):
        """Print the Sudoku board in a nice format"""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                    
                if j == 8:
                    print(self.puzzle[i][j])
                else:
                    print(str(self.puzzle[i][j]) + " ", end="")

    def find_empty(self):
        """Find an empty cell in the puzzle"""
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    return (i, j)
        return None

    def get_possible_numbers(self, row, col):
        """Find all possible numbers for a given cell"""
        possible = []
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                possible.append(num)
        return possible

    def is_valid(self, row, col, num):
        """Check if a number is valid in a given cell"""
        # Check row
        for j in range(9):
            if self.puzzle[row][j] == num and col != j:
                return False
                
        # Check column
        for i in range(9):
            if self.puzzle[i][col] == num and row != i:
                return False
        
        # Check 3x3 box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.puzzle[i][j] == num and (i, j) != (row, col):
                    return False
                    
        return True

    def explain_possibilities(self, row, col):
        """Explain why certain numbers are possible or not"""
        if self.puzzle[row][col] != 0:
            print(f"\nCell ({row+1},{col+1}) already contains {self.puzzle[row][col]}")
            return

        possible = self.get_possible_numbers(row, col)
        
        print(f"\nAnalysis for cell ({row+1},{col+1}):")
        print("Possible numbers:", possible)
        
        # Explain why numbers are blocked
        row_numbers = set(self.puzzle[row]) - {0}
        col_numbers = set(self.puzzle[i][col] for i in range(9)) - {0}
        
        box_x = col // 3
        box_y = row // 3
        box_numbers = set()
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.puzzle[i][j] != 0:
                    box_numbers.add(self.puzzle[i][j])

        print("\nWhy?")
        print(f"Numbers already in row: {sorted(row_numbers)}")
        print(f"Numbers already in column: {sorted(col_numbers)}")
        print(f"Numbers already in 3x3 box: {sorted(box_numbers)}")

def main():
    game = SudokuTeacher()
    
    while True:
        game.print_board()
        print("\nOptions:")
        print("1. Analyze cell")
        print("2. Quit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                if 0 <= row <= 8 and 0 <= col <= 8:
                    game.explain_possibilities(row, col)
                else:
                    print("Invalid input! Row and column must be between 1 and 9.")
            except ValueError:
                print("Please enter valid numbers!")
        elif choice == '2':
            print("Thanks for learning Sudoku!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()