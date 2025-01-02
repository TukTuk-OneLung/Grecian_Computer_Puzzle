Program logic

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
    
