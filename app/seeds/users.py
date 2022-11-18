from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        email='demo@aa.io', password='password', first_name="Demo", last_name="User", buy_power=100000)
    curtis = User(
        email='curtis@gmail.com', password='password', first_name="Curtis", last_name="Chung", buy_power=100000)
    dylan = User(
        email='dylan@gmail.com', password='password', first_name="Dylan", last_name="Luu", buy_power=100000)
    jarrod = User(
        email ='jarrod@gmail.com', password='password', first_name="Jarrod", last_name="Mishima", buy_power=100000)
    nhut = User(
        email='nhut@gmail.com', password='password', first_name="Nhut", last_name="Ngo", buy_power=100000)
    rec_dummy = User(
        email="thereccuser@gmail.com", password="dontgoherebro", first_name="Recc", last_name="User", buy_power=100000)

    db.session.add(demo)
    db.session.add(curtis)
    db.session.add(dylan)
    db.session.add(jarrod)
    db.session.add(nhut)
    db.session.add(rec_dummy)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
