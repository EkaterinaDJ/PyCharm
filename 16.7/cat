class Cat:
    def __init__(self, name='', gender='', age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")

cats = [
    {
    'name': 'Сэм',
    'gender': 'мальчик',
    'age': 2
    },
    {'name': 'Барон',
    'gender': 'мальчик',
    'age': 2
    },
]

for cat in cats:
    cat_obj = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))

    print(cat_obj.name, cat_obj.gender, cat_obj.age)
