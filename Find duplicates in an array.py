
 def duplicates(self, arr, n): 
    	# code here
    	a=[]
    	mp={}
    	
    	for i in range(0,n):
    	    if arr[i] in mp:
    	        mp[arr[i]]+=1
    	    else:
    	        mp[arr[i]]=1
    	for key,value in mp.items():
    	    if value>1:
    	        a.append(key)
    	if len(a)==0:
    	    a.append(-1)
    	return sorted(a);
