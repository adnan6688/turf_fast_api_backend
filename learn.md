autoflush=True

You write a letter and place it on the table. If needed, your assistant automatically sends it to the post office.

Write Letter
      ↓
Assistant sends automatically
      ↓
Post Office



autoflush=False

You write a letter and keep it on the table. It will stay there until you say:

"Send it now."

Then you manually send it to the post office.

Write Letter
      ↓
Keep on table
      ↓
You call flush/commit
      ↓
Post Office

Remember:

autoflush=True → SQLAlchemy automatically calls flush() before necessary queries.
autoflush=False → You decide when to call flush() or commit().




<!-- 
 Session কী?

Session হলো database এর সাথে কাজ করার workspace।
এই db দিয়ে আমরা করি:

Data Read
users = db.query(User).all()
Data Insert
db.add(new_user)
db.commit()
Data Update
user.name = "Adnan"
db.commit()
Data Delete
db.delete(user)
db.commit()
 -->


 <!-- 
 sessionLocal 
 
SessionLocal (factory)
      |
      ↓
db = SessionLocal()
      |
      ↓
db হলো Session object




get_db() এর ভিতরে এটা কীভাবে কাজ করে?

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Flow:

Request
   ↓
SessionLocal()
   ↓
db Session তৈরি
   ↓
API route এ পাঠানো
   ↓
CRUD Operation
   ↓
close()
  -->