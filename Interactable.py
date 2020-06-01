from Eums import Interactions


class Interactable:
    # TODO: determine if id should be kept in class or kept as a key for
    #       the global dictionary of item
    def __init__(self, name, desc, responses, interactions, hidden=False):
        # self.iid = iid
        self.name = name
        self.description = desc
        self.responses = responses
        self.interactions = interactions
        self.hidden = hidden


class InteractablesBuilder:

    def build_interactables(self):
        #retrieve intera. list from file
        #loop through file list and instantiate each intera.

    @staticmethod
    def create_presets():
        with open('interactables.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')
            line_count = 0
            interactables = {}
            for row in csv_reader:
                if line_count == 0:
                    continue
                # instantiate
                ine_count += 1

            print(f'Processed {line_count} lines.')
