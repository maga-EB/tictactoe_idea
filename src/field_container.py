from dataclasses import dataclass

from fields import Fields


@dataclass
class FieldContainer:
    _fields: Fields

    @property
    def fields(self) -> Fields:
        return self._fields.occupied

    @property
    def occupied_fields(self) -> Fields:
        return self._fields.occupied

    @property
    def unoccupied_fields(self) -> Fields:
        return self._fields.unoccupied

    @property
    def players(self):
        return self._fields.players

    @property
    def unique_players(self):
        return self._fields.unique_players
