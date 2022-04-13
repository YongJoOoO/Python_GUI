import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정 
screen_width = 480 #가로 크기 
screen_height = 640 #세로 크기 
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정 
pygame.display.set_caption("YongJu Game ") #게임이름 

#FPS 
clock = pygame.time.Clock()

#배경 이미지 불러오기 
background = pygame.image.load("C:\\Users\\LG\\OneDrive\\바탕 화면\\pygame\\pygame_myGame\\background.png")

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\LG\\OneDrive\\바탕 화면\\pygame\\pygame_myGame\\character.png")
character_size = character.get_rect().size #알아서 캐릭터 규격 알아옴
character_width = character_size[0] #가로
character_height = character_size[1] #세로
character_x_pos = (screen_width / 2) - (character_width/2) #윈도우 규격의 절반에 위치
character_y_pos = screen_height - character_height # 윈도우 가장 밑에 위치

#캐릭터 이동할 좌표
to_x = 0
to_y = 0
# 이동 속도 
character_speed = 0.6

# 이벤트 루프
running = True #게임이 진행 중 ? 
while running:
    dt = clock.tick(30)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 ? 
        if event.type == pygame.QUIT: #창 닫으면
            running = False #게임 진행 False값 

        if event.type == pygame.KEYDOWN: #키 이벤트 처러ㅣ 
            if event.key == pygame.K_LEFT: #왼쪽 키
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #오른쪽 키
                to_x += character_speed
            elif event.key == pygame.K_UP: # 위쪽 키
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #아래쪽 키 
                to_y += character_speed
        if event.type == pygame.KEYUP: #user가 방향키 손에서 떼면 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #캐릭터의 가로 경계값 처리 
    if character_x_pos < 0:
        charater_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #캐릭터의 세로 경계값 처리 
    if character_y_pos < 0:
        charater_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0)) #내가 설정한 배경 그리기 
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() #pygame 은 매번 frame 다시 그려줘야 함

# pygame 종료
pygame.quit()