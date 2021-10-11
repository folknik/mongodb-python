print('Start #################################################################');

db = db.getSiblingDB('eco_db');
db.createUser(
  {
    user: 'eco',
    pwd: 'eco',
    roles: [{ role: 'readWrite', db: 'eco_db' }],
  },
);
db.createCollection('users');

print('END #################################################################');