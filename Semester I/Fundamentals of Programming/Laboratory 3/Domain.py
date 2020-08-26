def get_cmd():
    cmd=str(input())
    cmd=cmd.rstrip()
    cmd=cmd.split()
    return cmd
def create_list(List):
    '''
    #function that create a list of dictionaries
    #input:List-the list of days and categories
    #output:the list of dictionaries with zero values
    '''
    dictionary_list={"housekeeping":0,"food":0,"transport":0,"clothing":0,"internet":0,"others":0}
    i=0
    while i<30:
        List.append(dictionary_list.copy())
        i+=1
def add_to_history(List,history):
    '''
    #function that add a list to another list
    #input:List-the list of days and categories,history-the list of the others commands
    #output:-
    '''
    l1=List.copy()
    history.append(l1)
def ten_items_startup(List):
    #10 suitable examples at program start-up
    List[0]["food"]=5
    List[4]["housekeeping"]=10
    List[4]["transport"]=3
    List[10]["others"]=11
    List[12]["others"]=11
    List[18]["internet"]=30
    List[20]["others"]=55
    List[24]["food"]=8
    List[29]["others"]=15
    List[29]["housekeeping"]=18