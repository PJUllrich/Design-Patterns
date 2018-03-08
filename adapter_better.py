class Elf:
    def nall_nin(self):
        print('Elf says: Calling the Overlord ...')


class Dwarf:
    def estver_narho(self):
        print('Dwarf says: Calling the Overlord ...')


class Human:
    def ring_mig(self):
        print('Human says: Calling the Overlord ...')


class ElfAdapter:
    def __init__(self, elf):
        self.elf = elf

    def call_me(self):
        self.elf.nall_nin()


class DwarfAdapter:
    def __init__(self, dwarf):
        self.dwarf = dwarf

    def call_me(self):
        self.dwarf.estver_narho()


class HumanAdapter:
    def __init__(self, human):
        self.human = human

    def call_me(self):
        self.human.ring_mig()


if __name__ == '__main__':
    minions = [ElfAdapter(Elf()),
               DwarfAdapter(Dwarf()),
               HumanAdapter(Human())]

    for minion in minions:
        minion.call_me()
