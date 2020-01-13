

def sliding(train,width,overlap_count):
    
    
    indx=np.arange (train.shape[0])  
    
    slider = Slider(width,overlap_count)
    slider.fit(indx)
    
    data3d=  np.array([]).reshape(0,width, train.shape[1])

    while True: 
        window_data = slider.slide()
        if slider.reached_end_of_list():break
            
        start=window_data[0]
        end  =window_data[-1]+1
        
        slic=train[start:end,:]
        
        ds=slic.reshape(1,width,-1)

        data3d=np.concatenate((data3d, ds))
    
        
    return data3d

def datasld(train,test,width,overlap_count):
    
    idx=test.reshape(-1,1)
    

    changes=list(np.where(np.roll(idx,1)!=idx)[0])
    daa= changes + [len(idx)]

    
    
    y=[]
    
    new=  np.array([]).reshape(0,width, train.shape[1])

    
    for i in range(len(daa)-1):

        goto=train[ daa[i] : daa[i+1] , : ]
        
        get3d= sliding(goto,width,overlap_count)

        yval=get3d.shape[0]*[ test[daa[i]] ]

        new=np.concatenate((new,get3d))

        #y=np.concatenate((y,test[i]))= np.asarray(mylist)
        y=y+yval
        
    return new.astype(np.float32), np.asarray(y).reshape(-1,).astype(np.uint8)
