temperatura=int(input())
if temperatura<10:
    print("fa fred")
    if temperatura<=0:
        print("l'aigua es gelaria")
elif temperatura>30:
    print("fa calor")
    if temperatura>=100:
        print("l'aigua bulliria")
else:
    print("s'esta be")