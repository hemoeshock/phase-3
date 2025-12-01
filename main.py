import pygame as pg
import sys

win_width, win_height = 800, 200

def main():
    pg.init()
    dis_surf = pg.display.set_mode((win_width, win_height))
    pg.display.set_caption("Open Loop Control - Step 1")
    clock = pg.time.Clock()

    bg = pg.Surface((win_width, win_height))
    bg.fill("white")

    game(bg, dis_surf, clock)

def game(background, display_surface, clock):
    # Declare variables
    position = 100         # starting point
    velocity = 0
    u = 0
    target = 600           # for drawing only
    Kp = 0.05              # porpotional gain factor
    Ki = 0.0002            # integral gain factor
    Kd = 0.05
    integral_error = 0
    previous_error = 0
    tau = 2.0          # ثابت الزمن للنظام (كلما كبر صار أبطأ)
    plant_gain = 3.0    # كسب النظام K
    dt = 1 / 60.0   # الزمن لكل فريم (بما إننا نعمل tick(60))




    running = True
    # Game loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

        # --- Control System ---
        error = target - position       # 1) compute error
        derivative_error = error - previous_error
        integral_error += error
       
        # Anti-windup clamp
        if integral_error > 2000:
            integral_error = 2000
        if integral_error < -2000:
            integral_error = -2000

        if derivative_error > 100:
            derivative_error = 100
        if derivative_error < -100:
            derivative_error = -100

       
        u = (Kp * error) + (Ki * integral_error) + (Kd * derivative_error)            # 2) proportional control
        previous_error = error
        # نموذج موتور من الدرجة الأولى على السرعة:
        velocity += (-velocity / tau + plant_gain * u / tau) * dt
        position += velocity * dt   # 3) update plant
          
  


        # --- Drawing ---
        display_surface.blit(background, (0, 0))
        pg.draw.line(display_surface, "black", (50, 100), (750, 100), 3)
        pg.draw.line(display_surface, "green", (target, 75), (target, 125), 4)
        pg.draw.circle(display_surface, "red", (int(position), 100), 10)

        # --- Update display ---
        print(
    "pos:", round(position,1),
    " err:", round(error,1),
    " I:", round(integral_error,1),
    " D:", round(derivative_error,1),
    " vel:", round(velocity,3)
)

        pg.display.update()
        clock.tick(60)


        












if __name__ == "__main__":
    main()