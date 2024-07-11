capacity = int(input("Enter the no. of frames in main memory : "))
p = int(input("Enter the no. of pages : "))
frames, st, fault = [],[],0
print("Enter the reference string : ",end="")
ref_str = list(map(int,input().strip().split()))
for s in ref_str:
    if s not in frames:
        if len(frames)<capacity:
            frames.append(s)
            st.append(len(frames)-1)
        else:
            idx = st.pop(0)
            frames[idx] = s
            st.append(idx)
        fault += 1
    else:
        st.append(st.pop(st.index(frames.index(s))))

print("Hit count : ", p-fault)
print("Fault count : ", fault)