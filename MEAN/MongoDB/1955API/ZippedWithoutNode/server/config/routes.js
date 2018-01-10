// here we load the Quote model that we created on the server.js page
// var mongoose = require('mongoose');
var people = require('../controllers/People.js')
module.exports = function(app) {
  app.get('/', people.show)
  app.get('/new/:name', people.create)
  app.get('/remove/:name', people.remove)
  app.get('/:name', people.profile)
}
