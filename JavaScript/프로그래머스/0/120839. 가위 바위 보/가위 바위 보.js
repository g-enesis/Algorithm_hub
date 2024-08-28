function solution(rsp) {
    var answer = rsp;
   const spl = answer.split("").map((item) => {
        switch(item) {
            case "2":
                return "0"
            case "0":
                return "5"
            case "5":
                return "2"
        }
    }).join("")
    return spl;
}