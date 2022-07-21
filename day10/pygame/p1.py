import pygame
import sys

# 色定義(rgb)
WHITE=(255,255,255)
BLACK=(0,0,0)

def main():
	pygame.init() # 初期化処理
	pygame.display.set_caption('My Game') # タイトルセット
	screen=pygame.display.set_mode((800,600)) # Surface(描画面)をセット
	clock=pygame.time.Clock() # ゲーム時間管理オブジェクト
	font=pygame.font.Font(None,80) # フォント設定(Noneでデフォルトフォント（日本語NG))
	tmr=0

	while True:
		tmr=tmr+1
		# 以下のfor文はpygameで処理を終える時の定型
		for event in pygame.event.get():
			# ウインドウを閉じるxボタンが押されたら
			if event.type==pygame.QUIT:
				pygame.quit() # pygameを終える
				sys.exit() # sysを終える
		# 文字列を書いたSurfaceを作成(第二引数はアンチエイリアス)
		txt=font.render(str(tmr),True,WHITE) 
		screen.fill(BLACK) # 画面を黒で塗りつぶす
		screen.blit(txt,[300,200]) # blitで文字列を書いたsurfaceを配置(第二引数は位置)
		pygame.display.update() # 描画を更新
		clock.tick(10) # １秒間に約10回のフレームレート(10fps)

# このファイルを直接実行された場合にmain()が走る
if __name__ == '__main__':
	main()
