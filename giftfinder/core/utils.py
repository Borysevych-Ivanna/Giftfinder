# core/utils.py

GIFTS = [
    # ===== ЖІНКА / ДІВЧИНА =====
    {
        "name": "Подарунковий набір NIVEA",
        "image_url": "https://chistoshop.net/content/images/19/513x536l50nn0/podarunkovyi-nabir-nivea-men-active-sensitive-16693714786067.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year", "any"],
    },
    {
        "name": "Парфуми Armani Si (mini)",
        "image_url": "https://images.prom.ua/2758699775_w640_h640_2758699775.jpg",
        "recipients": ["woman", "girl"],
        "age_groups": ["adult"],
        "occasions": ["birthday", "anniversary"],
    },
    {
        "name": "Смарт-годинник Xiaomi Redmi Watch",
        "image_url": "https://assol.in.ua/image/cache/catalog/assol/86443/smart-godinnik-xiaomi-redmi-watch-5-active-midnight-black-bhr8784gl-4-445x445.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year", "any"],
    },
    {
        "name": "Ароматична свічка Vanilla Dream",
        "image_url": "https://content1.rozetka.com.ua/goods/images/base_action/406720413.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult", "senior"],
        "occasions": ["new_year", "any"],
    },
    {
        "name": "Плед-фліс для дому",
        "image_url": "https://cdn.27.ua/sc--media--prod/default/b4/f3/96/b4f39686-2c4f-4001-80f4-4c3798edbf19.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["adult", "senior"],
        "occasions": ["new_year", "any"],
    },
    {
        "name": "Набір чаю Basilur у коробці",
        "image_url": "https://basilur.com.ua/image/cache/catalog/basilur/giftbox-oriental-1-500x500.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["adult", "senior"],
        "occasions": ["new_year", "any"],
    },
    {
        "name": "Щоденник з мотиваційними фразами",
        "image_url": "https://dumka.top/image/cache/catalog/1OSV/100%D1%80/417-270x270.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Сертифікат на манікюр",
        "image_url": "https://img.freepik.com/free-psd/nail-salon-voucher-template-design_23-2151919345.jpg?semt=ais_incoming&w=740&q=80",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "anniversary"],
    },
    {
        "name": "Срібний браслет з підвіскою",
        "image_url": "https://zasluha.com/image/cache/catalog/import_products/190/1ee6728b-45a6-4e46-b00e-86e71dcc0a7e-1000x1000.jpg",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "anniversary", "any"],
    },
    {
        "name": "Косметичка для подорожей",
        "image_url": "https://images.prom.ua/4177386953_w1280_h640_4177386953.jpg",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["any"],
    },
    # додаткові логічні для дівчини
    {
        "name": "Набір для догляду за волоссям",
        "image_url": "https://ua.loccitane.com/cdn/shop/files/TR_26.png?v=1748256909",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Домашня піжама з принтом",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyQAsG_uUxVTnZljtuJb845J6TAjrjzkUSaA&s",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["new_year", "any"],
    },
    {
        "name": "Сумка-шоппер на кожен день",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpdI9dIp06OumZYVfK1dCaiYeyEnpCqE1vqQ&s",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["any"],
    },
    {
        "name": "Подарунковий бокс з косметикою",
        "image_url": "https://buket-market.kiev.ua/content/images/25/536x513l50nn0/podarunkovyi-nabir-boks-dlia-zhinky-z-kosmetykoiu-rituals-aiurveda-i-tsukerkamy-1403-11350763996900.png",
        "recipients": ["woman", "girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year"],
    },

    # ===== ЧОЛОВІК / ХЛОПЕЦЬ =====
    {
        "name": "Навушники JBL Tune 510BT",
        "image_url": "https://i.moyo.ua/img/products/5154/81_1500.jpg",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year", "any"],
    },
    {
        "name": "Powerbank Xiaomi 20000mAh",
        "image_url": "https://cactus.net.ua/image/cache/catalog/product/Power%20bank/1006413/glavnayacherniy20000-700x700.png",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Шкіряний гаманець",
        "image_url": "https://images.prom.ua/6699948163_w1280_h640_6699948163.jpg",
        "recipients": ["man", "boy"],
        "age_groups": ["adult"],
        "occasions": ["birthday", "anniversary", "wedding", "any"],
    },
    {
        "name": "Парфуми Dior Sauvage (mini)",
        "image_url": "https://u.makeup.com.ua/h/hj/hjbe0qysd8qo.jpg",
        "recipients": ["man", "boy"],
        "age_groups": ["adult"],
        "occasions": ["birthday", "anniversary"],
    },
    {
        "name": "Смарт-браслет для спорту",
        "image_url": "https://png.pngtree.com/png-vector/20240601/ourmid/pngtree-vector-smart-bracelet-displaying-the-counting-step-png-image_12588438.png",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year", "any"],
    },
    {
        "name": "Термокружка для кави",
        "image_url": "https://png.pngtree.com/png-clipart/20200225/original/pngtree-white-thermos-mug-mockup-realistic-style-png-image_5258725.jpg",
        "recipients": ["man", "boy"],
        "age_groups": ["adult", "senior"],
        "occasions": ["new_year", "any"],
    },
    {
        "name": "Футболка з улюбленим принтом",
        "image_url": "https://images.prom.ua/5842207044_w1280_h640_5842207044.jpg",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Настільна гра для компанії",
        "image_url": "https://geekach.com.ua/content/uploads/images/component%281%29.png",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year", "any"],
    },
    # додаткові логічні для хлопця/чувака
    {
        "name": "Бездротова мишка для компʼютера",
        "image_url": "https://content2.rozetka.com.ua/goods/images/big/320913461.png",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Ігрова гарнітура з мікрофоном",
        "image_url": "https://havit.com.ua/files/products/221ff0f1-5c3d-11ee-836f-78e7d1920006.330x470.png",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "new_year"],
    },
    {
        "name": "Набір для догляду за бородою",
        "image_url": "https://media.prostor.ua/catalog/product/2/1/212706.png?width=370&height=370",
        "recipients": ["man", "boy"],
        "age_groups": ["adult"],
        "occasions": ["birthday", "anniversary", "any"],
    },
    {
        "name": "Міський рюкзак",
        "image_url": "https://cdn.27.ua/sc--media--prod/default/b6/34/d5/b634d51a-72b4-4973-b56e-2543113baac4.jpeg",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Кружка з крутими написами",
        "image_url": "https://printuy.com/image/cache/catalog/products/8-85-137-199-front-250x250.png",
        "recipients": ["man", "boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["any"],
    },

    # ===== РОМАНТИЧНЕ (дівчина / хлопець) =====
    {
        "name": "Букет квітів у коробці",
        "image_url": "https://www.annetflowers.com.ua/image/cache/catalog/tsvetyi-v-korobke-yaroslava-800x800.png",
        "recipients": ["girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "anniversary", "any"],
    },
    {
        "name": "Фотокнига зі спільними фото",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOkNvs29C-fnP2P6SBYElPmSORdEDZ35pi3g&s",
        "recipients": ["girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "any"],
    },
    {
        "name": "Сертифікат на спільну фотосесію",
        "image_url": "https://insider-media.net/storage/28132/conversions/1-big.webp",
        "recipients": ["girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "birthday"],
    },
    {
    "name": "Світлова картина з вашим фото",
    "image_url": "https://images.prom.ua/6713797517_w1280_h640_6713797517.jpg",
    "recipients": ["girl"],
    "age_groups": ["teen", "adult"],
    "occasions": ["anniversary", "birthday", "any"],
    },

    {
        "name": "Гірлянда з прищіпками для фото",
        "image_url": "https://images.prom.ua/5257468179_w1280_h640_5257468179.jpg",
        "recipients": ["girl"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "new_year", "any"],
    },

    {
        "name": "Парні браслети для закоханих",
        "image_url": "https://images.prom.ua/6713797517_w1280_h640_6713797517.jpg",
        "recipients": ["boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "any"],
    },
    {
        "name": "Сертифікат на картинг",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvibNtF7Kg0wYMhIq0pqU-Y20UpYCQcHQ_7WMNUCwlmVw7RGqA_n_uR2XtEQRRAFSf7Pw&usqp=CAU",
        "recipients": ["boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["birthday", "any"],
    },
    {
        "name": "Настільна гра для двох",
        "image_url": "https://cdn.27.ua/sc--media--prod/default/9d/64/b7/9d64b756-a99f-4681-a7eb-98854da0b71a.png",
        "recipients": ["boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "any"],
    },
    {
        "name": "Футболка з вашим спільним фото",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC3WsxP-My2YjT4b5DfovQY24qJz3uRdagAw&s",
        "recipients": ["boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "birthday"],
    },
    {
        "name": "Квитки в кіно на двох",
        "image_url": "https://st2.depositphotos.com/1734074/6963/v/450/depositphotos_69632097-stock-illustration-two-vintage-cinema-tickets-vector.jpg",
        "recipients": ["boy"],
        "age_groups": ["teen", "adult"],
        "occasions": ["anniversary", "any"],
    },

    # ===== УНІВЕРСАЛЬНІ =====
    {
        "name": "Подарункова коробка цукерок",
        "image_url": "https://rin.com.ua/wp-content/uploads/2019/02/20171119_105447.png",
        "recipients": ["any"],
        "age_groups": ["any"],
        "occasions": ["birthday", "new_year", "any"],
    },
    {
        "name": "Подарунковий сертифікат у магазин",
        "image_url": "https://ilovemommy.com.ua/media/catalog/product/cache/1e25e445037f35a9cfcb4b9cef4d5536/1/6/1683709742_certificate-1000-plastic.png",
        "recipients": ["any"],
        "age_groups": ["teen", "adult", "senior"],
        "occasions": ["birthday", "new_year", "anniversary", "wedding", "any"],
    },
    {
        "name": "Набір кави та чаю",
        "image_url": "https://royal-life.ua/content/uploads/images/novorchn-podarunki.png",
        "recipients": ["any"],
        "age_groups": ["adult", "senior"],
        "occasions": ["new_year", "any"],
    },
    {
        "name": "Настільна лампа для робочого столу",
        "image_url": "https://images.prom.ua/6832351771_w1280_h640_6832351771.jpg",
        "recipients": ["any"],
        "age_groups": ["teen", "adult", "senior"],
        "occasions": ["any"],
    },
    {
        "name": "Настінний постер у рамці",
        "image_url": "https://cdn.27.ua/sc--media--prod/default/35/4a/e8/354ae8c8-789e-43af-a45c-9d4820ccfa8a.png",
        "recipients": ["any"],
        "age_groups": ["teen", "adult"],
        "occasions": ["any"],
    },
    {
        "name": "Світлодіодна гірлянда",
        "image_url": "https://images.prom.ua/1361167283_w640_h640_1361167283.jpg",
        "recipients": ["any"],
        "age_groups": ["teen", "adult", "senior"],
        "occasions": ["new_year", "any"],
    },
]


def _match_recipient(gift_recipients, selected: str) -> bool:
    return "any" in gift_recipients or selected in gift_recipients


def _match_age(gift_age_groups, selected: str) -> bool:
    return "any" in gift_age_groups or selected in gift_age_groups


def _match_occasion(gift_occasions, selected: str) -> bool:
    if "any" in gift_occasions:
        return True
    if selected == "none":  # без приводу
        return True
    return selected in gift_occasions


def get_gift_suggestions(criteria):
    """
    Повертає стабільний список подарунків:
    - БЕЗ random
    - Завжди однаковий порядок для однакових параметрів
    - Спочатку жорсткі збіги, потім мʼякі
    - максимум 20
    """

    recipient_type = criteria.get("recipient_type")
    age_group = criteria.get("age_group")
    occasion = criteria.get("occasion")

    hard = []  # повністю підходять за всіма параметрами
    soft = []  # частково підходять (той самий привід + або одержувач, або вік)

    # 1) ЖОРСТКИЙ ФІЛЬТР (одержувач + вік + привід)
    for gift in GIFTS:
        if not _match_recipient(gift["recipients"], recipient_type):
            continue
        if not _match_age(gift["age_groups"], age_group):
            continue
        if not _match_occasion(gift["occasions"], occasion):
            continue
        hard.append(gift)

    # 2) МʼЯКИЙ ФІЛЬТР
    for gift in GIFTS:
        if gift in hard:
            continue
        if not _match_occasion(gift["occasions"], occasion):
            continue
        if (
            _match_recipient(gift["recipients"], recipient_type)
            or _match_age(gift["age_groups"], age_group)
        ):
            soft.append(gift)

    candidates = hard + soft

    # до 20, стабільний порядок
    return candidates[:20]
