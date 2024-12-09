#Oluwapelumi, you should use a software to draw the flowcharts. 
#Please add transition for the game as well.
#You can re draw and email me for a better grade.

# Oluwapelumi Omidiji

class Chapter1:
    def start_chapter_1(self):
        print("Start of Chapter 1")
        self.receive_transmission()

    def receive_transmission(self):
        print("Lira receives a weird transmission in her workshop.")
        self.search_workshop()

    def search_workshop(self):
        print("Lira searches her workshop for kits and upgrades.")
        self.trace_signal()

    def trace_signal(self):
        print("Lira traces the signal to a nearby unoccupied zone.")
        self.engage_with_locals()

    def engage_with_locals(self):
        print("Lira engages with locals to learn about disturbances.")
        self.discover_clues()

    def discover_clues(self):
        print("Lira discovers clues pointing to a mysterious faction behind the disturbances.")
        self.end_chapter_1()

    def end_chapter_1(self):
        print("End of Chapter 1")
        self.suspicion_of_void()

    def suspicion_of_void(self):
        print("Lira becomes suspicious of The Void's involvement.")
        self.transition_to_chapter_2()

    def transition_to_chapter_2(self):
        print("Transitioning to Chapter 2: Lira investigates The Void.")


class Chapter2:
    def begin_chapter_2(self):
        print("Start of Chapter 2")
        self.discover_void_proof()

    def discover_void_proof(self):
        print("Lira finds proof of The Void's movements.")
        self.solve_riddle()

    def solve_riddle(self):
        print("Lira answers a riddle to access a secure terminal.")
        self.access_terminal()

    def access_terminal(self):
        print("Lira accesses the terminal to learn about The Void’s goals.")
        self.sneak_through_base()

    def sneak_through_base(self):
        print("Lira carefully moves through the base to avoid detection.")
        self.save_ally()

    def save_ally(self):
        print("Lira saves a captured ally.")
        self.learn_void_plan()

    def learn_void_plan(self):
        print("Lira learns about The Void’s plans to take over Astra Nova.")
        self.end_chapter_2()

    def end_chapter_2(self):
        print("End of Chapter 2")
        self.unite_factions()

    def unite_factions(self):
        print("Lira decides to unite factions against The Void.")
        self.transition_to_chapter_3()

    def transition_to_chapter_3(self):
        print("Transitioning to Chapter 3: Lira rallies factions against The Void.")


class Chapter3:
    def start_chapter_3(self):
        print("Start of Chapter 3")
        self.meet_factions()

    def meet_factions(self):
        print("Lira meets with factions in a neutral zone.")
        self.make_dialogue_choices()

    def make_dialogue_choices(self):
        print("Lira makes dialogue choices to convince factions to join the cause.")
        self.fulfill_side_quests()

    def fulfill_side_quests(self):
        print("Lira fulfills side quests to earn support and resources.")
        self.prepare_for_clash()

    def prepare_for_clash(self):
        print("Lira prepares for a clash against The Void.")
        self.end_chapter_3()

    def end_chapter_3(self):
        print("End of Chapter 3")
        self.allies_ready()

    def allies_ready(self):
        print("Lira’s allies are ready to take on The Void.")
        self.transition_to_chapter_4()

    def transition_to_chapter_4(self):
        print("Transitioning to Chapter 4: Lira and allies attack The Void.")


class Chapter4:
    def start_chapter_4(self):
        print("Start of Chapter 4")
        self.stage_attack()

    def stage_attack(self):
        print("Lira and allies stage an attack on The Void's base.")
        self.navigate_security()

    def navigate_security(self):
        print("Lira navigates through security systems using technical skills.")
        self.engage_in_combat()

    def engage_in_combat(self):
        print("Lira engages in combat with The Void's elite guards.")
        self.solve_puzzles()

    def solve_puzzles(self):
        print("Lira solves environmental puzzles to deactivate defense systems.")
        self.reach_core()

    def reach_core(self):
        print("Lira reaches the core of The Void's base, where the leader awaits.")
        self.end_chapter_4()

    def end_chapter_4(self):
        print("End of Chapter 4")
        self.face_void_leader()

    def face_void_leader(self):
        print("Lira faces off against The Void's leader.")
        self.transition_to_chapter_5()

    def transition_to_chapter_5(self):
        print("Transitioning to Chapter 5: Final Confrontation.")


class Chapter5:
    def start_chapter_5(self):
        print("Start of Chapter 5")
        self.assemble_allies()

    def assemble_allies(self):
        print("Lira assembles all gathered allies for the final clash against The Void's leader.")
        self.make_vital_decisions()

    def make_vital_decisions(self):
        print("Lira makes vital decisions that impact the outcome of the war and the future of Astra Nova.")
        self.confront_void_leader()

    def confront_void_leader(self):
        print("Lira confronts The Void's leader in a final boss battle.")
        self.determine_fate()

    def determine_fate(self):
        print("Lira determines the fate of Astra Nova and its inhabitants.")
        self.end_game()

    def end_game(self):
        print("End of Chapter 5")
        print("Game Ending")


class Game:
    def __init__(self):
        self.chapter_1 = Chapter1()
        self.chapter_2 = Chapter2()
        self.chapter_3 = Chapter3()
        self.chapter_4 = Chapter4()
        self.chapter_5 = Chapter5()

    def start_game(self):
        self.chapter_1.start_chapter_1()
        self.chapter_2.begin_chapter_2()
        self.chapter_3.start_chapter_3()
        self.chapter_4.start_chapter_4()
        self.chapter_5.start_chapter_5()


# Create a game object and start the game
game = Game()
game.start_game()
