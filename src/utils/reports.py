import pathlib

class inwar:
    def __init__(self, report_file, clan, remaining_hours, remaining_attacks):
        self.report_file = report_file
        self.clan = clan
        self.remaining_hours = remaining_hours
        self.remaining_attacks = remaining_attacks
    
    def send(self):
        with open(self.report_file, mode = 'r') as inwar_file:
            inwar_report = inwar_file.read()
        print(inwar_report.format(clan = self.clan, remaining_hours = self.remaining_hours, remaining_attacks = self.remaining_attacks))