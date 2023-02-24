const total_n = 1_000_000
let max_n = 0
let max_count = 0
const start_time = Date.now()

//calculation
for(let i = 1; i < total_n; i++){
    n = i
    count = 0
    while(n > 1){
        if(n % 2 == 0){
            n = n / 2
        }else{
            n = 3 * n + 1
        }
        count += 1
    }  
    if(count > max_count){
        max_count = count
        max_n = i
    }
}

//print results
const elapsed_time = Math.floor(Date.now()-start_time)

console.log(max_n, max_count, "?", elapsed_time, "ms")