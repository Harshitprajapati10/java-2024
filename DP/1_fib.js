// Return nth term of fibonacci sequence 
// 0 1 1 2 3 5 8 13....


// Ordinary recursion + Memoization

const getfib = (n, memo = {}) => {
    if(n in memo){
        return memo[n];
    }
    if(n<2){
        return n;
    }
    memo[n] =  getfib(n-1, memo) + getfib(n-2, memo);
    return memo[n];
}

console.log(getfib(2))
console.log(getfib(6))
console.log(getfib(8))
console.log(getfib(50))


//Using Tabulation strategy

// n = 5
// [0,1,0,0,0]
// [0,1,1,1,0]
// [0,1,1,2,1]
// [0,1,1,2,3]

const getfibTabulated = (n) => {
    const table = Array(n+1).fill(0);
    table[1] = 1
    for(let i = 0; i<=n; i++){
        table[i+1] += table[i];
        table[i+2] += table[i];
    }
    return table[n];
}

console.log(getfibTabulated(2))
console.log(getfibTabulated(6))
console.log(getfibTabulated(8))
console.log(getfibTabulated(50))