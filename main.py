import json

def load_inventory():
    try:
        with open("inventory.json", "r", encoding="utf-8") as f:
            inventory = json.load(f)
    except FileNotFoundError:
        inventory = {}



#1.商品登録
def register_item(inventory):
    
    item_name = input('商品名を入力してください:').strip()

    if item_name == '' :
        print('商品名を入力してください')
    
    elif item_name in inventory:
        print('その商品は既に登録されています')

    else:
        inventory[item_name] = {'stock' : 0}
        print(f'{item_name}を登録しました')

#2.入庫
def stock_in(inventory):
    if not inventory:
        print("商品が登録されていません")
        return

    print('現在の在庫')
    for item in inventory:
        print(f'{item}:{inventory[item]["stock"]}')
        
    item = input('入庫する商品を入力してください:')

    if item in inventory:
        num_input = input('入庫数を入力してください:')

        if num_input == '':
            print('入庫数を入力してください')
        else:
            try:
                num = int(num_input)
                inventory[item]['stock'] += num
                print(f'現在の在庫は {inventory[item]["stock"]} 個')

            except ValueError:
                print('数字を入力してください')
    else:
        print('商品が登録されていません')

#3.出庫
def stock_out(inventory):
    if not inventory:
        if not inventory:
            print("商品が登録されていません")
            return

        print('現在の在庫')
        for item in inventory:
            print(f'{item}:{inventory[item]["stock"]}')
            
        item = input('出庫する商品を入力してください:')

        if item in inventory:
            num_input = input('出庫数を入力してください:')

            if num_input == '':
                print('出庫数を入力してください:')
            else:
                try:
                    num = int(num_input)
                    if inventory[item]['stock'] >= num:
                        inventory[item]['stock'] -= num
                        print(f'現在の{item} の在庫は {inventory[item]["stock"]} 個')
                    
                        if inventory[item]['stock'] == 0:
                            print('在庫がゼロになりました!')
                except ValueError:
                    print('数字を入力してください')

                else:
                    print('在庫が足りません')
        
        else:
            print('商品が登録されていません')

#4.一覧表示
def display_inventory(inventory):
    print('===在庫一覧===')

    if not inventory:
        print('在庫が登録されていません')
    
    else:
        for item in inventory:
            print(f'{item} : {inventory[item]["stock"]}')

#5.終了
def save_and_exit(inventory):
    with open("inventory.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, ensure_ascii=False, indent=4)

print("データを保存しました。終了します。")


#メインループ
def main():
    inventory = load_inventory()

    while True:
        print('\n1.商品登録')
        print('2.入庫')
        print('3.出庫')
        print('4.一覧表示')
        print('5.終了')

        choice = input('番号を選んでください:')

        if choice == '1':
            register_item(inventory)
        elif choice == '2':
            stock_in(inventory)
        elif choice == '3':
            stock_out(inventory)
        elif choice == '4':
            display_inventory(inventory)
        elif choice == '5':
            save_and_exit(inventory)
            break
        else:
            print('無効な選択です。')