from itertools import groupby
from operator import itemgetter

class Node(object):
    def __init__(self, data=None, next_node=None):
        self._data = int(data)
        self._next_node = next_node

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next_node

    def set_next(self, new_next):
        self._next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._end = head

    def append(self, data):
        print("APPENDING")
        new_node = Node(data)
        new_node.set_next(None)
        if self._head != None:
            print("APPEND: {}".format(self._head.get_data()))
            self._head = new_node
        else:
            self._end = new_node

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self._head)
        self._head = new_node

    def size(self):
        current = self._head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self._head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self._head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def sum_matched(self):
        current = self._head
        sum = 0
        print("SUM: {}".format(sum))
        while current:
            print(dir(current))
            if current.get_next() == None:
                if current.get_data() == self._head.get_data():
                    sum += current.get_data()
            if current.get_data() == current.get_next().get_data():
                print("Current matches next data {}".format(current.get_data()))
                sum += current.get_data()
            current = current.get_next()

        return sum



def main():

    #data = list('649713959682898259577777982349515784822684939966191359164369933435366431847754488661965363557985166219358714739318371382388296151195361571216131925158492441461844687324923315381358331571577613789649166486152237945917987977793891739865149734755993241361886336926538482271124755359572791451335842534893192693558659991171983849285489139421425933638614884415896938914992732492192458636484523228244532331587584779552788544667253577324649915274115924611758345676183443982992733966373498385685965768929241477983727921279826727976872556315428434799161759734932659829934562339385328119656823483954856427365892627728163524721467938449943358192632262354854593635831559352247443975945144163183563723562891357859367964126289445982135523535923113589316417623483631637569291941782992213889513714525342468563349385271884221685549996534333765731243895662624829924982971685443825366827923589435254514211489649482374876434549682785459698885521673258939413255158196525696236457911447599947449665542554251486847388823576937167237476556782133227279324526834946534444718161524129285919477959937684728882592779941734186144138883994322742484853925383518651687147246943421311287324867663698432546619583638976637733345251834869985746385371617743498627111441933546356934671639545342515392536574744795732243617113574641284231928489312683617154536648219244996491745718658151648246791826466973654765284263928884137863647623237345882469142933142637583644258427416972595241737254449718531724176538648369253796688931245191382956961544775856872281317743828552629843551844927913147518377362266554334386721313244223233396453291224932499277961525785755863852487141946626663835195286762947172384186667439516367219391823774338692151926472717373235612911848773387771244144969149482477519437822863422662157461968444281972353149695515494992537927492111388193837553844671719291482442337761321272333982924289323437277224565149928416255435841327756139118119744528993269157174414264387573331116323982614862952264597611885999285995516357519648695594299657387614793341626318866519144574571816535351149394735916975448425618171572917195165594323552199346814729617189679698944337146')
    data = list('1122')

    day1data = LinkedList()


    for d in data:
        day1data.append(d)

    print(day1data.sum_matched())

if __name__ == '__main__':
    main()