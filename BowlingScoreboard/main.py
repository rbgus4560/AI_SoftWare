import flet as ft
import random

from game_engine import BowlingGame
from ui_formatter import get_frame_displays

# =====================================================================
# UI 화면 구성 및 이벤트 제어 (Flet 0.84 기준)
# =====================================================================
def main(page: ft.Page):
    # 앱 기본 설정
    page.title = "볼링 스코어보드"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30

    # 점수 계산기
    game = BowlingGame()
    
    # 상단 상태 텍스트
    status_text = ft.Text("1 프레임 - 1번째 투구", size=24, weight=ft.FontWeight.BOLD)
    
    # 점수판 컨테이너
    scoreboard_container = ft.Container(padding=10)

    def update_scoreboard_ui():
        """
        현재 게임 데이터를 읽어와서 스코어보드 표를 동적으로 다시 그립니다.
        """
        scores = game.calculate_scores()             
        displays = get_frame_displays(game.rolls)    
        
        frame_columns = []
        for i in range(10): 
            disp = displays[i] if i < len(displays) else ['', '', ''] if i == 9 else ['', '']
            score = str(scores[i]) if i < len(scores) else ' ' 
            
            # 투구 기록 네모 상자 (Row)
            roll_boxes = []
            for text in disp:
                roll_boxes.append(
                    ft.Container(
                        content=ft.Text(text if text else " ", size=14, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        width=25, height=25,
                        border=ft.Border.all(1, ft.Colors.GREY_400),
                        alignment=ft.Alignment.CENTER 
                    )
                )

            # 프레임 1개 조립 (Column: 숫자 + 투구상자 + 점수)
            frame_container = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"{i+1}", size=14, color=ft.Colors.BLUE_700, text_align=ft.TextAlign.CENTER),
                        ft.Row(roll_boxes, spacing=0, alignment=ft.MainAxisAlignment.CENTER), 
                        ft.Text(score, size=18, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
                    ],
                    alignment=ft.MainAxisAlignment.START, 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                    spacing=5
                ),
                width=85 if i == 9 else 65, 
                border=ft.Border.all(1, ft.Colors.BLACK), 
                padding=5,
                bgcolor=ft.Colors.WHITE 
            )
            frame_columns.append(frame_container) 
            
        # 프레임 상자 가로 나열
        scoreboard_container.content = ft.Row(frame_columns, spacing=0, alignment=ft.MainAxisAlignment.CENTER)

    def on_roll_click(e):
        if game.is_game_over:
            return

        # 서 있는 핀 안에서 랜덤 시뮬레이션 후 game_engine.py에 전송
        knocked_down = random.randint(0, game.pins_standing)
        game.roll(knocked_down)
        
        # 화면 최신화
        update_scoreboard_ui()
        
        # 게임 상태 체크 및 텍스트 업데이트
        if game.is_game_over:
            scores = game.calculate_scores()
            final_score = scores[-1] if scores else 0
            if final_score == 300: 
                status_text.value = "PERFECT GAME!!! 300점!"
                status_text.color = ft.Colors.RED_700
            else: 
                status_text.value = f"게임 종료! 최종 점수: {final_score}점"
            roll_btn.disabled = True 
        else:
            status_text.value = f"{game.current_frame} 프레임 - {game.throw_in_frame}번째 투구"

        page.update() 

    def on_reset_click(e):
        nonlocal game
        game = BowlingGame() 
        status_text.value = "1 프레임 - 1번째 투구"
        status_text.color = ft.Colors.BLACK
        roll_btn.disabled = False 
        update_scoreboard_ui() 
        page.update()

    roll_btn = ft.Button("공 굴리기", on_click=on_roll_click, width=200, height=50)
    reset_btn = ft.Button("게임 초기화", on_click=on_reset_click)

    update_scoreboard_ui()

    # 페이지 조립
    page.add(
        ft.Text("Bowling Scoreboard", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT), 
        status_text,
        ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
        scoreboard_container, 
        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
        ft.Row([roll_btn, reset_btn], alignment=ft.MainAxisAlignment.CENTER) 
    )

if __name__ == "__main__":
    ft.run(main)