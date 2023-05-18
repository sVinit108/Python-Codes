for  a in range (1,21):
    with open(f"Tables/Table of {a}.txt",'w') as f:
     for b in range (1,11): 
        f.write(f'{a}X{b}={a*b}\n')
        #f.write('%sX%s=%s\n'%(a,b,a*b))
    
    
