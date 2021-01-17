/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
    maxValue = 0
    temp = 0
    for(i in s){
        if(s[i] === '('){
            temp = temp + 1
        }
        if(s[i] === ')'){
            temp = temp - 1
        }
        if(temp > maxValue){
            maxValue = temp
        }
    }
    return maxValue
};