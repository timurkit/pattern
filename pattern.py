def tokenize_B(B:str):
    tokens =(token for token in B.split('@') if token)
    B_position = 0
    for token in tokens:
        n = B.index(token,B_position)
        yield n,token
        B_position = B_position +len(token)+1

def ara_ara():
    A=input()
    B=input()
    c=0
    for i in range(len(B)):
        if B[i]=='@': c=c+1
        else: break

    check=(B[0],len(B),c)
    tokens = [*tokenize_B(B)]
    if not tokens:
        return 0
    atw = tokens[0][1]
    i=0
    words=A.find(atw)
    while words>-1:
        i=i+words
        A=A[words:]
        for n,token in tokens[1:]:
            if A[n:n+len(token)]!=token:
                i=i+1
                A = A[1:]
                words=A.find(atw)
                break
        else:
            if check[0]=='@' and check[1]>1:
                return i-c
            else:
                return i    

result=ara_ara()
if result is None: result=-1
print(result)                 
