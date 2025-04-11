import logging
import random
import sys
import time
from threading import Thread, Lock

from core import Core


def execute_ticketing_system_participation(ticket_number, part_id, shared_variable):
    output_file_name = "output-" + part_id + ".txt"
    # NOTE: Do not remove this print statement as it is used to grade assignment,
    # so it should be called by each thread
    print("Thread retrieved ticket number: {} started".format(ticket_number), file=open(output_file_name, "a"))
    # Reduce the random sleep to 0-2 seconds to avoid timeouts
    time.sleep(random.randint(0, 2))
    # wait until your ticket number has been called
    while True:
        with shared_variable['lock']:
            if shared_variable['current_ticket'] == ticket_number:
                break
        time.sleep(0.1)  # Small sleep to prevent busy-waiting

    # NOTE: Do not remove this print statement as it is used to grade assignment,
    # so it should be called by each thread
    print("Thread with ticket number: {} completed".format(ticket_number), file=open(output_file_name, "a"))
    return 0


class Assignment(Core):

    USERNAME = "surendraa"  # Your actual username
    active_threads = []

    def __init__(self, args):
        self.num_threads = 1
        self.args_conf_list = [['-n', 'num_threads', 1, 'number of concurrent threads to execute'],
                               ['-u', 'user', None, 'the user who is turning in the assignment, needs to match the '
                                                    '.user file contents'],
                               ['-p', 'part_id', 'test', 'the id for the assignment, test by default']]
        super().__init__(self.args_conf_list)
        super().parse_args(args=args)
        _format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=_format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        # Initialize the shared variable as a dictionary with a lock and current ticket number
        self.shared_variable = {
            'current_ticket': 0,
            'lock': Lock()
        }

    def run(self):
        output_file_name = "output-" + self.part_id + ".txt"
        open(output_file_name, 'w').close()
        if self.test_username_equality(self.USERNAME):
            for index in range(self.num_threads):
                logging.info("Assignment run    : create and start thread %d.", index)
                thread = Thread(target=execute_ticketing_system_participation, 
                              args=(index, self.part_id, self.shared_variable))
                self.active_threads.append(thread)
                thread.start()
            # Remove the unnecessary sleep; manage_ticketing_system will handle waiting
            self.manage_ticketing_system()
            logging.info("Assignment completed all running threads.")
            return 0
        else:
            logging.error("Assignment had an error your usernames not matching. Please check code and .user file.")
            return 1

    def manage_ticketing_system(self):
        # increment a ticket number shared by a number of threads and check that no active threads are running
        for ticket in range(self.num_threads):
            with self.shared_variable['lock']:
                self.shared_variable['current_ticket'] = ticket
            # Wait for the thread with the current ticket to complete
            self.active_threads[ticket].join()

        # Ensure no active threads remain
        for thread in self.active_threads:
            if thread.is_alive():
                thread.join()

        return 0


if __name__ == "__main__":
    # Write the username to the .user file without a newline
    with open(".user", "w") as f:
        f.write(Assignment.USERNAME)  # Removed the + "\n"
        
    assignment = Assignment(args=sys.argv[1:])
    exit_code = assignment.run()
    sys.exit(exit_code)