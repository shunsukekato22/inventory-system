inventory = {}

while True:
    print('1.商品登録')
    print('2.入庫')
    print('3.出庫')
    print('4.一覧表示')
    print('5.終了')

    choice = input('番号を選んでください:')

#商品登録
    if choice == '1':
        item_name = input('商品名を入力してください:').strip()

        if item_name == '' :
            print('商品名を入力してください')
        
        elif item_name in inventory:
            print('その商品は既に登録されています')

        else:
            inventory[item_name] = {'stock' : 0}
            print(f'{item_name}を登録しました')

#入庫
    elif choice == '2':
        print('現在の在庫')
        for item in inventory:
            print(f'{item}:{inventory[item]["stock"]}')
            
        item = input('入庫する商品を入力してください:')

        if item in inventory:
            num_input = input('入庫数を入力してください:')

            if num_input == '':
                print('入庫数を入力してください')
            else:
                num = int(num_input)
                inventory[item]['stock'] += num
                print(f'現在の在庫は {inventory[item]["stock"]} 個')
       
        else:
            print('商品が登録されていません')

#出庫
    elif choice == '3':
        print('現在の在庫')
        for item in inventory:
            print(f'{item}:{inventory[item]["stock"]}')
            
        item = input('出庫する商品を入力してください:')

        if item in inventory:
            num_input = input('出庫数を入力してください:')

            if num_input == '':
                print('出庫数を入力してください:')
            else:
                num = int(num_input)
                if inventory[item]['stock'] >= num:
                    inventory[item]['stock'] -= num
                    print(f'現在の{item} の在庫は {inventory[item]["stock"]} 個')
                
                    if inventory[item]['stock'] == 0:
                        print('在庫がゼロになりました!')

                else:
                    print('在庫が足りません')
        
        else:
            print('商品が登録されていません')

#一覧表示
    elif choice == '4':
        print('===在庫一覧===')

        if not inventory:
            print('在庫が登録されていません')
        
        else:
            for item in inventory:
                print(f'{item} : {inventory[item]["stock"]}')





        
        