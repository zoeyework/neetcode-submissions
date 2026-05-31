class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_string=''
        final_encode_string=''
        for string in strs:
         lens=len(string)
         encode_string=str(lens)+"#"+string
         final_encode_string =final_encode_string+encode_string
        print(final_encode_string)
        return final_encode_string
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 1. 讓小助手 j 從 i 的位置出發，去找下一個 "#"
            j = i
            while s[j] != "#":
                j += 1  # 小碎步前進
                
            # 2. 此時 s[i:j] 就是 `#` 前面的數字
            lens = int(s[i:j])
            
            # 3. 從 # 的下一格 (j + 1) 開始，切出對應長度的字串
            string = s[j + 1 : j + 1 + lens]
            res.append(string)
            
            # 4. 大跳躍：把主指標 i 移到這個單字結束的下一格
            i = j + 1 + lens
            
        return res