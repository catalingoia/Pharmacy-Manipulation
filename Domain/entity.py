class Entity:

    def __init__(self, id_entity):
        self.__id_entity = id_entity

    @property
    def id_entity(self):
        return self.__id_entity

    @id_entity.setter
    def id_entity(self, id_ent):
        self.__id_entity = id_ent
