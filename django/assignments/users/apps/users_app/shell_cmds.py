# retrieve all users
User.objects.all()


# get the last user
User.objects.last()


# add several records
phoebe = User(first_name='Phoebe', last_name='Bones-Prewett', email_address='phoebe@retrograde.com', age=27)
phoebe.save()
# alternative method of adding records
User.objects.create(first_name='Hermia', last_name='Bones-Prewett', email_address='hrbp@aurora.com', age=27)
User.objects.create(first_name='Vesper', last_name='Soren', email_address='vs@aurora.com', age=30)
User.objects.create(first_name='Val', last_name='Cassini', email_address='drvc@aurora.com', age=247)


# get the first user
User.objects.first()


# get the users ordered by first_name DESC
User.objects.order_by('-first_name')


# get the record for id=3 & change last name, using .get and .save
three = User.objects.get(id=3)
three.last_name = 'Søren'
three.save()


# delete a the record of user where id=4
User.objects.get(id=4).delete()
