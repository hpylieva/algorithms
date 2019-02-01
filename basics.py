import random
import logging

logging.basicConfig(filename='log.log', level=logging.INFO)


def list_to_string(list_):
    str_list_repr = ', '.join(str(e) for e in list_)
    return '['+str_list_repr+']'


class MinInList:
    def __init__(self, _list):
        self._list = _list

    def sequential(self):
        min_ = self._list[0]
        for el in self._list:
            if el < min_:
                min_ = el
        return min_


if __name__ == '__main__':
    logging.info('Test Find min in Array')
    list_ = [random.randint(10, 100) for i in range(10)]
    logging.info(' '.join(['Input:', list_to_string(list_)]))
    min_inlist = MinInList(list_).sequential()
    logging.info(' '.join(['Output: ', str(min_inlist)]))
