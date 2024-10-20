from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        result = ""
        for x in strs:
            x = x.encode("UTF-8")
            result += "\""
            for y in list(x):
                result += str(y)+ ","
            result = result[:-1]
            result += "\""
            result += "_"
        return result[:-1]

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        result = []
        sspl = s.split("_")
        for x in sspl:
            x = x.replace("\"", "")
            if len(x) == 0:
                result.append("")
            else:
                xspl = x.split(",")
                xspl = [int(i) for i in xspl]
                word = ""
                for y in xspl:
                    word += chr(y)
                result.append(word)

        return result

sol = Solution()
print(sol.encode(["test","asdf"]))
enc = sol.encode(["","test","asdf"])
print(sol.decode(enc))
enc = sol.encode([""])
print(sol.decode(enc))
enc = sol.encode([])
print(sol.decode(enc))
print(len([""]))
