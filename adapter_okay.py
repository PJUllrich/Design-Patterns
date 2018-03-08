class Elf:
    def nall_nin(self):
        print('Elf says: Calling the Overlord ...')


class Dwarf:
    def estver_narho(self):
        print('Dwarf says: Calling the Overlord ...')

class Human:
    def ring_mig(self):
        print('Human says: Calling the Overlord ...')


if __name__ == '__main__':
    minions = [Elf(), Dwarf(), Human()]

    for minion in minions:
        if isinstance(minion, Elf):
            minion.nall_nin()
        elif isinstance(minion, Dwarf):
            minion.estver_narho()
        else:
            minion.ring_mig()
