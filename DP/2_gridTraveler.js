// Return total number of ways to travel a n X n grid
// gridTraveler(3,3) -> 6

// Ordinary Recursion + memoization

const gridTraveler = (row, col, memo = {}) => {
    const key = row + ',' + col;
    if(key in memo) return memo[key];
    if(row === 1 || col === 1) return 1;
    if(row === 0 || col === 0) return 0;
    memo[key] =  gridTraveler(row-1,col, memo) + gridTraveler(row, col-1, memo);
    return memo[key]
}

console.log(gridTraveler(1,2))
console.log(gridTraveler(2,2))
console.log(gridTraveler(3,3))
console.log(gridTraveler(18,18))


// Tabulaton
// create (row + 1) cross (col + 1) table
// Add 1 at (1,1) , only one way to travel
// under the bounds  add i,j th element to its right and down
// Return table[i][j]
// calculate (n+m)C(n)

const gridTravelerTabulated = (row, col) => {
    const table = Array(row+1).fill().map(()=>Array(col+1).fill(0));
    table[1][1] = 1;
    for(let i = 0; i<=row; i++){
        for (let j = 0; j <= col; j++){
            const current = table[i][j];
            if (j+1<=col) table[i][j+1] += current;
            if(i+1<=row) table[i+1][j] += current;
        }
    }
    return table[row][col];
}

console.log(gridTravelerTabulated(1,2))
console.log(gridTravelerTabulated(2,2))
console.log(gridTravelerTabulated(3,3))
console.log(gridTravelerTabulated(18,18))


/*
It can be done in python in constant space and time using combinations

import math
def grid_paths(n, m):
    return math.comb(n + m, n) 

*/