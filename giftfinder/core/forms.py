from django import forms


class GiftSearchForm(forms.Form):
    RECIPIENT_TYPES = [
        ("girl", "Дівчина"),
        ("boy", "Хлопець"),
    ]

    AGE_GROUPS = [
        ("teen", "Підліток"),
        ("adult", "Дорослий"),
        ("senior", "Людина поважного віку"),
    ]

    OCCASIONS = [
        ("none", "Без приводу"),
        ("birthday", "День народження"),
        ("new_year", "Новий рік / Різдво"),
        ("anniversary", "Річниця"),
        ("wedding", "Весілля"),
    ]

    recipient_type = forms.ChoiceField(
        choices=RECIPIENT_TYPES,
        label="Для кого подарунок?"
    )

    age_group = forms.ChoiceField(
        choices=AGE_GROUPS,
        label="Вікова група"
    )

    occasion = forms.ChoiceField(
        choices=OCCASIONS,
        label="Привід"
    )
