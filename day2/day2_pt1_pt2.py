
# input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
input = """288352-412983,743179-799185,7298346751-7298403555,3269-7729,3939364590-3939433455,867092-900135,25259-67386,95107011-95138585,655569300-655755402,9372727140-9372846709,986003-1032361,69689-125217,417160-479391,642-1335,521359-592037,7456656494-7456690478,38956690-39035309,1-18,799312-861633,674384-733730,1684-2834,605744-666915,6534997-6766843,4659420-4693423,6161502941-6161738969,932668-985784,901838-922814,137371-216743,47446188-47487754,117-403,32-77,35299661-35411975,7778-14058,83706740-83939522"""

# pt 1 
ranges = map(lambda x: map(int, x.split("-")), input.split(","))
invalids = 0
for s, e in ranges:
    for i in range(int(s), int(e+1)):
        id_ = str(i)
        n = len(id_)
        if n%2 == 0: 
            m = int(n/2)
            if id_[:m] == id_[m:]:
                invalids += int(id_)
print(invalids)

# pt 2

# (my version)
# ranges = map(lambda x: map(int, x.split("-")), input.split(","))
# invalids = set()
# for s, e in ranges:
#     for i in range(int(s), int(e+1)):
#         id_ = str(i)
#         n = len(id_)
#         found = False
#         for k in range(2, n+1):
#             if n%k == 0:
#                 m = int(n//k)
#                 part_len = n // k
#                 splits = [id_[i:i + part_len] for i in range(0, n, part_len)]
#                 s0 = splits[0]
#                 if all([s == s0 for s in splits]):
#                     invalids.add(int(id_))
#             if found:
#                 break
# print(sum(invalids))

# (AI-enhanced)
ranges = (tuple(map(int, x.split("-"))) for x in input.split(","))
invalids = set()
for s, e in ranges:
    for i in range(s, e + 1):
        id_ = str(i)
        n = len(id_)
        found = False
        for k in range(2, n + 1):
            if n % k != 0:
                continue
            part_len = n // k
            first = id_[:part_len]
            if first * k == id_:
                invalids.add(i)
                found = True
                break  
print(sum(invalids))
