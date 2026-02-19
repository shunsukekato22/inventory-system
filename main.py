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
    if choice == '2':
        stock = input('入庫数を入力してください').strip()

        if stock == '':
            print