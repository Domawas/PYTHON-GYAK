def masodperc(szam:int):
    
    if szam < 59:
        print(f"{szam:>4}mp -> 00:00:{szam:02}")
    elif 3600 > szam >= 60:
        
        perc = szam // 60  
        masodperc = szam % 60  
        print(f"{szam:>4}mp -> 00:{perc:02}:{masodperc}")  
    elif szam >= 3600:
        ora = szam // 3600  
        perc = (szam % 3600) // 60  
        masodperc = szam % 60  
        print(f"{szam:>4}mp -> {ora:02}:{perc:02}:{masodperc:02}")  


def forditva(ora:int,perc:int,mperc:int):
    ossz = (ora * 60 * 60) + (perc * 60) + mperc
    print(f"{ora:>4}ó, {perc:>4}p, {mperc:2}mp -> {ossz:4}mp")