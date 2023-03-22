from timer import Timer


class TimerGroup:
    def __init__(self, *args):
        self.timers = {}
        self.init_timers(args)

    def init_timers(self, args):
        """Create timers with keys given by args."""
        for timer_name in args:
            self.add_timer(timer_name)

    def add_timer(self, timer_name):
        """Adds a timer to the TimerGroup with the name as key."""
        self.timers[timer_name] = Timer()

    def total_elapsed_time(self):
        """Prints the sum of all timers elapsed_time in group."""
        total = 0
        for timer in self.timers.values():
            total += timer.elapsed_time
        print(f"Total Elapsed Time: {total}")

    def get_all_timers_elapsed_time(self):
        """Prints all the timers elapsed times in the group."""
        for key, timer in self.timers.items():
            print(f"{key}: {timer.elapsed_time}")

    def get_timer_elapsed_time(self, timer_name):
        """Given a timers name, print the elapsed time for that timer."""
        timer = self.timers.get(timer_name, None)
        if timer is None:
            print(f"No timer found for {timer_name}")
        else:
            print(f"{timer_name}: {timer.elapsed_time}")

    def start_timer(self, timer_name):
        """Given a timers name, start that timer in the group."""
        timer = self.timers.get(timer_name, None)
        if timer is None:
            print(f"No time found for {timer_name}")
        else:
            timer.start()

    def end_timer(self, timer_name):
        """Given a timers name, end that timer in the group"""
        timer = self.timers.get(timer_name, None)
        if timer is None:
            print(f"No time found for {timer_name}")
        else:
            timer.end()

    def end_all(self):
        """End all timers in the group."""
        for timer in self.timers.values():
            timer.end()

    def display_full(self):
        """Prints all load times for each timer and total load times in the group."""
        self.get_all_timers_elapsed_time()
        self.total_elapsed_time()
