
function solution(id_pw, db) {
    const userId = id_pw[0];
    const userPw = id_pw[1];
    
    for(const [dbId, dbPw] of db){
        
        
        if(dbId === userId){
            if(dbPw === userPw) {
                return "login";
            }else{
                return "wrong pw";
            }
            
        } 
    }
    return "fail"
}