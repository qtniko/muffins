from pylab import *

# Finds amount (and 'mode')
loopieloop=True
while loopieloop==True:
    loopieloop=False
    INPUT=str(input("Antall muffinsformer (f bak for fritt fall, noe annet bak for ikke fritt fall VS fritt fall): "))
    INPUT=INPUT.split(" ")
    try:
        amount=INPUT[0]
        amount=int(amount)
    except: loopieloop=True
try: muff=INPUT[1]
except: muff=False

# Colors for graph (in the order they are used)
colors=["red", "blue", "green", "yellow", "pink"]

# Class for simulation with force
muffin_list=[]
class muffins:
    def __init__(self, antall):

        def a(v):
            L=k*v**2
            F_tot=G-L
            return F_tot/m

        m=0.00032*antall
        G=m*9.81
        k=0.001

        terminalfart=(G/k)**0.5
        terminaldist=False

        v=0
        t=0
        s=0
        s_slutt=3.92
        dt=0.01
        s_verdier=[s]
        v_verdier=[v]

        while s<s_slutt:
            v=v+a(v)*dt
            t=t+dt
            s=s+v*dt
            s_verdier.append(s)
            v_verdier.append(v)
            if v>=terminalfart*0.9 and bool(terminaldist)==False:
                terminaldist=s
        
        self.terminalfart=terminalfart
        self.tordis=terminaldist
        self.time=t
        self.s_values=s_verdier
        self.v_values=v_verdier
        self.number=antall
        muffin_list.append(self)

# Class for simulation without force
class muffins2:
    def __init__(self, antall):

        v=0
        t=0
        s=0
        a=9.81

        s_slutt=3.92
        dt=0.01
        s_verdier=[s]
        v_verdier=[v]

        while s<s_slutt:
            v=v+a*dt
            t=t+dt
            s=s+v*dt
            s_verdier.append(s)
            v_verdier.append(v)

        self.time=t
        self.s_values=s_verdier
        self.v_values=v_verdier
        self.number=antall
        muffin_list.append(self)

# Thingamajig to make sure the correct simulations are used
if bool(muff)==False:
    for i in range(1, amount+1):
        muffins(i)
else:
    if muff=="f":
        for i in range(1, amount+1):
            muffins2(i)
    else:
        muffins(amount)
        muffins2(amount)

# Adding all the values to pyplot
c=0
for i in muffin_list:
    plot(i.s_values, i.v_values, color=colors[c])
    c+=1
    if c==5:
        c=0
if bool(muff)==False:
    title("noe er muffins...")
else:
    if muff=="f":
        title("noe er muffins, men i fritt fall...")
    else:
        title("rød = med luftmotstand, blå = fritt fall")
xlabel("$s$ (m)")
ylabel("$v$ (m/s)")
grid()
show()

# Listing additional information about simulations
if bool(muff)==False:
    for i in muffin_list:
        print(i.number, "stk  | ", round(i.time,3), "s  | ", round(i.tordis,3), "m  | ", round(i.terminalfart,3), "m/s")
else:
    if muff=="f":
        for i in muffin_list:
            print(i.number, "stk  | ", round(i.time,3), "s")
    else:
        print("Med luftmotstand:")
        print(f"Antall muffinsformer: {muffin_list[0].number} stk")
        print(f"Tid: {round(muffin_list[0].time,3)} s")
        print(f"90% av terminalfart oppnådd etter: {round(muffin_list[0].tordis,3)} m")
        print(f"Terminalfart: {round(muffin_list[0].terminalfart,3)} m/s")
        print()
        print("Uten luftmotstand (fritt fall):")
        print(f"Antall muffinsformer: {muffin_list[1].number} stk")
        print(f"Tid: {round(muffin_list[1].time,3)} s")
