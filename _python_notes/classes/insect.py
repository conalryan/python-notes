#!/usr/bin/env python

from  animal import Animal


class Insect(Animal):
    """
        An animal with 2 sets of wings and 3 pairs of legs
    """
    # Constructor aka initializer
    def __init__(self, species, name, sound, can_fly=True):
        # Call base class constructor
        super().__init__(species, name, sound)
        # Add new attributes specific to Insect
        self._can_fly = can_fly

    # Getter property
    @property
    def can_fly(self):
        return self._can_fly


if __name__ == '__main__':
    mon = Insect('monarch butterfly', 'Mary', None) # Defaults to can_fly=True
    scar = Insect('scarab beetle', 'Rupert', 'Bzzz', False)

    for insect in mon, scar:
        flying_status = 'can' if insect.can_fly else "can't"
        print("Hi! I am {} the {} and I {} fly!".format(  # make_sound inherited from Animal
                insect.name, insect.species, flying_status
            ),
        )
        insect.make_sound() # <6>
        print()
