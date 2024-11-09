// Given a string and an array of characters, tell whether the string can be formed or not
// use any element of array as many times as possible


// Ordinary recursion + Memoization

const canConstruct = (target, wordBank, memo = {}) => {
    if(target in memo) return memo[target];
    if(target === "") return true;
    for(let word of wordBank){
        if(target.indexOf(word)===0){
            const suffix = target.slice(word.length);
            if(canConstruct(suffix, wordBank, memo) === true){
                memo[target]= true;
                return true;
            }
        }
    }
    memo[target] = false;
    return false;
}

console.log(canConstruct("abcdef",["ab","abc","cd","def","abcd"]));
console.log(canConstruct("skateboard",["bo","rd","ate","t","ska","sk","boar"]));
console.log(canConstruct("purple",["purp","p","ur","le","purpl"]));
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey",["e","ee","eee","eeee","eeeee"]));



// Tabulation

const canConstructTabulated = (target, wordBank) => {
    const table = Array(target.length + 1).fill(false);
    table[0] = true;
    for(let i = 0; i<=target.length; i++){
        if(table[i]===true){
            for(let word of wordBank){
                if(target.slice(i, i+word.length) === word){
                    table[i+word.length] = true;
                }
            }
        }
    }
    return table[target.length];
}

console.log(canConstructTabulated("abcdef",["ab","abc","cd","def","abcd"]));
console.log(canConstructTabulated("skateboard",["bo","rd","ate","t","ska","sk","boar"]));
console.log(canConstructTabulated("purple",["purp","p","ur","le","purpl"]));
console.log(canConstructTabulated("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeey",["e","ee","eee","eeee","eeeee"]));