This is the active working repository for my Python code to solve the True Genius brand Grecian Computer puzzle.  All columns must add up to 42 for the puzzle to be solved.

Program logic
    - Check the first column of the puzzle.
        - Start with the bottom layer of the puzzle in column A
        - Populate Cells 1-4 (cell1, 2, 3, 4) with the values in the active column for that layer
            - The active column (activecolumn1, 2, 3, 4, 5) is the current indexed position of the layer from the starting point
        - Move up one layer and if any cells that are called have a number that is not zero, overwrite the value from the previous layer
            - This simulates the physical build of the puzzle where each disc has either a number or a cutout in any given position
            - Repeat for each layer
        - Check if the sum of cells 1-4 == 42
            - If it does, index the active column for each layer by 1 and repeat
            - If it does not, run the index function to index one layer one position forward
                - Starting with layer 5, the layer (column1, 2, 3, 4, 5) is indexed until it rolls over to the original position
                    - When rolling over, the layer below indexes by one
                    - The entire stack indexes in the same way as an analog odometer
                - Reset the activecolumn(1-5) to the new value of column(1-5)
                - Back to the beginning to check with the new puzzle index
                    
