import math
from math import pi as PI
from math import sqrt as sqrt



print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()
if inp == "a":
    print("pcBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()


    if inp == "a":
        print("pcSzecianu - a | pcProstopadloscianu - b | pcGraniastoslupa - c | pcOstroslupa - d | pcWalca - e | pcStozka - f | pcKuli - g")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            a = float(input("a = "))
            print(f"pcSzecianu o boku {a} = {6*a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"pcProstopadloscianu o bokach {a} {b} {c} = {2*a*b+2*b*c+2*c*a}")
        elif inp == "c":
            pp = float(input("pp = "))
            pb = float(input("pb = "))
            print(f"pcGraniastoslupa dla pp = {pp} i pb = {pb} = {2*pp+pb}")
        elif inp == "d":
                pp = float(input("pp = "))
                pb = float(input("pb = "))
                print(f"pcOstroslupa dla pp = {pp} i pb = {pb} = {pp+pb}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"pcWalca dla r = {r} i h = {h} = {2*PI*r**2+2*PI*r*h}")
        elif inp == "f":
            r = float(input("r = "))
            l = float(input("l = "))
            print(f"pcStozka dla r = {r} i l = {l} = {PI*r**2+PI*r*l}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"pcKuli dla r = {r} = {4*PI*r**2}")
        else:
            print("Nie ma takiej komendy: ")




    elif inp == "b":
        print("vSzecianu - a | vProstopadloscianu - b | vGraniastroslupa - c | vOstroslupa - d | vWalca - e | vStozka - f | vKuli - g")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"vSzescianu dla a = {a} = {a*a*a}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"vProsopadloscianu dla a = {a} b = {b} i c = {c} = {a*b*c}")
        elif inp == "c":
            pp = float(input("pp: "))
            h = float(input("h: "))
            print(f"vGraniastoslupa dla pp = {pp} i h = {h} = {pp*h}")
        elif inp == "d":
            pp = float(input("pp: "))
            h = float(input("h: "))
            print(f"vOstroslupa dla pp = {pp} i h = {h} = {pp/3*h}")
        elif inp == "e":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"vWalca dla r = {r} i h = h = {PI*r**2*h}") 
        elif inp == "f":
            r = float(input("r = "))
            h = float(input("h = "))
            print(f"vStozka dla r = {r} i h = {h} = {1/3*PI*r**2*h}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"vKuli dla r = {r} = {4/3*PI*r**3}")
        else:
            print("nie ma takiej komendy")    
    else:
        print("nie ma takiej komendy")



elif inp == "b":
    print("obwody fig plaskie - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print("oKwadratu - a | oProstokata - b | oRownolegloboku - c | oTrapezu - d | oTrojkata - e | oTrojkatarownobocznego - f | oKola - g | oRombu - h")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"oKwadratu dla a = {a} = {a*4}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"oProstokata dla a = {a} i b = {b} = {2*a+2*b}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"oRownolegloboku dla a = {a} i b = {b} = {2*a+2*b}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"oTrapezu dla a = {a} b = {b} c = {c} i d = {d} = {a+b+c+d}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"oTrojkata dla a = {a} b = {b} c = i {c} = {a+b+c}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"oTrojkatarownobocznego dla a = {a} = {3*a}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"oKola dla r = {r} = {2*PI*r}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"oRombu dla a = {a} = {a*4}")
        else:
            print("nie ma takiej komendy")
                    




    elif inp == "b":
        print("ppKwadratu - a | ppProstokata - b | pp rownolegloboku - c | ppTrapezu - d | ppTrojkata - e | ppTrojkatarownobocznego - f | ppKola - g | ppRombu - h ")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input("a = "))
            print(f"ppKwadratu dla a = {a} = {a**2}")
        elif inp == "b":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"ppProstokata dla a ={a} i b = {b} = {a*b}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppRownolegloboku dla a ={a} i h = {h} = {a*h}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"ppTrapezu dla a = {a} b rownego {b} i h = {h} = {(a+b)*h/2}")
        elif inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"ppTrojkata dla a = {a} i h = {h} = {a*h/2}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"ppTrojkatarownobocznego dla a = {a} = {a**2*sqrt(3)/4}")
        elif inp == "g":
            r = float(input("r = "))
            print(f"ppKola dla r = {r} = {PI*r**2}")
        elif inp == "h":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"ppRombu dla e = {e} i f = {f} = {e*f/2}")    
        else:
            print("nie ma takiej komendy")







    else:
        print("nie ma takiej komendy")




else:
    print("Nie ma takiej komendy")

