
# ------------------------------------------- DAY 1 ------------------------------------------- #
# 1a. Find the two entries that sum to 2020; what do you get if you multiply them together?
# 1b. In your expense report, what is the product of the three entries that sum to 2020?

# use itertools.combinations to get: [A,B,C] >> [AB,AC,BC] and check if sum == 2020

# from itertools import combinations
# [print(a*b*c) for a,b,c in combinations(map(int,open("d1.txt")), 3) if a+b+c == 2020]

# s = open("d1.txt").readlines()
# print([s[i]*s[j]*s[k] for i in range(len(s)) for j in range(i+1,len(s)) for k in range(j+1,len(s)) if s[i]+s[j]+s[k] == 2020])

# ------------------------------------------- DAY 2 ------------------------------------------- #
# 2a. How many passwords are valid according to their policies?
# 2b. How many passwords are valid according to the new interpretation of the policies?

# use regex to split strings on non-alphanumeric symbols using \W+ then use standard indexing to access elements

# import re
# print(len([s for s in [re.split(r"\W+", t) for t in open("d2.txt")] if s[3].count(s[2]) >= int(s[0]) and s[3].count(s[2]) <= int(s[1])]))
# print(len([s for s in [re.split(r"\W+", t) for t in open("d2.txt")] if s[3][int(s[0])-1] == s[2] and s[3][int(s[1])-1] != s[2] or s[3][int(s[0])-1] != s[2] and s[3][int(s[1])-1] == s[2]]))

# ------------------------------------------- DAY 3 ------------------------------------------- #
# 3a. Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
# 3b. What do you get if you multiply together the number of trees encountered on each of the listed slopes?

# use a bit of math to get the row/col movements then use functools.reduce to multiply the array together

# from functools import reduce
# s = [[j for j in i.strip()] for i in open("d3.txt")]
# print(reduce(lambda x,y:x*y, [(lambda r,c: len([s[i*r][i*c%len(s[0])] for i in range(1,len(s)//r) if s[i*r][i*c%len(s[0])] == "#"]))(a[0],a[1]) for a in ((1,1),(1,3),(1,5),(1,7),(2,1))]))

# ------------------------------------------- DAY 4 ------------------------------------------- #
# 4a. Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
# 4b. Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?

# use regex to test for validity
# if any wrong format, set valid flag to False

# !!! IMPORTANT !!!
# for "pid" (ie. match 9 numbers): using r'[0-9]{9}' will match numbers with >9 digits, ie. will match 10 digits and above
# to prevent that, need to use start/end string qualifiers (^ for start, $ for end)
# r'^[0-9]{9}$' ensures string must start and end with the 9 digits of [0-9]. any less/more will not be matched

# s = [{j.split(":")[0]:j.split(":")[1] for j in i.split()} for i in open("d4.txt").read().split("\n\n")]
# print(len([i for i in s if len(i) == 7 and "cid" not in i or len(i) == 8]))

# import re
# all_valid = []
# for passport in s:
#     valid = True
#     if "cid" in passport: del passport["cid"]
#     if len(passport) != 7: valid = False
#     for k,v in passport.items():
#         if not valid: break
#         if k == "byr":
#             if int(v) < 1920 or int(v) > 2002: valid = False
#         elif k == "iyr":
#             if int(v) < 2010 or int(v) > 2020: valid = False
#         elif k == "eyr":
#             if int(v) < 2020 or int(v) > 2030: valid = False
#         elif k == "hgt":
#             if v[-2:] == "cm":
#                 if int(v[:-2]) < 150 or int(v[:-2]) > 193: valid = False
#             elif v[-2:] == "in":
#                 if int(v[:-2]) < 59 or int(v[:-2]) > 76: valid = False
#             else: valid = False
#         elif k == "hcl":
#             if not re.match(r'^#[0-9a-f]{6}$', v): valid = False
#         elif k == "ecl":
#             if not re.match(r'amb|blu|brn|gry|grn|hzl|oth', v): valid = False
#         elif k == "pid":
#             if not re.match(r'^[0-9]{9}$', v): valid = False
#     if valid: all_valid.append(passport)

# print(len(all_valid))

# ------------------------------------------- DAY 5 ------------------------------------------- #
# 5a. As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
# 5b. What is the ID of your seat?

# bsp: binary space partioning
# use recursion to split array of seat numbers (rows 0-127 and cols 0-7) into desired halves (similar to binary search)

# s = [i.strip() for i in open("d5.txt")]
# def bsp(seq, items):
#     if len(seq) == 1: return items[:2**len(seq)//2][0] if seq[0] == "F" or seq[0] == "L" else items[2**len(seq)//2:][0]
#     if seq[0] == "F" or seq[0] == "L": return bsp(seq[1:], items[:2**len(seq)//2])
#     else: return bsp(seq[1:], items[2**len(seq)//2:])

# seats = [bsp(ss[:7], [i for i in range(2**len(ss[:7]))]) * 8 + bsp(ss[7:], [i for i in range(2**len(ss[7:]))]) for ss in s]
# print(max(seats))
# print([seat for seat in seats+[i for i in range(min(seats), max(seats)+1)] if seat not in seats])

# ------------------------------------------- DAY 6 ------------------------------------------- #
# 6a. For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
# 6b. For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

# use sets to count number of unique letters. for 6b, match with number of people in each group

# s = [[j for j in i.split()] for i in open("d6.txt").read().split("\n\n")]
# print(sum([len(set("".join(i))) for i in s]))
# print(sum([len([j for j in set("".join(i)) if "".join(i).count(j) == len(i)]) for i in s]))

# ------------------------------------------- DAY 7 ------------------------------------------- #
# 7a. How many bag colors can eventually contain at least one shiny gold bag?

s = [i for i in open("d7.txt")]
print(s)

# ------------------------------------------- DAY 8 ------------------------------------------- #
