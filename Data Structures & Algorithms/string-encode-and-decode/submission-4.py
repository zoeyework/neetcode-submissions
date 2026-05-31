class Solution:
    def encode(self, strs: List[str]) -> str:
        res=''
        for string in strs:       
            res = res + str(len(string)) + "#" + string
        return res
    # ['abcde','adbacs','adasfgd']
    # 5#adbce6#adbacs#8#adasfgd
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0 #從字串1開始
        # while i < len(s):
        #     j=i
        #     while s[j] != "#":
        #         j=j+1
        #     length=int(s[i:j])
        #     tmp_string= s[j+1:j+1+length]
        #     res.append(tmp_string)  
        #     i=j+1+length

        while i < len(s):
            j = i
            str_len = ""
            while s[j] != "#":
                str_len+=s[j]
                j+=1
            tmp_len = int(str_len)
            i=j+1
            tmp_str = ""
            for k in range(tmp_len):
                tmp_str+=s[i]
                i+=1
            res.append(tmp_str)

        return res
        
# time complexity = O(n)+O(n^2) ~ O(n^2)
# edge case, error case 