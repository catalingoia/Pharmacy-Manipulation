import pickle


class GenericFileRepository:

    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()
        f_read.close()

    def __save_to_file(self):

        with open(self.__filename, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)
        f_write.close()

    def create(self, entity):
        '''
        Adds a new entity.
        :param entity: the given entity
        :return: -
        :raises: RepositoryError if the id already exists
        '''
        self.__load_from_file()
        id_entity = entity.id_entity
        if id_entity in self.__storage:
            raise ('The entity id already exists!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def read(self, id_entity=None):
        '''
        Gets a vote by id or all the votes
        :param id_entity: optional, the entity id
        :return: the list of entities or the entity with the given id
        '''
        self.__load_from_file()
        if id_entity is None:
            return self.__storage.values()

        if id_entity in self.__storage:
            return self.__storage[id_entity]
        return None

    def update(self, entity):
        '''
        Updates an entity.
        :param entity: the entity to update
        :return: -
        :raises: RepositoryError if the id does not exist
        '''
        self.__load_from_file()
        id_entity = entity.id_entity
        if id_entity not in self.__storage:
            raise ('There is no entity with that id!')
        self.__storage[id_entity] = entity
        self.__save_to_file()

    def delete(self, id_entity):
        '''
        Deletes a entity.
        :param id_entity: the entity id to delete.
        :return: -
        :raises RepositoryError: if no entity with id_entity
        '''
        self.__load_from_file()
        if id_entity not in self.__storage:
            raise ('There is no entity with that id!')
        del self.__storage[id_entity]
        self.__save_to_file()
