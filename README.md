Program logic

Bottom Up - This will be the first attempt
1. Slice data set into layers - I think using the Pandas array works well for this
    - Done
2. Create a solution table with columns A-L and rows 0-4
3. Populate column A on solution table
    - Pull layer 1 column A data and place it in solution table
    - Pull layer 2 column A data
        - If there is a value in layer 2 table, overwrite layer 1 data
        - If layer 2 value is NaN, keep layer 1 data
    - Pull layer 3 column A data
        - Same as layer 2
    - Pull layer 4 column A data
        - Same as layer 3
    - Pull layer 5 column A data
        - Same as layer 4
    - Sum column A rows 0-3
        - Output sum in column A row 4
4. Check column A
    - If A4 == 42, loop with column B
        - If all values in row 4 == 42, the puzzle is solved
    - ElseIf A4 != 42, index layer 1 columns one to the right
        - Column L data is now in column A
        - Clear the solution table
        - Restart at step 3
        - Once layer 1 indexes back to the original position with no solution, index layer 2
            - Layer 1 will then index on every failure until it returns to the original position
            - Layer 2 will index a second time and the process will repeat
            - Layer indexing will cascade until a solution is reached, or layer 5 indexes back to the original position with no solution


Top Down - I don't think this is the way to do it...
1. Slice data set into layers - I think using the Pandas array works well for this
2. Pull 4 numbers from column A
    - Start at layer 5
    - Grab A3
      - If NaN, Grab layer 4 A3
    - Grab A2
      - If NaN, Grab layer 4 A2, layer 3 A2, etc until real value is found
    - Grab A1
      - Same logic as above
    - Grab A0
      - Same logic as above
    - Sum the 4 numbers
      - If the sum == 42
        - Build new PANDAS table with Column A consisting of the 4 numbers pulled
        - The total should be in new row 4
        - Loop process for columns B-L
      - If the sum != 42
        - Shift layer 5 one column to the right
          - Column L moves to Column A
    - Repeat the process
      - Once layer 5 comes back to the original position, we index the columns on layer 4 one at a time
      - After layer 4 has indexed all the way around, index layer 5 by one and then begin indexing layer 4 again
      - This process repeats as a cascade to go through every combination of columns on all 5 layers until we get a result table where all row 4 entries are 42
     

    
