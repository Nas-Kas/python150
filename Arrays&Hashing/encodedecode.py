'''

build a delimeter with a number that tells me the length of the next string
example
[hello, world] -> 5#hello5#world
when we decode it we use the number up to the hashtag to determine the length of the next string
take value up to the hashtag
convert it to a number
take the substring from that index+1 -> index + value + 1
add substring to array
increment the index by value + 1
until index reaches the length of that string

Questions
will the string contain any possible english character or unicode symbol
will there be a max size for the string
will the string have empty spaces how do i deal with that?
5 mins
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += str(f"{len(x)}#{x}")
        return res


    def decode(self, s: str) -> List[str]:
        index = 0
        reslist = []
        while index < len(s):
            val = ""
            while index < len(s) and s[index] != "#":
                val += s[index]
                index += 1
            index += 1
            val = int(val) + index
            curr = s[index:int(val)]
            index = val
            reslist.append(curr)
        return reslist