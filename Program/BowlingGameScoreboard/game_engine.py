# =====================================================================
# 볼링의 핀 개수, 프레임 이동, 점수 계산 등 순수 '규칙'만을 다루는 클래스.
# =====================================================================
class BowlingGame:
    def __init__(self):
        # 이번 게임에서 굴린 '모든 투구의 쓰러진 핀 개수'를 순서대로 기록하는 리스트입니다.
        self.rolls = []           
        
        # 현재 진행 중인 프레임 번호입니다. (1부터 시작해서 10까지 증가)
        self.current_frame = 1
        
        # 현재 프레임에서 몇 번째로 공을 던지는 중인지 나타냅니다.
        self.throw_in_frame = 1   
        
        # 현재 레인에 서 있는 핀의 개수입니다. (매 프레임 시작 시 10으로 초기화됨)
        self.pins_standing = 10   
        
        # 10프레임 투구가 모두 끝나면 True로 바뀌어 더 이상 공을 굴릴 수 없게 합니다.
        self.is_game_over = False

    def roll(self, pins): # 피
        """
        사용자가 공을 굴려 핀을 쓰러뜨렸을 때 호출되는 핵심 규칙 함수입니다.
        """
        if self.is_game_over:
            return

        self.rolls.append(pins)


        # 1 ~ 9 프레임의 일반적인 게임 진행 로직
        if self.current_frame < 10:
            if self.throw_in_frame == 1: 
                if pins == 10:  
                    self.current_frame += 1
                    self.pins_standing = 10 
                else:
                    self.throw_in_frame = 2
                    self.pins_standing -= pins 
            
            else: 
                self.current_frame += 1
                self.throw_in_frame = 1 
                self.pins_standing = 10 
                
        # 10 프레임의 특수 게임 진행 로직 (보너스 투구 포함)
        else:
            if self.throw_in_frame == 1: 
                if pins == 10: 
                    self.pins_standing = 10 
                else:
                    self.pins_standing -= pins
                self.throw_in_frame = 2
                
            elif self.throw_in_frame == 2: 
                if self.rolls[-2] == 10 or self.rolls[-2] + pins == 10:
                    if pins == 10 or self.rolls[-2] + pins == 10:
                        self.pins_standing = 10 
                    else:
                        self.pins_standing -= pins
                    self.throw_in_frame = 3 
                else:
                    self.is_game_over = True 
                    
            elif self.throw_in_frame == 3: 
                self.is_game_over = True 

    def calculate_scores(self):
        scores = []
        roll_idx = 0     
        total_score = 0  

        for frame in range(10): 
            if roll_idx >= len(self.rolls):
                break
                
            # [조건 1: 스트라이크] 
            if self.rolls[roll_idx] == 10: 
                if roll_idx + 2 < len(self.rolls):
                    total_score += 10 + self.rolls[roll_idx+1] + self.rolls[roll_idx+2]
                    scores.append(total_score)
                    roll_idx += 1 
                else:
                    break 
                
            # [조건 2: 스페어] 
            elif roll_idx + 1 < len(self.rolls) and self.rolls[roll_idx] + self.rolls[roll_idx+1] == 10: 
                if roll_idx + 2 < len(self.rolls):
                    total_score += 10 + self.rolls[roll_idx+2]
                    scores.append(total_score)
                    roll_idx += 2 
                else:
                    break 
                
            # [조건 3: 일반 프레임] 
            else: 
                if roll_idx + 1 < len(self.rolls):
                    total_score += self.rolls[roll_idx] + self.rolls[roll_idx+1]
                    scores.append(total_score)
                    roll_idx += 2 
                else:
                    break 
                
        return scores