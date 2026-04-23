# =====================================================================
# 어댑터/번역기
# UI에 예쁘게 그리기 위해 [10, 7, 3] 같은 숫자를 ['X', '', '7', '/'] 로 변환.
#   * 스트라이크, 스페어 등
# =====================================================================
def get_frame_displays(rolls):
    frames = []
    idx = 0
    
    for f in range(10):
        if idx >= len(rolls): 
            break

        # 1~9 프레임 변환 로직     
        if f < 9: 
            if rolls[idx] == 10:
                frames.append(['X', '']) # 스트라이크
                idx += 1
            elif idx + 1 < len(rolls):
                r1, r2 = rolls[idx], rolls[idx+1]
                d1 = '-' if r1 == 0 else str(r1) 
                d2 = '/' if r1 + r2 == 10 else ('-' if r2 == 0 else str(r2)) # 스페어
                frames.append([d1, d2])
                idx += 2
            else:
                d1 = '-' if rolls[idx] == 0 else str(rolls[idx])
                frames.append([d1, ''])
                idx += 1

        # 10 프레임 변환 로직        
        else: 
            frame_rolls = rolls[idx:] 
            disp_rolls = []
            
            for i, r in enumerate(frame_rolls):
                if r == 10:
                    disp_rolls.append('X')
                elif i == 1 and frame_rolls[0] + frame_rolls[1] == 10 and frame_rolls[0] != 10:
                    disp_rolls.append('/') 
                elif i == 2 and frame_rolls[1] != 10 and frame_rolls[1] + frame_rolls[2] == 10:
                    disp_rolls.append('/') 
                else:
                    disp_rolls.append('-' if r == 0 else str(r))
            
            while len(disp_rolls) < 3:
                disp_rolls.append('')
            frames.append(disp_rolls)
            
    return frames