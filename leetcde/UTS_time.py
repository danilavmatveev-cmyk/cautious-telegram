import time
day = 24*60*60
sec = int(time.time() % 60)
minute =  int((time.time() % 3600)//60)
hours = int((time.time() % (3600*24))//3600)
print (f"количество дней от эпохи - {time.time()//day} \n {hours:02d}:{minute:02d}:{sec:02d}")