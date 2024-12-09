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

# Running Chapter 1
chapter_1 = Chapter1()
chapter_1.start_chapter_1()