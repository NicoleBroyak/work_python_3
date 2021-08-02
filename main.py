packages_sent = 0
kg_sent = 0
unused_kg = 0
item_weight = 1
count = 0
current_package_weight = 0
package_number = 1
the_lightest_package = 20
the_lightest_package_number = 0
# ^addition of initial variables
while item_weight and count > -1:
    print("Please type weight of item to add to package number {}"
          .format(package_number))
    item_weight = int(input())
    if item_weight > 10 or item_weight < 0:
        print("Please type correct weight of item")
        continue
    elif item_weight == 0:
        if count == 0:
            count = -1
        break
    count = count + 1
    if (current_package_weight + item_weight) > 20:
        package_number += 1
        packages_sent += 1
        unused_kg += 20 - current_package_weight
        kg_sent += item_weight
        if the_lightest_package > current_package_weight:
            the_lightest_package = current_package_weight
            the_lightest_package_number = package_number
        current_package_weight = item_weight
        print("item too heavy for current package, switching to next package, "
              "current package weight is {}".format(current_package_weight))
        continue
    else:
        current_package_weight = current_package_weight + item_weight
        kg_sent += item_weight
        print("Item added to package successfully, "
              "current package weight is {} kg".format(current_package_weight))
if count == -1:
    print("Packages sent: 0; kilograms sent: 0; unused kg in packages sent: 0; "
          "the lightest package sent: 0 kg")
if count != -1:
    packages_sent += 1
    print ("Process finished, sending packages and calculating results")
    unused_kg += 20 - current_package_weight
    kg_sent += item_weight
    if the_lightest_package > current_package_weight:
        the_lightest_package = current_package_weight
        the_lightest_package_number = package_number
    print("Packages sent: {}; kilograms sent: {};"
          " unused kg in packages sent: {}; the lightest package sent:"
          "number {} ({}kg))"
          .format(packages_sent, kg_sent, unused_kg,
                  the_lightest_package_number, the_lightest_package))
# Made by Nicole Broyak <3
