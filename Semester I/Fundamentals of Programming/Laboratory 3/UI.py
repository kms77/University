def command_menu():
    '''
    #function that starts the program
    #input:-
    #output:message about the input/ nothing-for a correct command
    '''
    category=["housekeeping","food","transport","clothing","internet","others"]
    from Service import add_expense
    from Service import insert_expense
    from Service import remove_expense
    from Service import display_list
    commands={"add":add_expense,"insert":insert_expense,"remove":remove_expense,"list":display_list}
    List=[]
    history=[]
    from Domain import create_list
    create_list(List)
    from Domain import ten_items_startup
    ten_items_startup(List)
    from Domain import add_to_history
    add_to_history(List,history)
    from Tests import all_tests
    all_tests()
    while True:
        from Domain import get_cmd
        cmd=get_cmd()
        if cmd[0] in commands:
            if cmd[0]=='add':
                add_expense(List,category,cmd,history)
            elif cmd[0]=='insert':
                insert_expense(List,category,cmd,history)
            elif cmd[0]=='remove':
                remove_expense(List,category,cmd,history)
            elif cmd[0]=='list':
                display_list(List,category,cmd)
        elif cmd[0]=='exit':
            print("Command-menu was closed!")
            return 
        else:
            print("Invalid command!")