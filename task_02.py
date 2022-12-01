#### TASK 02 ####
# Создайте приложение для приготовления пасты.
# Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие методы:
# - Тип пасты;
# - Соус;
# - Начинка;
# - Добавки.
# Для реализации используйте порождающие паттерны.
import copy


class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        print(f"Pasta: {obj.name}\nType: {obj.type}\nSauce: {obj.sauce}\nStaffing: {obj.staffing}"
              f"\nAdditive: {obj.additive}")
        return obj


class Pasta(object):
    """Pasta"""


prototype = Prototype()
prototype.register("Pasta", Pasta())
capellini = prototype.clone("Pasta", {"name": "Capellini", "type": "long", "sauce": "tomate", "staffing": None,
                                      "additive": "cheese"})
print("-" * 100)
girandolles = prototype.clone("Pasta", {"name": "Girandolles", "type": "short", "sauce": None, "staffing": None,
                                        "additive": "cheese"})
print("-" * 100)
Conquillier = prototype.clone("Pasta", {"name": "Conquillier", "type": "short", "sauce": "tomate", "staffing": "meat",
                                        "additive": "cheese"})
