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
    velocity = 2           # constant open-loop speed
    target = 600           # for drawing only


    running = True
    # Game loop
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    velocity += 0.5
                if event.key == pg.K_LEFT:
                    velocity -= 0.5

        # Clamp velocity
        if velocity > 10:
            velocity = 10
        if velocity < -10:
            velocity = -10

        
        position += velocity

        # Draw
        display_surface.blit(background, (0, 0))
        pg.draw.line(display_surface, "black", (50,100), (750,100),3)
        pg.draw.line(display_surface, "green",
             (target, 75), (target, 125), 4)
        pg.draw.circle(display_surface, "red",
               (int(position), 100), 10)
        print("pos:", position, " vel:", velocity)

        # Update
        pg.display.update()
        clock.tick(60)

        












if __name__ == "__main__":
    main()