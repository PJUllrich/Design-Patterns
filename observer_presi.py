from observer.observer_pattern import Observable, Observer


class Elf:
    name = 'Galadriel'

    def nall_nin(self):
        print('Elf says: Calling the Overlord ...')


class Dwarf:
    def estver_narho(self):
        print('Dwarf says: Calling the Overlord ...')


class Human:
    def ring_mig(self):
        print('Human says: Calling the Overlord ...')


class MinionAdapter(Observable):
    _initialised = False

    def __init__(self, minion, **adapted_methods):
        super().__init__()

        self.minion = minion

        for key, value in adapted_methods.items():
            func = getattr(self.minion, value)
            self.__setattr__(key, func)

        self._initialised = True

    def __getattr__(self, attr):
        return getattr(self.minion, attr)

    def __setattr__(self, key, value):
        if not self._initialised:
            super().__setattr__(key, value)
        else:
            setattr(self.minion, key, value)
            self.notify_observer(key=key, value=value)


class MinionFacade:
    minion_adapters = None

    @classmethod
    def create_minions(cls):
        print('Creating minions ...')
        cls.minion_adapters = [
            MinionAdapter(Elf(), call_me='nall_nin'),
            MinionAdapter(Dwarf(), call_me='estver_narho'),
            MinionAdapter(Human(), call_me='ring_mig')
        ]

    @classmethod
    def summon_minions(cls):
        print('Summoning minions ...')
        for adapter in cls.minion_adapters:
            adapter.call_me()

    @classmethod
    def monitor_elves(cls, observer):
        cls.minion_adapters[0].add_observer(observer)
        print('Added an observer to the Elves!')

    @classmethod
    def change_elves_name(cls, new_name):
        print('Changing the Elves name ...')
        cls.minion_adapters[0].name = new_name
        print('Elves name changed!')


class EvilOverlord(Observer):
    def update(self, obj, *args, **kwargs):
        print('The Evil Overlord received a message!')
        print(f'Object: {obj}, Args: {args}, Kwargs: {kwargs}')


if __name__ == '__main__':
    overlord = EvilOverlord()

    MinionFacade.create_minions()
    MinionFacade.monitor_elves(overlord)
    MinionFacade.change_elves_name('Elrond')
