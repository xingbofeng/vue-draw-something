from pymongo.write_concern import WriteConcern

from pymodm import MongoModel, fields


class User(MongoModel):
  username = fields.CharField(primary_key=True)
  password = fields.CharField()
  email = fields.EmailField()
  nickname = fields.CharField()
  birthday = fields.CharField()
  sex = fields.CharField()
  
  class Meta:
    write_concern = WriteConcern(j=True)
    connection_alias = 'draw'
  def getAll(self):
    return {
      'username': self.username,
      'password': self.password,
      'email': self.email,
      'nickname': self.nickname,
      'birthday': self.birthday,
      'sex': self.sex,
    }
