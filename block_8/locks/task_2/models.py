from django.db import (
    models,
)


class Account(models.Model):

    balance = models.IntegerField(default=0)
    version = models.IntegerField(default=0)

    class Meta:
        db_table = 'locks_2_account'

    def deposit(self, amount):

        data = Account.objects.filter(pk=self.pk, version=self.version).first() or None

        if data is None:
            data = Account.objects.get(pk=self.pk)

        data.balance += amount
        data.version += 1
        data.save()

    def withdraw(self, amount):

        if self.balance < amount:
            raise ValueError('Сумма снятия больше, чем баланс счета')

        data = Account.objects.filter(pk=self.pk, version=self.version).first() or None

        if data is None:
            data = Account.objects.get(pk=self.pk)

        data.balance -= amount
        data.version += 1
        data.save()



