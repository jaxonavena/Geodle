import pygame
from sys import exit
from comparison import Comparison

class Game:
  def __init__(self, country_info_list):
    self.comparison = Comparison(country_info_list)
    pygame.init()
    pygame.key.set_repeat(500, 100)


  def run(self):
    #Misc.
    self.screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Geodle")
    self.clock = pygame.time.Clock()
    self.game_active = True
    self.guess_count = 0
    self.current_available_y = 320 #for when guesses start being outputted

    #Output lists
    self.guess_bool_list = []
    self.guess_text_list = []

    #fonts
    header_font = pygame.font.Font(None, 80)
    input_font = pygame.font.Font(None,40)
    self.guess_count_font = pygame.font.Font(None,25)

    #input box stuff
    self.user_text = "ENTER GUESS..."
    input_base_color = pygame.Color(82, 95, 238) #purpley blue
    input_active_color = pygame.Color(180, 185, 243) #lighter purpley blue
    current_input_color = input_base_color
    input_active = False

    #invalid entry message
    self.error_message_check = False
    self.error_message = "Entry Not Included In Word Bank" if self.error_message_check else "spot"



    #SURFACES
    self.background_surface = pygame.image.load('hackathon2022images/background_surface.jpg').convert_alpha()
    self.header_shadow_surface = header_font.render("GEODLE", True, (72,77,67))
    self.header_surface = header_font.render("GEODLE", True, (120, 194, 58)) #text, AA?, Color
    self.user_text_surface = input_font.render(self.user_text,True,"Black")
    self.guess_count_surface = self.guess_count_font.render(f"Guess Count: {str(self.guess_count)}",True,"Black")
    self.categories_surface = self.guess_count_font.render("NAME             HEMISPHERE              CONTINENT             AREA              POPULATION", True, "Black")
    self.invalid_entry_surface = self.guess_count_font.render(self.error_message,True,"Black")
    #green/yellow/grey boxes
    self.green_box_surface = pygame.image.load("hackathon2022images/correct_box.png").convert_alpha()
    self.green_box_surface = pygame.transform.rotozoom(self.green_box_surface, 0, 2)
    self.yellow_box_surface = pygame.image.load("hackathon2022images/close_box.png").convert_alpha()
    self.yellow_box_surface = pygame.transform.rotozoom(self.yellow_box_surface, 0, 2)
    self.grey_box_surface = pygame.image.load("hackathon2022images/incorrect_box.png").convert_alpha()
    self.grey_box_surface = pygame.transform.rotozoom(self.grey_box_surface, 0, 2)



    #RECTS
    self.input_rect = pygame.Rect(260,120, 500, 100)
    self.input_rect_shadow = pygame.Rect(258,118,504,104)



    while True:
      # pygame.display.update()


      if self.game_active:

        #BLIT/DRAW
        self.screen.blit(self.background_surface,(0,0))
        self.screen.blit(self.header_shadow_surface,(403,53))
        self.screen.blit(self.header_surface,(400,50))
        self.screen.blit(self.guess_count_surface, (800,50))
        self.screen.blit(self.categories_surface, (150,250))
        self.screen.blit(self.invalid_entry_surface, (200, 500))

        #user text
        pygame.draw.rect(self.screen, (1, 42, 151), self.input_rect_shadow) #draw input area's shadow
        pygame.draw.rect(self.screen, current_input_color, self.input_rect) #where to draw, color, input_rect, border size
        current_input_color = input_active_color if input_active else input_base_color
        self.screen.blit(self.user_text_surface, (self.input_rect.x + 10, self.input_rect.y + 35)) #(265,150)
        # self.input_rect.w = max(500,self.user_text_surface.get_width() + 10) stretchy thing

        self.display_output()

      #EVENTS
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

        #CLICKING
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.input_rect.collidepoint(event.pos):
            input_active = True
          else:
            input_active = False

        #TYPING
        if input_active: #if clicked on text box

          #if it hasn't been typed in yet clear it once clicked on
          if self.user_text == "ENTER GUESS...":
            self.user_text = ""
            self.user_text_surface = input_font.render(self.user_text,True,"Black")

          #editing guess
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
              # get text input from 0 to -1 i.e. end.
              self.user_text = self.user_text[:-1]

            elif event.key == pygame.K_RETURN:
              #run
              if self.comparison.win(self.user_text):
                #RETURN WINNING SCREEN ##################
                print("WINNER WINNER CHICKEN PETE")
              else:
                self.output_list = self.comparison.compare_all(self.user_text)
                if self.output_list == "invalid":
                  self.error_message_check = True
                  self.invalid_entry_surface = self.guess_count_font.render(self.error_message,True,"Black")
                  print("Entry bad")
                else:
                  print(self.output_list)
              self.user_text = ""
              self.guess_count += 1
              self.guess_count_surface = self.guess_count_font.render(f"Guess Count: {str(self.guess_count)}",True,"Black")

            #regular typing
            else:
              self.user_text += (event.unicode).upper()
            self.user_text_surface = input_font.render(self.user_text,True,"Black")

      pygame.display.flip()
      self.clock.tick(60)


  def add_output(self, guess):
    self.current_available_x = 150
    #box surfaces
    bool_list = [True, False, True, False, True] #name, hemi, cont, area, pop
    name_box_text = guess
    hemisphere_box_text = "Hemi"
    continent_box_text = "Cont"
    area_box_text = "100,000km"
    pop_box_text = "12 ppl"
    text_list = [name_box_text,hemisphere_box_text,continent_box_text,area_box_text,pop_box_text]

    index = 0
    for bool in bool_list:
      if bool == True:
        self.screen.blit(self.green_box_surface, (self.current_available_x,self.current_available_y))
      elif bool == False:
        self.screen.blit(self.grey_box_surface, (self.current_available_x,self.current_available_y))
      else:
        self.screen.blit(self.yellow_box_surface, (self.current_available_x,self.current_available_y))

      self.box_text_surface = self.guess_count_font.render(text_list[index],True,"Black")
      self.screen.blit(self.box_text_surface, (self.current_available_x,self.current_available_y))
      self.current_available_x += 100
      index += 1
    self.current_available_y += 70

  def display_output(self):
    pass