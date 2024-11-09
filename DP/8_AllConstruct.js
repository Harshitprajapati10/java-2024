// Given a string and an array of characters, return 2D array of all ways the string can be formed 
// use any element of array as many times as possible


// Ordinary recursion + Memoization

const AllConstruct = (target, wordBank, memo = {}) => {
    if(target in memo) return memo[target];
    if(target === "") return [[]];
    const result = [];

    for(let word of wordBank){
        if(target.indexOf(word)===0){
            const suffix = target.slice(word.length);
            const suffixways = AllConstruct(suffix, wordBank, memo);    
            const targetWays = suffixways.map(way => [word,...way]);
            result.push(...targetWays)
        }
    }

    memo[target]= result;
    return result;
}

console.log(AllConstruct("abcdef",["ab","abc","cd","def","abcd"]));
console.log(AllConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]));
console.log(AllConstruct("purple",["purp","p","ur","le","purpl"]));
console.log(AllConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee"]));


// Tabulation

const AllConstructTabulated = (target, wordBank) => {
    const table = Array(target.length + 1).fill().map(() => []);
    table[0] = [[]];

    for(let i = 0; i <= target.length ; i++){
        for(let word of wordBank){
            if(target.slice(i, i+word.length) === word){
                const newCombination = table[i].map(subArray => [...subArray, word]);
                table[i + word.length].push(...newCombination);
            }
        }
    }

    return table[target.length];
}

console.log(AllConstructTabulated("abcdef",["ab","abc","cd","def","abcd"]));
console.log(AllConstructTabulated("skateboard",["bo","rd","ate","t","ska","sk","boar"]));
console.log(AllConstructTabulated("purple",["purp","p","ur","le","purpl"]));
console.log(AllConstructTabulated("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee"]));
