function solution(keyinput, board) {
    var answer = [0, 0];
    const maxX = Math.floor(board[0] / 2)
    const maxY = Math.floor(board[1] / 2)
        keyinput.forEach((key) => {
            switch(key) {
                case "left":
                    if(answer[0] > -maxX) {
                        answer[0] -= 1
                    }
                    break;

                case "right":
                    if(answer[0] < maxX) {
                        answer[0] += 1
                    }
                    break;


                case "up":
                   if (answer[1] < maxY) {
                       answer[1] += 1
                   }
                    break;

                case "down":
                    if (answer[1] > -maxY) {
                        answer[1] -= 1
                    }
                    break;
        }
        })
        
        
    
    
    return answer;

}