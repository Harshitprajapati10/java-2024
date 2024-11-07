// return true if target is formed with array
// repetition of elements are allowed

// ordinary recursion + memoization


const canSum = (targetSum, numbers, memo = {}) => {
    if (targetSum in memo) return memo[targetSum];
    if(targetSum == 0) return true;
    if(targetSum < 0) return false;

    for (const num of numbers) {
        const remainder = targetSum - num;
        if (canSum(remainder, numbers ,memo)) {
            memo[targetSum] = true;
            return true;
        }
    }

    memo[targetSum] = false;
    return false;
}

console.log(canSum(7,[5,3,4,5]))
console.log(canSum(7,[2,4]))
console.log(canSum(100,[25,3,3,4]))
console.log(canSum(8,[2,4]))


// canSum using tabulation
// create boolean array of size targetSum + 1

const canSumTabulated = (targetSum, numbers) =>{
    const table = Array(targetSum + 1).fill(false);
    table[0] = true;
    for(let i = 0; i<= targetSum; i++){
        if(table[i] === true){
            for(let num of numbers){
                table[i+num] = true;
            }
        }
    }
    return table[targetSum];
}

console.log(canSumTabulated(7,[5,3,4,5]))
console.log(canSumTabulated(7,[2,4]))
console.log(canSumTabulated(100,[25,3,3,4]))
console.log(canSumTabulated(8,[2,4]))
