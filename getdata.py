from KEEpydb import KEEpydb
def get(value):
    row=120
    column='a'
    i=1
    query=KEEpydb.query('database','NitinKumar','12345678')
    for i in range(1,row+1):
        if query.get_cell(f'{column+str(i)}')==value:
            return {
                str(query.get_cell('A1')):str(query.get_cell('A'+str(i))),
                str(query.get_cell('B1')):str(query.get_cell('B'+str(i))),
                str(query.get_cell('C1')):str(query.get_cell('C'+str(i))),
                str(query.get_cell('D1')):str(query.get_cell('D'+str(i))),
                str(query.get_cell('E1')):str(query.get_cell('E'+str(i))),
                str(query.get_cell('F1')):str(query.get_cell('F'+str(i)))    
            }

if __name__=='__main__':
    while True:
        print(get(input('enter choice : ')))