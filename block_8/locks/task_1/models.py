from django.db import (
    models
)

from django.db import (
    transaction
)


class Account(models.Model):

    balance = models.IntegerField(default=0)

    class Meta:
        db_table = 'locks_1_account'

    @classmethod
    def deposit(cls, amount):
        with transaction.atomic():
            account = (cls.objects.select_for_update().get())
            account.balance += amount
            account.save()

        return account

    @classmethod
    def withdraw(cls, amount):
        with transaction.atomic():
            account = (cls.objects.select_for_update().get())

            if account.balance < amount:
                raise ValueError('Сумма снятия больше, чем баланс счета')

        account.balance -= amount
        account.save()

        return account

