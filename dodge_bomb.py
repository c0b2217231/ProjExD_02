import random
import sys
from tkinter import messagebox
import pygame as pg

# 練習４
delta = {
        pg.K_UP : (0,-1),
        pg.K_DOWN : (0, +1),
        pg.K_LEFT : (-1, 0),
        pg.K_RIGHT : (+1, 0)

}

# 追加機能１（未完成）
size = {
    
}

def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値をタプルで返す関数
    引数１：画面SurfaceのRect
    引数２：こうかとん、または爆弾SurfaceのRect
    戻り値：横方向、縦方向のはみ出し判定結果（画面内：True/画面外：False)
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate




def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1400, 800))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect() # 練習４
    kk_rct.center = 900, 400 # 練習4
    
    # タイマーを作りたい（未完成）
    clock = pg.time.Clock()
    total_time = 10 
    game_font = pg.font.Font(None, 40)
    start_time = pg.time.get_ticks()# 始まる時間
    elapsed_time = (pg.time.get_ticks() - start_time) / 1000 # 経過時間表示（1000で分ける）
    timer = game_font.render(str(int(total_time- elapsed_time)),True, (255,255,255))
    screen.blit(timer, (10,10))
    
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0)) # 練習1
    x, y = random.randint(0, 1400), random.randint(0, 800) # 練習２,練習５の時に画面のサイズを調整
    #screen.blit(bb_img, [x, y])# 練習２
    vx, vy = +1, +1 # 練習３
    bb_rct = bb_img.get_rect() # 練習３
    bb_rct.center = x, y # 練習３
    tmr = 0

    while True:
        for event in pg.event.get(): # 必ず書くこと
            if event.type == pg.QUIT:
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct) # 練習4
        # screen.blit(bg_img, [x, y])
        bb_rct.move_ip(vx, vy) # 練習３
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko: # 横方向にはみ出ていたら
            vx *= -1
        if not tate: # 縦方向に這い出ていたら
            vy *= -1
        screen.blit(bb_img, bb_rct) # 練習3
        if kk_rct.colliderect(bb_rct): # 練習６
            messagebox.showinfo("終わり","ゲームオーバー")
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()