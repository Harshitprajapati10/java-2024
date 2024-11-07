// Return shortest array that sum upto target using numbers array
// repetition of elements are allowed

// ordinary recursion + memoization

const bestSum = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    let shortestCombination = null;

    for (const num of numbers) {
        const remainder = targetSum - num;
        const remainderResult = bestSum(remainder, numbers, memo);
        if (remainderResult !== null) {
            const combination = [...remainderResult, num];
            if (shortestCombination === null || combination.length < shortestCombination.length) {
                shortestCombination = combination;
            }
        }
    }

    memo[targetSum] = shortestCombination;
    return shortestCombination;
};


console.log(bestSum(7,[5,3,4,5]))
console.log(bestSum(7,[2,4]))
console.log(bestSum(100,[25,3,3,4]))
console.log(bestSum(8,[2,4]))


// Tabulation

const bestSumTabulated = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];
    
    for (let i = 0; i <= targetSum; i++) {
        if (table[i] !== null) {
            for (let num of numbers) {
                const nextIndex = i + num;
                
                if (nextIndex <= targetSum) {
                    const newCombination = [...table[i], num];
                    
                    // Only update if it's the first combination or if the new one is shorter
                    if (table[nextIndex] === null || newCombination.length < table[nextIndex].length) {
                        table[nextIndex] = newCombination;
                    }
                }
            }
        }
    }
    
    return table[targetSum];
};


console.log(bestSumTabulated(7,[5,3,4,5]))
console.log(bestSumTabulated(7,[2,4]))
console.log(bestSumTabulated(100,[25,3,3,4]))
console.log(bestSumTabulated(8,[2,4]))
