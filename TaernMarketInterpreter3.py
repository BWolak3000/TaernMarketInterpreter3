import AnalizerForAndroid


def convert_price_to_int(price):
    try:
        price = price.split(':')
        if price[1][-1] == 'k':
            price[1] = price[1][:-1]
            return float(int(price[1]) * 1000)/float(int(price[0]))
        else:
            return float(int(price[1]))/float(int(price[0]))
    except:
        return -1


def count_entity(list):
    result = {}
    max = 0
    thing = list[0]
    for ent in list:
        if ent in result:
            result[ent] += 1
            if result[ent] > max:
                max = result[ent]
                thing = ent
        else:
            result[ent] = 1
    return result, thing


def add_to_average(av, added, count):
    av *= count
    av += added
    count += 1
    av = av / count
    return av, count


if __name__ == '__main__':
    f = open(r"C:\Users\Bartoszek\Desktop\TaernTradeHistory\procesed20.08.23.txt", "r")
    data = f.read().split('\n')
    sell_products = []
    buy_products = []
    authors = []
    average_price = 0
    count = 0
    i = 0#dla oszczedzania quary w monkeylearn
    for line in data:
        #dla oszczedzania quary w monkeylearn
        if i > 70:
            break
        elif i < 55:
            i += 1
            continue
        else:
            i = i + 1
        #koniec oszczedzania
        result = AnalizerForAndroid.analize(line)
        try:
            for extraction in result.body[1]['extractions']:
                if extraction['tag_name'] == 'SellProduct':
                    sell_products.append(extraction['parsed_value'])
                elif extraction['tag_name'] == 'BuyProduct':
                    buy_products.append(extraction['parsed_value'])
                elif extraction['tag_name'] == 'Price':
                    p = convert_price_to_int(extraction['parsed_value'])
                    if p != -1:
                        average_price, count = add_to_average(average_price, p, count)
                elif extraction['tag_name'] == 'Author':
                    authors.append(extraction['parsed_value'])
        except TypeError:
            continue
    if not sell_products:
        pass
    else:
        sell_products_map, best_sell_product = count_entity(sell_products)
        # print(sell_products)
        # print(sell_products_map)
        print('najczesciej sprzedawany: ' + best_sell_product)

    if not authors:
        pass
    else:
        authors_map, best_author = count_entity(authors)
        print('najaktywniejszy sprzedawca: ' + best_author)

    if not buy_products:
        pass
    else:
        buy_products_map, best_buy_product = count_entity(buy_products)
        print('najczesciej kupowany: ' + best_buy_product)

    print('średnia cena: ' + str(average_price))
    f.close()
