var users = require('../controllers/users.js')
module.exports = function(app) {
  app.get('/', users.show),
  app.post('/register', users.register)
}