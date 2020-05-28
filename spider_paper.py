class Paper:
    def __init__(self, title='', url='', date = '', resourcetype='', author='', source='', time='', summary=''):
        self.title = title
        self.url = url 
        self.author = author
        self.source = source
        self.summary = summary
        self.date = date

    def printf(self):
        print(self.title)
        print(self.url)
        print(self.author)
        print(self.date)
        print(self.source)
        print(self.summary)
        print('\n')

    def printFile(self, keyword):
        file1 = open(keyword+'_data.txt', 'a+')
        file1.write(self.title + '\n')
        file1.write(self.url + '\n')
        file1.write(self.author + '\n')
        file1.write(self.date + '\n')
        file1.write(self.source + '\n')
        file1.write(self.summary + '\n')
        file1.write('\n\n')
        print('write success!')
        file1.close()


        






