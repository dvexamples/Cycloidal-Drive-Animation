import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
ax.set_title('Reduction ratio '+(str(int(10)-1))+':1')
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.2*40,1.2*40)
plt.ylim(-1.2*40,1.2*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 4000)
delta = 1
Output_fig = 0

## draw pin
num_pins = 61
pins = [ax.plot([], [], 'k-')[0] for n in range(num_pins)]
def draw_pin_init():
    for p in pins:
        p.set_data([0], [0])

def pin_update(n,d,D):
    for i in range(int(n)):    
        x = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))
        y = (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))
        pins[i].set_data(x,y)

## draw inner_pin
num_inner_pins = 10
inner_pins = [ax.plot([], [], 'g-')[0] for n in range(num_inner_pins)]
def draw_inner_pin_init():
    for p in inner_pins:
        p.set_data([0], [0])

def inner_pin_update(n,N,rd,Rd,phi):
    for i in range(int(n)):    
        x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1))
        y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1))
        inner_pins[i].set_data(x,y)

## draw drive_pin
d0, = ax.plot([0],[0],'k-')
def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data([x], [y])

#inner circle:
num_inner_circles = 10
inner_circles = [ax.plot([], [], 'r-')[0] for n in range(num_inner_circles)]
def draw_inner_circle_init():
    for p in inner_circles:
        p.set_data([0], [0])

def update_inner_circle(e,n,N,rd,Rd, phi):
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)) + e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)) + e*np.sin(phi)
        inner_circles[i].set_data(x,y)
 
##inner pin:
inner_pin, = ax.plot([0],[0],'r-')
dot, = ax.plot([0],[0], 'ro', ms=5)
def update_inner_pin(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pin.set_data([x], [y])
    
    x1 = (Rm+e)*np.cos(phi)+e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi)+e*np.sin(phi)
    dot.set_data([x1], [y1])

##ehypocycloid:
ehypocycloid, = ax.plot([0],[0],'r-')
edot, = ax.plot([0],[0], 'ro', ms=5)
def update_ehypocycloid(e,n,D,d, phis):
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
    ehypocycloid.set_data([x], [y])
    edot.set_data([x[0]], [y[0]])

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
sli_D = Slider(ax_D, 'D', 5, 200, valinit=80,valstep=delta)

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
    ax.set_title('Reduction ratio '+(str(int(sN)-1))+':1')
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

resetax = plt.axes([0.84, 0.02, 0.12, 0.04])
output_tax = plt.axes([0.84, 0.08, 0.12, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
button_output = Button(output_tax, 'Equation', color=axcolor, hovercolor='0.975')

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

def output(event):
    global Output_fig
    Output_fig = 1

button.on_clicked(reset)
button_output.on_clicked(output)

def animate(frame):
    global Output_fig
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

    if  Output_fig == 1:
        RD=sD/2
        rd=sd/2
        rc = (sN-1)*(RD/sN)
        rm = (RD/sN)
        R_EN = RD/(se*sN)
        X = "({}*cos(t)) - ( {}*cos( t+arctan( sin({}*t)/({} - cos({}*t)) ) ) ) - ({}*cos({}*t)) ".format((rc+rm),rd,(1-sN),R_EN,(1-sN),se,sN)
        Y = "(-{}*sin(t)) + ( {}*sin( t+arctan( sin({}*t)/({} - cos({}*t)) ) ) ) + ({}*sin({}*t)) ".format((rc+rm),rd,(1-sN),R_EN,(1-sN),se,sN)
        print(X)
        print(Y)
        Output_fig = 0

    draw_pin_init()
    draw_inner_pin_init()
    draw_inner_circle_init()
    pin_update(sN,sd,sD)
    update_inner_pin(se,sRm, phi)
    inner_pin_update(sn,sN,srd,sRd,phi)
    drive_pin_update(sRm)
    update_inner_circle(se,sn,sN,srd,sRd, phi)
    update_ehypocycloid(se,sN,sD,sd, phi)


    fig.canvas.draw_idle()

ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
plt.show()
