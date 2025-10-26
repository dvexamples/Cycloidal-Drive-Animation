
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*40,1.2*40)
plt.ylim(-1.2*40,1.2*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 4000)
delta = 1

## draw pin
num_pins = 61
pins = [ax.plot([], [], 'g-')[0] for n in range(num_pins)]

def draw_pin_init():
    for p in pins:
        p.set_data([0], [0])

def pin_update1(n,d,D):
    for i in range(int(n)):    
        x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))
        y = (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))
        pins[i].set_data(x,y)

def pin_update2(n,d,D,phi):
    for i in range(int(n)):    
        x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))*np.cos(phi/(n)) - (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))*np.sin(phi/(n))
        y = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))*np.sin(phi/(n)) + (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))*np.cos(phi/(n))
        pins[i].set_data(x,y)

## draw inner_pin
num_inner_pins = 10
inner_pins = [ax.plot([], [], 'k-')[0] for n in range(num_inner_pins)]

def draw_inner_pin_init():
    for p in inner_pins:
        p.set_data([0], [0])

def inner_pin_update1(n,N,rd,Rd,phi):
    for i in range(int(n)):    
        x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1))
        y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1))
        inner_pins[i].set_data(x,y)

def inner_pin_update2(n,N,rd,Rd,phi):
    for i in range(int(n)):    
        x = (rd*np.sin(t) + Rd*np.cos(2*i*np.pi/n))
        y = (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))
        inner_pins[i].set_data(x,y)

## draw drive_pin
d0, = ax.plot([0],[0],'k-')

def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data([x], [y])

#inner circleA:
num_inner_circlesA = 10
inner_circlesA = [ax.plot([], [], 'r-')[0] for n in range(num_inner_circlesA)]

def draw_inner_circleA_init():
    for p in inner_circlesA:
        p.set_data([0], [0])

def update_inner_circleA1(e,n,N,rd,Rd, phi):
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)) + e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)) + e*np.sin(phi)
        inner_circlesA[i].set_data(x,y)

def update_inner_circleA2(e,n,N,rd,Rd, phi):  
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n)) + e*np.cos(phi)
        y = ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n)) + e*np.sin(phi)
        inner_circlesA[i].set_data(x,y)

#inner circleB:
num_inner_circlesB = 10
inner_circlesB = [ax.plot([], [], 'b-')[0] for n in range(num_inner_circlesB)]

def draw_inner_circleB_init():
    for p in inner_circlesB:
        p.set_data([0], [0])

def update_inner_circleB1(e,n,N,rd,Rd, phi):
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)) - e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)) - e*np.sin(phi)
        inner_circlesB[i].set_data(x,y)

def update_inner_circleB2(e,n,N,rd,Rd, phi):
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n)) - e*np.cos(phi)
        y = ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n)) - e*np.sin(phi)
        inner_circlesB[i].set_data(x,y)

##inner pinA:
inner_pinA, = ax.plot([0], [0],'r-')
dotA, = ax.plot([0],[0], 'ro', ms=5)

def update_inner_pinA(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pinA.set_data([x], [y])
    
    x1 = (Rm+e)*np.cos(phi)+e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi)+e*np.sin(phi)
    dotA.set_data([x1], [y1])

##inner pinB:
inner_pinB, = ax.plot([0], [0],'b-')
dotB, = ax.plot([0],[0], 'bo', ms=5)

def update_inner_pinB(e,Rm, phi):
    x = (Rm+e)*np.cos(t)-e*np.cos(phi)
    y = (Rm+e)*np.sin(t)-e*np.sin(phi)
    inner_pinB.set_data([x], [y])
    
    x1 = (Rm+e)*np.cos(phi+np.pi)-e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi+np.pi)-e*np.sin(phi)
    dotB.set_data([x1], [y1])

##ehypocycloidA:
ehypocycloidA, = ax.plot([0],[0],'r-')
edotA, = ax.plot([0],[0], 'ro', ms=5)

def update_ehypocycloidA1(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1))  + e*np.cos(phis)
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1))  + e*np.sin(phis)
    ehypocycloidA.set_data([x], [y])
    edotA.set_data([x[0]], [y[0]])

def update_ehypocycloidA2(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)-e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)-e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)+(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)-(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))+ e*np.cos(phis)
    y = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)  + e*np.sin(phis)
    ehypocycloidA.set_data([x], [y])

    x1a = (rc+rm)*np.cos(phis/n)-e*np.cos((rc+rm)/rm*phis/n)
    y1a = (rc+rm)*np.sin(phis/n)-e*np.sin((rc+rm)/rm*phis/n)

    dx1a = (rc+rm)*(-np.sin(phis/n)+(e/rm)*np.sin((rc+rm)/rm*phis/n))
    dy1a = (rc+rm)*(np.cos(phis/n)-(e/rm)*np.cos((rc+rm)/rm*phis/n))

    x1 = (x1a + rd/np.sqrt(dx1a**2 + dy1a**2)*(-dy1a)) + e*np.cos(phis)
    y1 = (y1a + rd/np.sqrt(dx1a**2 + dy1a**2)*dx1a)  + e*np.sin(phis)
    edotA.set_data([x1], [y1])

##ehypocycloidB:
ehypocycloidB, = ax.plot([0],[0],'b-')
edotB, = ax.plot([0],[0], 'bo', ms=5)

def update_ehypocycloidB1(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos(-phis/(n-1))-(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin(-phis/(n-1))  - e*np.cos(phis)
    y = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin(-phis/(n-1))+(ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos(-phis/(n-1))  - e*np.sin(phis)
    ehypocycloidB.set_data([x], [y])
    edotB.set_data([x[0]], [y[0]])

def update_ehypocycloidB2(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n-1)*(RD/n)
    rm = (RD/n)
    xa = (rc+rm)*np.cos(t)+e*np.cos((rc+rm)/rm*t)
    ya = (rc+rm)*np.sin(t)+e*np.sin((rc+rm)/rm*t)

    dxa = (rc+rm)*(-np.sin(t)-(e/rm)*np.sin((rc+rm)/rm*t))
    dya = (rc+rm)*(np.cos(t)+(e/rm)*np.cos((rc+rm)/rm*t))

    x = (xa + rd/np.sqrt(dxa**2 + dya**2)*(-dya))  - e*np.cos(phis)
    y = (ya + rd/np.sqrt(dxa**2 + dya**2)*dxa)  - e*np.sin(phis)
    ehypocycloidB.set_data([x], [y])

    x1a = (rc+rm)*np.cos(phis/n)+e*np.cos((rc+rm)/rm*phis/n)
    y1a = (rc+rm)*np.sin(phis/n)+e*np.sin((rc+rm)/rm*phis/n)

    dx1a = (rc+rm)*(-np.sin(phis/n)-(e/rm)*np.sin((rc+rm)/rm*phis/n))
    dy1a = (rc+rm)*(np.cos(phis/n)+(e/rm)*np.cos((rc+rm)/rm*phis/n))

    x1 = (x1a + rd/np.sqrt(dx1a**2 + dy1a**2)*(-dy1a)) - e*np.cos(phis)
    y1 = (y1a + rd/np.sqrt(dx1a**2 + dy1a**2)*dx1a)  - e*np.sin(phis)

    edotB.set_data([x1], [y1])


axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.27, 0.5, 0.02], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.24, 0.5, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_n = Slider(ax_n, 'n', 3, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 1, 10, valinit=5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.2*0.5*sD,1.2*0.5*sD)
    ax.set_ylim(-1.2*0.5*sD,1.2*0.5*sD)



sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
sli_n.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.8, 0.0, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset()
    sli_n.reset()
    sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm


    draw_pin_init()
    draw_inner_pin_init()
    draw_inner_circleA_init()
    draw_inner_circleB_init()
    
    pin_update2(sN,sd,sD,phi)
    update_inner_pinA(se,sRm, phi)
    update_inner_pinB(se,sRm, phi)

    inner_pin_update2(sn,sN,srd,sRd,phi)
    drive_pin_update(sRm)

    update_inner_circleA2(se,sn,sN,srd,sRd, phi)
    update_inner_circleB2(se,sn,sN,srd,sRd, phi)

    update_ehypocycloidA2(se,sN,sD,sd, phi)
    update_ehypocycloidB2(se,sN,sD,sd, phi)

    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=150)
dpi=100
plt.show()
