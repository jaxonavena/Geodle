from itertools import count
import pygame
from sys import exit
from comparison2 import Comparison
from box import Box

class Game:
  def __init__(self, country_info_list):
    self.country_info_list = country_info_list
    pygame.init()
    pygame.key.set_repeat(500, 100)


  def make_box_array(self):
    #Output list
    box_class_list = []
    index = 0
    y = 300
    for _ in range(10):
      box_class_list.append([])
      x = 0
      for _ in range(5):
        new_box = Box(x,y)
        box_class_list[index].append(new_box)
        x += 200
      index += 1
      y += 52
    return box_class_list


  def run(self):
    #Misc.
    self.comparison = Comparison(self.country_info_list)
    self.screen = pygame.display.set_mode((1000,1000))
    pygame.display.set_caption("Geodle")
    self.clock = pygame.time.Clock()
    self.game_active = True
    self.guess_count = 0
    self.box_row_list = self.make_box_array()
    self.box_row_index = 0


    #fonts
    header_font = pygame.font.Font(None, 80)
    input_font = pygame.font.Font(None,40)
    self.guess_count_font = pygame.font.Font(None,25)
    self.big_word_font = pygame.font.Font(None,22)

    #input box stuff
    self.user_text = "ENTER GUESS..."
    input_base_color = pygame.Color(82, 95, 238) #purpley blue
    input_active_color = pygame.Color(180, 185, 243) #lighter purpley blue
    current_input_color = input_base_color
    input_active = False

    #invalid entry message
    self.error_message_check = False
    self.error_message = "Entry Not Included In Word Bank" if self.error_message_check else ""



    #SURFACES
    self.background_surface = pygame.image.load('hackathon2022images/background_surface.jpg').convert_alpha()
    self.header_shadow_surface = header_font.render("GEODLE", True, (72,77,67))
    self.header_surface = header_font.render("GEODLE", True, (120, 194, 58)) #text, AA?, Color
    self.user_text_surface = input_font.render(self.user_text,True,"Black")
    self.guess_count_surface = self.guess_count_font.render(f"Guess Count: {str(self.guess_count)}/10",True,"Black")
    self.categories_surface = self.guess_count_font.render("NAME                          HEMISPHERE                  CONTINENT                         AREA                       POPULATION", True, "Black")

    self.invalid_entry_surface = self.guess_count_font.render(self.error_message,True,"Black")

    self.winner_screen_surface = input_font.render("YOU ARE NOW THE WORLD'S GREATEST GEODLER!",True,(54, 189, 225))
    self.winner_screen_shadow_surface = input_font.render("YOU ARE NOW THE WORLD'S GREATEST GEODLER!",True,(12, 105, 130 ))

    self.loser_screen_surface = input_font.render("SORRY, YOU'RE OUT OF GUESSES!",True,"Red")
    self.loser_screen_shadow_surface = input_font.render("SORRY, YOU'RE OUT OF GUESSES!",True,(112, 5, 0))

    self.secret_country_surface = input_font.render(f"The Geodle Was: {self.comparison.secretcountry.name}!",True,"Red")
    self.secret_country_shadow_surface = input_font.render(f"The Geodle Was: {self.comparison.secretcountry.name}!",True,(112, 5, 0))

    self.instructions_surface = self.guess_count_font.render("Press SPACE To Play Again", True, "Black")

    self.clout_surface = pygame.image.load('hackathon2022images/clout.jpg').convert_alpha()
    self.clout_surface = pygame.transform.rotozoom(self.clout_surface,0,.25)

    self.map_surface = pygame.image.load('hackathon2022images/map.png').convert_alpha()
    self.map_surface = pygame.transform.rotozoom(self.map_surface,0,.06)

    #green/yellow/grey boxes
    self.green_box_surface = pygame.image.load("hackathon2022images/correct_box2.png").convert_alpha()
    self.yellow_box_surface = pygame.image.load("hackathon2022images/close_box2.png").convert_alpha()
    self.grey_box_surface = pygame.image.load("hackathon2022images/incorrect_box2.png").convert_alpha()


    #RECTS
    self.input_rect = pygame.Rect(260,120, 500, 100)
    self.input_rect_shadow = pygame.Rect(258,118,504,104)



    while True:
      if self.game_active:

        #BLIT/DRAW
        self.screen.blit(self.background_surface,(0,0))
        self.screen.blit(self.header_shadow_surface,(403,53))
        self.screen.blit(self.header_surface,(400,50))
        self.screen.blit(self.guess_count_surface, (800,65))
        self.screen.blit(self.categories_surface, (70,250))
        self.screen.blit(self.invalid_entry_surface, (400, 230))
        self.screen.blit(self.map_surface,(53,125))

        for row in self.box_row_list:
          for box in row:
            if box.color == "green":
              self.screen.blit(self.green_box_surface, (box.x,box.y))
            elif box.color == "yellow":
              self.screen.blit(self.yellow_box_surface, (box.x,box.y))
            elif box.color == "grey":
              self.screen.blit(self.grey_box_surface, (box.x,box.y))
            if len(box.text) > 16:
              self.box_text_surface = self.big_word_font.render(box.text,True,"Black")
            else:
              self.box_text_surface = self.guess_count_font.render(box.text,True,"Black")
            self.screen.blit(self.box_text_surface, (box.x+5,box.y+20))


        #user text
        pygame.draw.rect(self.screen, (1, 42, 151), self.input_rect_shadow) #draw input area's shadow
        pygame.draw.rect(self.screen, current_input_color, self.input_rect) #where to draw, color, input_rect, border size
        current_input_color = input_active_color if input_active else input_base_color
        self.screen.blit(self.user_text_surface, (self.input_rect.x + 8, self.input_rect.y + 35)) #(265,150)
        # self.input_rect.w = max(500,self.user_text_surface.get_width() + 10) stretchy thing



      #EVENTS
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()

        #CLICKING
        if self.guess_count < 10:
          if self.game_active:
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
                    self.game_active = False
                  else:
                    self.output_list = self.comparison.compare_all(self.user_text)
                    if self.output_list == "invalid":
                      self.error_message_check = True
                      self.invalid_entry_surface = self.guess_count_font.render(self.error_message,True,"Black")
                    else:
                      item_index = 0
                      for color in self.output_list:
                        if color == "green":
                          self.box_row_list[self.box_row_index][item_index].color = "green"
                        elif color == "yellow":
                          self.box_row_list[self.box_row_index][item_index].color = "yellow"
                        elif color == "grey":
                          self.box_row_list[self.box_row_index][item_index].color = "grey"
                        item_index += 1
                      self.box_row_index += 1

                      for country in self.comparison.country_info_list:
                        if country.name == self.user_text:
                          area_arrow = ""
                          pop_arrow = ""

                          #population arrow
                          if self.output_list[5] == "higher":
                            pop_arrow = "^"
                          elif self.output_list[5] == "lower":
                            pop_arrow ="v"

                          #area arrow
                          if self.output_list[6] == "higher":
                            area_arrow = "^"
                          elif self.output_list[6] == "lower":
                            area_arrow = "v"


                          self.box_row_list[self.guess_count][0].text = country.name
                          self.box_row_list[self.guess_count][1].text = country.hemisphere
                          self.box_row_list[self.guess_count][2].text = country.continent
                          self.box_row_list[self.guess_count][3].text = f"{country.area}   ---    {area_arrow}"
                          self.box_row_list[self.guess_count][4].text = f"{country.pop}   ---    {pop_arrow}"

                      self.guess_count += 1
                      self.guess_count_surface = self.guess_count_font.render(f"Guess Count: {str(self.guess_count)}/10",True,"Black")
                  self.user_text = ""


                #regular typing
                else:
                  if len(self.user_text) < 26:
                    self.user_text += (event.unicode).upper()
                self.user_text_surface = input_font.render(self.user_text,True,"Black")

          else: #End Win Screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
              self.run()

            self.screen.blit(self.background_surface,(0,0))

            self.screen.blit(self.winner_screen_shadow_surface,(167,402))
            self.screen.blit(self.winner_screen_surface,(165,400))

            self.screen.blit(self.instructions_surface,(390,550))
            self.screen.blit(self.clout_surface,(385,-40))
        else: #End Lose Screen
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
              self.run()

            self.screen.blit(self.background_surface,(0,0))

            self.screen.blit(self.loser_screen_shadow_surface,(277,202))
            self.screen.blit(self.loser_screen_surface,(275,200))

            self.screen.blit(self.secret_country_shadow_surface,(302,302))
            self.screen.blit(self.secret_country_surface,(300, 300))

            self.screen.blit(self.instructions_surface,(390,550))
            self.game_active = False




      pygame.display.flip()
      self.clock.tick(60)


