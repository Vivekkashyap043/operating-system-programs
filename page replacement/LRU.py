capacity = int(input("Enter the no. of frames in main memory : "))
p = int(input("Enter the no. of pages : "))
f,st,fault = [],[],0
print("Enter the reference string : ",end="")
s = list(map(int,input().strip().split()))
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            st.append(len(f)-1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))

print("Hit count : ", p-fault)
print("Fault count : ", fault)