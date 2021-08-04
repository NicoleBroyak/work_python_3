packages_sent = 0
kg_sent = 0
unused_kg = 0
item_weight = 1
count = 0
current_package_weight = 0
package_number = 1
min_item_weight = int(input("Type minimal weight of item: "))
max_item_weight = int(input("Type maximum weight of item: "))
package_weight_limit = int(input("Type maximum weight of package: "))
lightest_package = package_weight_limit
lightest_package_number = 1
heaviest_package = 0
heaviest_package_number = 1
while item_weight:
    item_weight = int(input("Please type weight of item to add to package"
                            " number {}:".format(package_number)))

    if ((item_weight > max_item_weight) and (item_weight != 0) or
       (item_weight < min_item_weight) and (item_weight != 0)):
        print("Please type correct weight of item")
        continue

    kg_sent += item_weight
    if item_weight == 0 and current_package_weight != 0 and count > 0:
        packages_sent += 1
        unused_kg += (package_weight_limit - current_package_weight)
        break

    if (current_package_weight + item_weight) > package_weight_limit:
        if lightest_package > current_package_weight:
            lightest_package = current_package_weight
            lightest_package_number = package_number
        if heaviest_package < current_package_weight:
            heaviest_package = current_package_weight
            heaviest_package_number = package_number
        package_number += 1
        packages_sent += 1
        unused_kg += package_weight_limit - current_package_weight
        current_package_weight = item_weight
        count += 1
        print("item too heavy for current package, switching to next package, "
              "current package weight is {}".format(current_package_weight))
        continue
    else:
        current_package_weight = current_package_weight + item_weight
        if item_weight != 0:
            count += 1
        print("Item added to package successfully, current package weight is "   
              " {} kg".format(current_package_weight))

if item_weight == 0 and count == 0:
    print("Packages sent: 0; kilograms sent: 0; unused kg in packages sent: 0; "
          "the lightest package sent: 0 kg")

if count != 0:
    print("Process finished, sending packages and calculating results")
    if lightest_package > current_package_weight:
        lightest_package = current_package_weight
        lightest_package_number = package_number
    if heaviest_package < current_package_weight:
        heaviest_package = current_package_weight
        heaviest_package_number = package_number
    print("Packages sent: {}; kilograms sent: {};"
          " unused kg in packages sent: {}; the lightest package sent:"
          "number {} ({}kg); the heaviest package sent: number {} ({}kg)"
          .format(packages_sent, kg_sent, unused_kg,
                  lightest_package_number, lightest_package,
                  heaviest_package_number, heaviest_package))
'''
Made
by 
Nicole 
Broyak 
<3
'''
