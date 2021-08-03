packages_sent = 0
kg_sent = 0
unused_kg = 0
item_weight = 1
count = 0
current_package_weight = 0
package_number = 1
lightest_package = 20
lightest_package_number = 1
# ^addition of initial variables
while item_weight:
    item_weight = int(input("Please type weight of item to add to package"
                            " number {}:".format(package_number)))

    if item_weight > 10 or item_weight < 0:          # Protection in case of
        print("Please type correct weight of item")  # typing wrong weight
        continue                                     #

    kg_sent += item_weight

    if item_weight == 0 and current_package_weight != 0 and count > 0:  # this
        packages_sent += 1                        # block ensures that partially
        unused_kg += 20 - current_package_weight  # filled package is included
        break                                     # in final calculation

    if (current_package_weight + item_weight) > 20:    # This block ensures
        package_number += 1                            # that the package weight
        packages_sent += 1                             # won't exceed 20 kg
        unused_kg += 20 - current_package_weight       # and switches to next
        if lightest_package > current_package_weight:  # package while exceeded
            lightest_package = current_package_weight  # and notes whether the
            lightest_package_number = package_number   # package is the lightest
        current_package_weight = item_weight           # and adds too heavy item
        count += 1                                     # to next package
        print("item too heavy for current package, switching to next package, "
              "current package weight is {}".format(current_package_weight))
        continue                                       #
    else:                                              #
        current_package_weight = current_package_weight + item_weight
        if item_weight != 0:                           #
            count += 1                                 #
        print("Item added to package successfully, current package weight is "   
              " {} kg".format(current_package_weight))  # end of block

if item_weight == 0 and count == 0:
    print("Packages sent: 0; kilograms sent: 0; unused kg in packages sent: 0; "
          "the lightest package sent: 0 kg")

if count != 0:
    print("Process finished, sending packages and calculating results")
    if lightest_package > current_package_weight:
        lightest_package = current_package_weight
        lightest_package_number = package_number
    print("Packages sent: {}; kilograms sent: {};"
          " unused kg in packages sent: {}; the lightest package sent:"
          "number {} ({}kg))"
          .format(packages_sent, kg_sent, unused_kg,
                  lightest_package_number, lightest_package))
'''
Made
by 
Nicole 
Broyak 
<3
'''