import matplotlib.pyplot as plt
import numpy as np


dt = 0.01
t_end = 5.0
t = np.arange(0, t_end, dt)
position = 0.0   # x
velocity = 0.0   # x_dot
m = 1.0       # الكتلة
k = 20.0      # ثابت الزنبرك
u = 0         # لا نستخدم step الآن
c = 2*np.sqrt(k * m)       # معامل التخميد
positions = []
velocities = []
times = []
# PID parameters
Kp = 3.0
Ki = 0.0
Kd = 0.5

integral_error = 0.0
previous_error = 0.0

target = 1.0     # نريد موضع 1 متر مثلاً


plt.ion()
plt.plot(times, positions)

for current_t in t:

    error = target - position
    integral_error += error * dt
    derivative_error = (error - previous_error) / dt
    previous_error = error

    u = Kp*error + Ki*integral_error + Kd*derivative_error

    accel = (u - (k*position)-(velocity*c))/m
    velocity += accel * dt
    position += velocity * dt

    times.append(current_t)
    positions.append(position)
    velocities.append(velocity)

    plt.plot(times, positions)
    plt.pause(0.09)
    print('velocity:',velocity,'position:',position,'error:',error)
plt.ioff()
plt.show() 




