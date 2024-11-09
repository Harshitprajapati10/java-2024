// Given a string and an array of characters, tell number of ways the string can be formed 
// use any element of array as many times as possible


// Ordinary recursion + Memoization

const countConstruct = (target, wordBank, memo = {}) => {
    if(target in memo) return memo[target];
    if(target === "") return 1;
    let totalCount = 0;

    for(let word of wordBank){
        if(target.indexOf(word)===0){
            const numways = countConstruct(target.slice(word.length), wordBank, memo);     
            totalCount += numways;
        }
    }

    memo[target]= totalCount;
    return totalCount;
}

console.log(countConstruct("abcdef",["ab","abc","cd","def","abcd"]));
console.log(countConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]));
console.log(countConstruct("purple",["purp","p","ur","le","purpl"]));
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey",["e","ee","eee","eeee","eeeee"]));



// Tabulation

const countConstructTabulated = (target, wordBank) => {
    const table = Array(target.length + 1).fill(0);
    table[0] = 1;
    for(let i = 0; i<=target.length; i++){ 
        for(let word of wordBank){
            if(target.slice(i, i+word.length) === word){
                table[i+word.length] += table[i];
            }
        }    
    }
    return table[target.length];
}

console.log(countConstructTabulated("abcdef",["ab","abc","cd","def","abcd"]));
console.log(countConstructTabulated("skateboard",["bo","rd","ate","t","ska","sk","boar"]));
console.log(countConstructTabulated("purple",["purp","p","ur","le","purpl"]));
console.log(countConstructTabulated("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey",["e","ee","eee","eeee","eeeee"]));