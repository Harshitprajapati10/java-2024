// Return any array that sum upto target using numbers array
// repetition of elements are allowed

// ordinary recursion + memoization

const howSum = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if(targetSum == 0) return [];
    if(targetSum < 0) return null;

    for (const num of numbers) {
        const remainder = targetSum - num;
        const remainderResult = howSum(remainder, numbers, memo)

        if(remainderResult != null){
            memo[targetSum] = [...remainderResult, num];
            return memo[targetSum];
        }
    }
    memo[targetSum] = null
    return null;
}

console.log(howSum(7,[5,3,4,5]))
console.log(howSum(7,[2,4]))
console.log(howSum(100,[25,3,3,4]))
console.log(howSum(8,[2,4]))



// Tabulation

const howSumTabulated = (targetSum, numbers) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];
    
    for (let i = 0; i <= targetSum; i++) {
        if (table[i] !== null) {
            for (let num of numbers) {
                const nextIndex = i + num;
                if (nextIndex <= targetSum && table[nextIndex] === null) {
                    table[nextIndex] = [...table[i], num];
                }
            }
        }
    }
    
    return table[targetSum];
}


console.log(howSumTabulated(7,[5,3,4,5]))
console.log(howSumTabulated(7,[2,4]))
console.log(howSumTabulated(100,[25,3,3,4]))
console.log(howSumTabulated(8,[2,4]))