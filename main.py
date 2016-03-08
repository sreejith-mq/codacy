# codacy


class MainOne(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "MainOne - {}".format(self.name)

    def __unicode__(self):
        return unicode(self.__str__())
    
if __name__=='__main__':
    main = MainOne('sreejith')
    print str(main)
